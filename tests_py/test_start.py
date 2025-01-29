"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

Load model and test it
"""
from stable_baselines3 import A2C
from Model_max_area import ModelMaxArea
import sys
from MainWindow import UiMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame as pg


def open_main_window():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    class_main = UiMainWindow()
    class_main.setupUi(MainWindow)

    MainWindow.show()

    class_main.button_start_demonstration.clicked.connect(start_demonstration)
    class_main.button_model_settings.clicked.connect(go_to_settings)


def start_demonstration():
    load_model_path = 'C:/Code/pythonProjects/Drones_AI_Controll_2/models/1_epoch.zip'

    env = ModelMaxArea()
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
                if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    done = True

    # close Pygame window
    pg.quit()
    pg.display.quit()
    # show MainWindow again
    MainWindow.show()


def go_to_settings():
    print("need to create settings window")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    open_main_window()

    sys.exit(app.exec_())
