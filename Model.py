"""
Инициализация модели нейронной сети, выбор действия по входным данным

Пока что очень много непонятого, нужно продолжать рыться в интернете
"""

import time
from collections import deque

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from Environment import Environment


HISTORY_LEN = 30
TOTAL_ACTIONS = 30
N_DISCRETE_ACTIONS = 5
N_DRONES = 6


class Model(gym.Env):
    """Custom Environment that follows gym interface."""
    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super(Model, self).__init__()

        # Initial main parameters
        self.actions_history = None
        self.reward = None
        self.done = False
        self.window = Environment(N_DRONES)
        self.speed = 15
        self.action_number = 0

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        # (7 + test_time) == observation -> int
        self.observation_space = spaces.Box(low=-1, high=1280,
                                            shape=(len(self.window.drones_coordinates) * 2 + HISTORY_LEN,),
                                            dtype=np.int32)

    # TODO do action for all drone using 'for'. maybe i should invent drone_id to track who is doing the action
    def step(self, action):
        self.actions_history.append(action)  # add action to history (0, 1, 2, 3)
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
        if action == 0:
            self.window.drones_rect.move_ip(0, -self.speed)
        elif action == 1:
            self.window.drones_rect.move_ip(0, +self.speed)
        elif action == 2:
            self.window.drones_rect.move_ip(-self.speed, 0)
        elif action == 3:
            self.window.drones_rect.move_ip(+self.speed, 0)
        elif action == 4:
            self.window.drones_rect.move_ip(0, 0)

        # calculate reward
        drone_x = self.window.drones_rect.centerx
        drone_y = self.window.drones_rect.centery

        connections = 0
        for x, y in self.window.drones_coordinates:
            if (abs(x - drone_x) ** 2 + abs(y - drone_y) ** 2) ** 0.5 <= 200:
                connections += 1
        change_reward = {
            0: -5,
            1: -3,
            2: 3,
            3: 5,
            4: 7,
            5: -5,
            6: -5
        }
        self.reward += change_reward[connections]

        if self.action_number == TOTAL_ACTIONS:
            self.done = True
            # test_prints(reward=self.reward)

        # update observation
        cut_obs = [drone_x, drone_y]
        for x, y in self.window.drones_coordinates:
            cut_obs.append(x)
            cut_obs.append(y)

        observation = cut_obs + list(self.actions_history)
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
        self.window.__init__(N_DRONES)

        # reset main parameters
        self.reward = 0
        self.action_number = 0
        self.done = False

        # however long we aspire the drone to be
        self.actions_history = deque(maxlen=HISTORY_LEN)
        for i in range(HISTORY_LEN):
            self.actions_history.append(-1)  # to create history

        # create list of all drones coordinates
        coordinates_list = []
        for x, y in self.window.drones_coordinates:
            coordinates_list.append(x)
            coordinates_list.append(y)

        # create observation
        observation = coordinates_list + list(self.actions_history)
        observation = np.array(observation)

        info = {}

        return observation, info