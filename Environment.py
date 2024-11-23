"""
Файл описывающий окружение для нейронной сети, он является хранилищем данных
Никаких действий не выполняет
"""
import pygame as pg


class Environment:
    """
    This class responsible for all events in the game
    """

    def __init__(self, n_drones: int):
        """
        initial all needed parameters.
        Main task is create list of drones coordinates [[x_1, y_1], [x_2, y_2], ... [x_n, y_n]]
        :param n_drones: int
        """
        # initial main parameters
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60
        self.retransmission_radius = 200

        # drones parameters
        self.n_drones = n_drones
        self.all_drones = {}
        self.drones_rect = {}

        # initial main window
        self.window = pg.display.set_mode((self.WIDTH, self.HIGH))
        self.clock = pg.time.Clock()

        # create master and slave objects (dict)
        for i in range(self.n_drones + 1):
            if i == 0:
                self.all_drones = {i: pg.image.load('./images/MASTER_drone.png')}
            else:
                self.all_drones = {i: pg.image.load('./images/SLAVE_drone.png')}

        # create rects of all drones (dict)
        for i in range(self.n_drones + 1):
            if i == 0:
                self.drones_rect = {i: self.all_drones[i].get_rect(centerx=self.WIDTH // 2, centery=self.HIGH // 2)}
            else:
                self.drones_rect = {i: self.all_drones[i].get_rect(centerx=self.WIDTH // 2, centery=self.HIGH // 2)}

        # save all drones positions (list)
        self.drones_coordinates = [[self.drones_rect[i].centerx, self.drones_rect[i].centery] for i in self.drones_rect]

    def draw_all(self):
        """
        drawing all objects
        """

        self.window.fill(pg.Color('black'))

        # draw all drones and circle around they
        for drone, rect in self.all_drones.values(), self.drones_rect.values():
            self.window.blit(drone, rect)
            pg.draw.circle(self.window, pg.Color('blue'), rect.center, self.retransmission_radius, 2)

        pg.display.update()
        self.clock.tick(self.FPS)
