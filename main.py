"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

"""
import sys
import time

import pygame as pg
from PyQt5 import QtWidgets
from stable_baselines3 import A2C

from MainWindow import UiMainWindow
from Model_max_area import ModelMaxArea
from SettingsWindow import UiSettingsWindow


def pause():
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return False
                elif event.key == pg.K_ESCAPE:
                    return True
            elif event.type == pg.QUIT:
                return True


def demonstration(env, construction='Максимальная площадь'):
    # chose model based on construction
    if construction == 'Точка - точка':
        load_model_path = './models/1_epoch.zip'
    else:
        load_model_path = './models/max_area_model.zip'

    model = A2C('MlpPolicy', env, verbose=1)
    model.load(path=load_model_path)

    done = False
    obs = env.reset()[0]
    while not done:
        actions = model.predict(obs)[0]
        obs, reward = env.step(actions)[:2]

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True                 # close demonstration window

                elif event.key == pg.K_SPACE:
                    done = pause()              # pause the demonstration

            elif event.type == pg.QUIT:
                done = True                     # close demonstration window


def open_main_window():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    class_main = UiMainWindow()
    class_main.setupUi(MainWindow)

    MainWindow.show()

    def start_demonstration_from_main():
        env = ModelMaxArea()
        env.reset()

        demonstration(env)

        # close Pygame window
        pg.quit()
        pg.display.quit()
        # show MainWindow again
        MainWindow.show()

    def open_settings_window():
        global SettingsWindow
        SettingsWindow = QtWidgets.QMainWindow()
        class_settings = UiSettingsWindow()
        class_settings.setupUi(SettingsWindow)

        SettingsWindow.show()
        MainWindow.close()

        def start_demonstration_from_settings(n_drones, speed, retransmission_radius, map_path, construction):
            env = ModelMaxArea(n_drones=n_drones, speed=speed, retransmission_radius=retransmission_radius,
                               map_path=map_path, construction=construction)
            env.reset()

            demonstration(env, construction)

            # close Pygame window
            pg.quit()
            pg.display.quit()
            # show MainWindow again
            SettingsWindow.close()
            MainWindow.show()

        def open_map():
            class_settings.get_map_path()

        def back_to_main():
            SettingsWindow.close()
            open_main_window()

        def check_values():
            n_drones = class_settings.lineEdit_n_drones.text()
            speed = class_settings.lineEdit_drone_speed.text()
            retransmission_radius = class_settings.lineEdit_retransmission_radius.text()
            map_path = class_settings.label_map_path.text()
            construction = class_settings.comboBox_construction_type.currentText()

            if n_drones == '' or speed == '' or retransmission_radius == '' or map_path == '':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Проверьте заполненность всех полей")
                msg.setWindowTitle("ValueError")
                msg.exec_()
            else:
                start_demonstration_from_settings(int(n_drones),
                                                  int(speed),
                                                  int(retransmission_radius),
                                                  map_path,
                                                  construction)

        class_settings.button_start_demonstration.clicked.connect(check_values)
        class_settings.button_back.clicked.connect(back_to_main)
        class_settings.button_open_map.clicked.connect(open_map)

    class_main.button_start_demonstration.clicked.connect(start_demonstration_from_main)
    class_main.button_model_settings.clicked.connect(open_settings_window)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    open_main_window()

    sys.exit(app.exec_())
