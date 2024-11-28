"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

"""
import sys

import pygame as pg
from PyQt5 import QtWidgets
from stable_baselines3 import A2C

from MainWindow import UiMainWindow
from Model import Model
from SettingsWindow import UiSettingsWindow

MODEL_SETTINGS = {'n_drones': 6,
                  'speed': 15,
                  'retransmission_radius': 150}


def demonstration(env):
    load_model_path = './models/1_epoch.zip'

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
                    done = True
            elif event.type == pg.QUIT:
                done = True


def open_main_window():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    class_main = UiMainWindow()
    class_main.setupUi(MainWindow)

    MainWindow.show()

    def start_demonstration_from_main():
        env = Model()
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

        def start_demonstration_from_settings():
            env = Model(n_drones=int(class_settings.lineEdit_n_drones.text()),
                        speed=int(class_settings.lineEdit_drone_speed.text()),
                        retransmission_radius=int(class_settings.lineEdit_retransmission_radius.text()))
            env.reset()

            demonstration(env)

            # close Pygame window
            pg.quit()
            pg.display.quit()
            # show MainWindow again
            SettingsWindow.close()
            MainWindow.show()

        def back_to_main():
            SettingsWindow.close()
            open_main_window()

        class_settings.button_start_demonstration.clicked.connect(start_demonstration_from_settings)
        class_settings.button_back.clicked.connect(back_to_main)

    class_main.button_start_demonstration.clicked.connect(start_demonstration_from_main)
    class_main.button_model_settings.clicked.connect(open_settings_window)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    open_main_window()

    sys.exit(app.exec_())
