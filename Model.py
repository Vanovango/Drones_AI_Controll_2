"""
Инициализация модели нейронной сети, выбор действия по входным данным

"""

import time
from collections import deque

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces

from Environment import Environment

TOTAL_ACTIONS = 30
N_DISCRETE_ACTIONS = 5
HISTORY_LEN = 30 * N_DISCRETE_ACTIONS


class Model(gym.Env):
    """Custom Environment that follows gym interface."""
    metadata = {"render_modes": ["human"]}

    def __init__(self, n_drones=6, speed=15, retransmission_radius=150):
        # Initial main parameters
        self.speed = speed
        self.n_drones = n_drones
        self.retransmission_radius = retransmission_radius

        self.actions_history = None
        self.reward = None
        self.done = False
        self.window = Environment(n_drones=self.n_drones, retransmission_radius=self.retransmission_radius)
        self.action_number = 0

        # possible reward changes
        self.change_reward = {
            0: -5,
            1: -3,
            2: 3,
            3: 5,
            4: 7,
            5: -5,
            6: -5
        }

        # Define action and observation space
        # They must be gym.spaces objects
        self.action_space = spaces.MultiDiscrete([N_DISCRETE_ACTIONS] * n_drones)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=-1, high=1280,
                                            shape=(n_drones * 2 + HISTORY_LEN,),
                                            dtype=np.int32)

    def step(self, actions):
        self.actions_history += list(action for action in actions)  # add action to history (0, 1, 2, 3, 5)
        self.action_number += 1
        self.window.draw_all()  # draw objects on window (vizual learning proces)

        # Takes step after fixed time
        # need to vizual
        t_end = time.time() + 0.05
        k = -1
        while time.time() < t_end:
            if k == -1:
                k = cv2.waitKey(1)
            else:
                continue

        # Change the drone position based on the action
        # and save it on rect and coordinates
        for index in range(self.n_drones):
            # 0 - up, 1 - down, 2 - left, 3 - right, 4 - stay
            if actions[index] == 0:
                # go up
                self.window.drones_rect[index].move_ip(0, -self.speed)
                self.window.drones_coordinates[index] = \
                    [self.window.drones_coordinates[index][0], self.window.drones_coordinates[index][1] - self.speed]
            elif actions[index] == 1:
                # go down
                self.window.drones_rect[index].move_ip(0, +self.speed)
                self.window.drones_coordinates[index] = \
                    [self.window.drones_coordinates[index][0], self.window.drones_coordinates[index][1] + self.speed]
            elif actions[index] == 2:
                # go left
                self.window.drones_rect[index].move_ip(-self.speed, 0)
                self.window.drones_coordinates[index] = \
                    [self.window.drones_coordinates[index][0] - self.speed, self.window.drones_coordinates[index][1]]
            elif actions[index] == 3:
                # go right
                self.window.drones_rect[index].move_ip(+self.speed, 0)
                self.window.drones_coordinates[index] = \
                    [self.window.drones_coordinates[index][0] + self.speed, self.window.drones_coordinates[index][1]]
            elif actions[index] == 4:
                # nothing to do
                self.window.drones_rect[index].move_ip(0, 0)

        # calculate overall reward
        for index in range(self.n_drones):
            drone_x = self.window.drones_rect[index].centerx
            drone_y = self.window.drones_rect[index].centery

            connections = -1    # because this variable calculate himself at once
            for x, y in self.window.drones_coordinates:
                distance = (abs(x - drone_x) ** 2 + abs(y - drone_y) ** 2) ** 0.5
                if self.window.retransmission_radius - 50 <= distance <= self.window.retransmission_radius:
                    connections += 1
            if connections == -1:
                connections = 0
            self.reward += self.change_reward[connections]

        # tracks the end of an episode
        if self.action_number == TOTAL_ACTIONS:
            self.done = True
            # print(f"total reward = {self.reward}")

        # update observation
        coordinates_list = []
        for x, y in self.window.drones_coordinates:
            coordinates_list.append(x)
            coordinates_list.append(y)

        observation = coordinates_list + list(self.actions_history)
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

    # def close(self):
    #     self.window.
