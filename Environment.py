"""
Файл описывающий окружение для нейронной сети, он является хранилищем данных
Никаких действий не выполняет, занимается рисованием объектов
"""

import pygame as pg
from PIL import Image

pg.init()   # now use display and fonts


class Environment:
    """
    This class responsible for all events in the game
    """

    def __init__(self, n_drones=6, retransmission_radius=150,
                 map_path='./images/map_1.png', construction='Максимальная площадь'):
        """
        initial all needed parameters.
        Main task is create list of drones coordinates [[x_1, y_1], [x_2, y_2], ... [x_n, y_n]]
        :param n_drones: int
        """
        # initial main parameters
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60
        self.retransmission_radius = retransmission_radius

        # drones parameters
        self.n_drones = n_drones
        self.all_drones = {}
        self.drones_rect = {}

        # initial main window
        self.window = pg.display.set_mode((self.WIDTH, self.HIGH))
        self.clock = pg.time.Clock()

        # create master and slave objects (dict)
        for i in range(self.n_drones):
            if i == 0:
                self.all_drones[i] = pg.image.load('./images/MASTER_drone.png')
            else:
                self.all_drones[i] = pg.image.load('./images/SLAVE_drone.png')

        # create rects of all drones (dict)
        for i in range(self.n_drones):
            if i == 0:
                self.drones_rect[i] = self.all_drones[i].get_rect(centerx=self.WIDTH // 2, centery=self.HIGH // 2)
            else:
                self.drones_rect[i] = self.all_drones[i].get_rect(centerx=self.WIDTH // 2, centery=self.HIGH // 2)

        # save all drones positions (list)
        self.drones_coordinates = list([self.drones_rect[i].centerx, self.drones_rect[i].centery]
                                       for i in self.drones_rect)

        # load background image
        self.background_map = pg.image.load(map_path)

        # points
        self.construction = construction
        pg.font.init()
        self.font = pg.font.SysFont('times new roman', 30)
        self.point_object = pg.image.load('./images/point.png')
        self.points = []  # [{'object': ..., 'coordinates': (x, y)}, {...}]

        # colors
        self.colors = {'red': (255, 0, 0),
                       'green': (0, 255, 0),
                       'blue': (0, 0, 255),
                       'black': (0, 0, 0),
                       'white': (255, 255, 255)}

    def draw_all(self):
        """
        drawing all objects
        """
        self.window.blit(self.background_map, (0, 0))

        # if drones construction is 'Точка - точка'
        if self.construction == 'Точка - точка':
            """
            this part of the code is responsible for drawing points on the map
            """
            while len(self.points) != 2:
                self.window.blit(self.background_map, (0, 0))
                # draw current text
                if len(self.points) < 2:
                    text = self.font.render(f"Осталось точек - {2 - len(self.points)}", True, self.colors['black'])
                    self.window.blit(text, (10, 10))

                # draw the dots if they exist
                if len(self.construction) > 0:
                    for point in self.points:
                        self.window.blit(point['object'], point['coordinates'])

                # check events
                for event in pg.event.get():
                    # Если нажата кнопка мыши и точек меньше чем 2
                    if event.type == pg.MOUSEBUTTONDOWN and len(self.points) < 2:
                        x, y = pg.mouse.get_pos()  # Получение координат нажатия
                        self.points.append({'object': self.point_object,
                                            'coordinates': (x - 13, y - 26)})
                pg.display.update()
                self.clock.tick(self.FPS)

        # draw all drones and circle around they
        for index in range(self.n_drones):
            self.window.blit(self.all_drones[index], self.drones_rect[index])
            pg.draw.circle(self.window, pg.Color('blue'), self.drones_rect[index].center, self.retransmission_radius, 2)

        if len(self.points) == 2:
            for point in self.points:
                self.window.blit(point['object'], point['coordinates'])

            # if 2 points on map, change text and draw the line
            text = self.font.render(f"Точки нанесены", True, self.colors['red'])
            self.window.blit(text, (10, 10))
            # draw the connection line
            print(*self.points)
            pg.draw.line(self.window, self.colors['red'],
                         (self.points[0]['coordinates'][0] + 13, self.points[0]['coordinates'][1] + 26),
                         (self.points[1]['coordinates'][0] + 13, self.points[1]['coordinates'][1] + 26),
                         1)
        # draw help text for stop drones
        stop_help = self.font.render(f"Пауза - 'space'", True, self.colors['black'])
        self.window.blit(stop_help, (1100, 680))

        pg.display.update()
        self.clock.tick(self.FPS)
