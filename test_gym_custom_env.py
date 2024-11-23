"""
0 - up, 1 -down, 2 - left, 3 - right, 4 - stay
"""

import time
from collections import deque

import cv2
import gymnasium as gym
import numpy as np
import pygame as pg
from gymnasium import spaces

from stable_baselines3 import PPO
import os



class Game:
    """
    This class responsible for all events in the game
    """

    def __init__(self):
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60
        self.retransmission_radius = 200

        self.other_drones = [[100, 100], [600, 600], [100, 600], [600, 100], [1200, 300], [900, 150], [800, 400]]

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
        pg.draw.rect(self.window, (0, 255, 0), (900, 150, rect_w, rect_h))
        pg.draw.rect(self.window, (0, 255, 0), (800, 400, rect_w, rect_h))

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


def test_prints(func=None, done=None, reward=None, action_number=None):
    # test prints
    print(f"========================================================================")
    print(f'{func}')
    print(f"------------------------------------------------------------------------")
    print(f"done --- {done}")
    print(f"reward --- {reward}")
    print(f"action number --- {action_number}")
    print(f"========================================================================")


HISTORY_LEN = 30
TOTAL_ACTIONS = 30
N_DISCRETE_ACTIONS = 4


class DroneEnv(gym.Env):
    """Custom Environment that follows gym interface."""
    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super(DroneEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        # (7 + test_time) == observation -> int
        self.observation_space = spaces.Box(low=-1, high=1280,
                                            shape=(16 + HISTORY_LEN,), dtype=np.int32)

        # Initial main parameters
        self.prev_actions = None
        self.reward = None
        self.done = False
        self.window = Game()
        self.speed = 15
        self.action_number = 0

    def step(self, action):
        self.prev_actions.append(action)  # add action to history (0, 1, 2, 3)
        self.action_number += 1
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
        # 0 - up, 1 - down, 2 - left, 3 - right, 4 - stay
        # possible_actions = {
        #     0: self.window.drone_rect.move_ip(0, -self.speed),
        #     1: self.window.drone_rect.move_ip(0, +self.speed),
        #     2: self.window.drone_rect.move_ip(-self.speed, 0),
        #     3: self.window.drone_rect.move_ip(+self.speed, 0)
        # }

        if action == 0:
            self.window.drone_rect.move_ip(0, -self.speed)
        elif action == 1:
            self.window.drone_rect.move_ip(0, +self.speed)
        elif action == 2:
            self.window.drone_rect.move_ip(-self.speed, 0)
        elif action == 3:
            self.window.drone_rect.move_ip(+self.speed, 0)

        # calculate reward
        drone_x = self.window.drone_rect.centerx
        drone_y = self.window.drone_rect.centery

        connections = 0
        for x, y in self.window.other_drones:
            if (abs(x - drone_x) ** 2 + abs(y - drone_y) ** 2) ** 0.5 <= 200:
                connections += 1
        change_reward = {
            0: -5,
            1: -3,
            2: 3,
            3: 5,
            4: -5
        }
        self.reward += change_reward[connections]

        if self.action_number == TOTAL_ACTIONS:
            self.done = True
            test_prints(reward=self.reward)

        # update observation
        cut_obs = [drone_x, drone_y]
        for x, y in self.window.other_drones:
            cut_obs.append(x)
            cut_obs.append(y)



        observation = cut_obs + list(self.prev_actions)
        observation = np.array(observation)

        terminated = self.done
        truncated = False
        info = {}

        return observation, self.reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        """
        Function move program to the start position
        :return: observation, info
        """
        self.window.__init__()

        # reset main parameters
        self.reward = 0
        self.action_number = 0
        self.done = False

        # Initial drones position
        drone_x = self.window.drone_rect.centerx
        drone_y = self.window.drone_rect.centery

        # however long we aspire the drone to be
        self.prev_actions = deque(maxlen=HISTORY_LEN)
        for i in range(HISTORY_LEN):
            self.prev_actions.append(-1)  # to create history

        # create observation
        cut_obs = [drone_x, drone_y]
        for x, y in self.window.other_drones:
            cut_obs.append(x)
            cut_obs.append(y)

        # test_prints(func='reset', done=self.done, reward=self.reward, action_number=self.action_number)

        observation = cut_obs + list(self.prev_actions)
        observation = np.array(observation)

        info = {}

        return observation, info


if __name__ == "__main__":
    save_path = './models/models'
    log_dir = './models/log'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    env = DroneEnv()
    env.reset()

    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_dir)

    TIMESTEPS = 10000
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
        model.save(f"{save_path}/{TIMESTEPS * iters}_iterations")
