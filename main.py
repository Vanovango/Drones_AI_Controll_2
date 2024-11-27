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


def open_main_window():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    class_main = UiMainWindow()
    class_main.setupUi(MainWindow)

    MainWindow.show()

    class_main.button_start_demonstration.clicked.connect(start_demonstration)
    class_main.button_model_settings.clicked.connect(go_to_settings)


def start_demonstration():
    load_model_path = './models/1_epoch.zip'

    env = Model()
    env.reset()

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
    # close Pygame window
    pg.quit()
    pg.display.quit()
    # show MainWindow again
    if SettingsWindow.isVisible():
        SettingsWindow.close()

    MainWindow.show()


def back_to_main():
    SettingsWindow.close()
    open_main_window()


def go_to_settings():
    global SettingsWindow
    SettingsWindow = QtWidgets.QMainWindow()
    class_settings = UiSettingsWindow()
    class_settings.setupUi(SettingsWindow)

    SettingsWindow.show()
    MainWindow.close()

    class_settings.button_start_demonstration.clicked.connect(start_demonstration)
    class_settings.button_back.clicked.connect(back_to_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    open_main_window()

    sys.exit(app.exec_())
