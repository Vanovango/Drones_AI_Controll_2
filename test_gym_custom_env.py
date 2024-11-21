"""
0 - up, 1 -down, 2 - left, 3 - right, 4 - stay
actions = {
            0: self.observation_state.move_ip(0, -self.speed),
            1: self.observation_state.move_ip(0, +self.speed),
            2: self.observation_state.move_ip(-self.speed, 0),
            3: self.observation_state.move_ip(+self.speed, 0),
            4: self.observation_state.move_ip(0, 0)
        }
"""

import gymnasium as gym
import numpy as np
from gymnasium import spaces
import pygame as pg
from collections import deque
import time
import cv2


class Game:
    """
    This class responsible for all events in the game
    """

    def __init__(self):
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60
        self.retransmission_radius = 200

        self.window = pg.display.set_mode((self.WIDTH, self.HIGH))
        self.clock = pg.time.Clock()

        self.drone = pg.image.load('./images/MASTER_drone.png')
        self.drone_rect = self.drone.get_rect(centerx=640, centery=360)

    def draw_all(self):
        """
        drawing all objects
        """

        self.window.fill(pg.Color('black'))

        # draw rectangles for test agent movement
        rect_w = 30
        rect_h = 30

        pg.draw.rect(self.window, (0, 255, 0), (100, 100, rect_w, rect_h))  # x, y, w, h
        pg.draw.rect(self.window, (0, 255, 0), (600, 600, rect_w, rect_h))
        pg.draw.rect(self.window, (0, 255, 0), (600, 100, rect_w, rect_h))
        pg.draw.rect(self.window, (0, 255, 0), (100, 600, rect_w, rect_h))
        pg.draw.rect(self.window, (0, 255, 0), (1200, 300, rect_w, rect_h))

        # draw drone and circle around it
        self.window.blit(self.drone, self.drone_rect)
        pg.draw.circle(self.window, pg.Color('blue'), self.drone_rect.center, self.retransmission_radius, 2)

        pg.display.update()
        self.clock.tick(self.FPS)

    def start_game(self):
        """
        def for start environment
        :return: None
        """

        while True:
            self.draw_all()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit


test_time = 30
n_discrete_action = 4


class DroneEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self):
        super(DroneEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(n_discrete_action)
        # Example for using image as input (channel-first; channel-last also works):
        # (7 + test_time) == observation -> int
        self.observation_space = spaces.Box(low=0, high=1280,
                                            shape=(7 + test_time,), dtype=np.uint8)

        # Initial main parameters
        self.prev_actions = None
        self.reward = None
        self.done = None
        self.window = Game()
        self.speed = 20

        self.possible_actions = {
            0: self.window.drone_rect.move_ip(0, -self.speed),
            1: self.window.drone_rect.move_ip(0, +self.speed),
            2: self.window.drone_rect.move_ip(-self.speed, 0),
            3: self.window.drone_rect.move_ip(+self.speed, 0)
        }

    def step(self, action):
        self.prev_actions.append(action)    # add action to history (0, 1, 2, 3)
        self.window.draw_all()  # draw objects on window

        # Takes step after fixed time
        t_end = time.time() + 0.05
        k = -1
        while time.time() < t_end:
            if k == -1:
                k = cv2.waitKey(1)
            else:
                continue

            # Change the drone position based on the action
            if button_direction == 1:
                self.snake_head[0] += 10
            elif button_direction == 0:
                self.snake_head[0] -= 10
            elif button_direction == 2:
                self.snake_head[1] += 10
            elif button_direction == 3:
                self.snake_head[1] -= 10


        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        """
        Function move program to the start position
        :return: observation, info
        """
        self.window.__init__()

        # reset main parameters
        self.reward = 0
        self.done = False

        # Initial drones position
        drone_x = self.window.drone_rect.center()[0]
        drone_y = self.window.drone_rect.center()[1]

        other_drones = [[100, 100], [600, 600], [100, 600], [600, 100], [1200, 300]]

        # however long we aspire the drone to be
        self.prev_actions = deque(maxlen=test_time)
        for i in range(test_time):
            self.prev_actions.append(-1)  # to create history

        # create observation
        observation = [drone_x, drone_y] + list(other_drones) + list(self.prev_actions)
        observation = np.array(observation)

        info = {}
        return observation, info


if __name__ == "__main__":
    game = Game()
    game.start_game()
