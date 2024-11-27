"""
Файл, хранящий основную информацию о БпЛА (радиус ретранслятора, скорость, зарядка)
"""

import pygame as pg


class Drone:
    """
    main class for 2 types of drones
    """

    def __init__(self):
        """
        initialize main characteristics
        """
        self.retransmission_radius = 200
        self.speed = 20

        # global DRONE, DRONES_RECT
        self.DRONES = {'master': {}, 'slave': {}}       # хранение ссылок на созданные объекты
        self.DRONES_RECT = {'master': {}, 'slave': {}}  # хранение объектов в виде "прямоугольника"
        self.last_master_id = 1
        self.last_slave_id = 1

    def draw(self, window):
        """
        draw drones on selected area
        :param window: window there drone will be drawn
        :return: new frame on drawing window
        """
        window.blit(self.DRONES['master'][1], self.DRONES_RECT['master'][1])  # draw DRONES
        pg.draw.circle(window, pg.Color('blue'),
                       self.DRONES_RECT['master'][1].center, self.retransmission_radius, 2)  # draw circle around DRONES


class Master(Drone):
    """
    This class responsible for all actions and settings of drone-master
    """

    def __init__(self):
        super().__init__()
        self.icon = pg.image.load('images/MASTER_drone.png')
        # generate master position on center of game window

        self.DRONES['master'] = {
            self.last_master_id: self.icon
        }

        # TODO add settings to generate drones positions
        self.DRONES_RECT['master'] = {
            self.last_master_id: self.DRONES['master'][1].get_rect(centerx=640, centery=360)
        }

        self.last_master_id += 1


if __name__ == "__main__":
    drone = Drone()

    windo

    drone.draw(window)
