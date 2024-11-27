"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

Load model and test it
"""
from stable_baselines3 import A2C
from Model import Model
import sys
from MainWindow import UiMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame as pg


def start_demon_demonstration():
    load_model_path = 'C:/Code/pythonProjects/Drones_AI_Controll_2/models/1_epoch.zip'

    env = Model()
    env.reset()

    model = A2C('MlpPolicy', env, verbose=1)
    model.load(path=load_model_path)

    obs = env.reset()[0]
    while True:
        actions = model.predict(obs)[0]
        obs, reward = env.step(actions)[:2]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    ui.button_start_demonstration.clicked.connect(start_demon_demonstration)

    sys.exit(app.exec_())
