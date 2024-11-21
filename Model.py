"""
Инициализация модели нейронной сети, выбор действия по входным данным

Пока что очень много непонятого, нужно продолжать рыться в интернете
"""

import random

import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import clone_model
from tensorflow.keras.optimizers import Adam

from Environment import env


# get current state as a vector of features
def get_state(obs):
    v = []
    x, y = obs['player']
    v.append(x)
    v.append(y)
    for x, y in obs['monsters']:
        v.append(x)
        v.append(y)
    for x, y in obs['diamonds']:
        v.append(x)
        v.append(y)
    for x, y in obs['walls']:
        v.append(x)
        v.append(y)
    return v


# конструируем DQN
def dqn(shapes, actions):
    """

    :param shapes: входной слой - возможное число состояний
    :param actions: действия
    :return:
    """
    model = Sequential()
    model.add(Dense(units=64, input_shape=shapes, activation='relu'))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


def epsilon_greedy(q_values, epsilon, n_outputs):
    if random.random() < epsilon:
        return random.randrange(n_outputs)  # random action
    else:
        return np.argmax(q_values)  # q-optimal action


# Гиперпараметры
number_of_steps = 200_000  # количество раз, сколько мы корректируем вес
w = 10_000  # первые итерации после перед началом обучения
interval_of_training = 5  # количество шагов, после которых мы корректируем веса
new_steps = 10_000  # количество шагов, после которых веса online network  копируются в target network
g = 0.99  # ставка дисконтирования
batch = 64  # размер батча
epsilon_maximum = 1.0  # epsilon max
epsilon_minimum = 0.05  # epsilon min
epsilon_decay_steps = int(number_of_steps / 2)
learning_rate = 0.001

memory = []  # массив для хранения прошлых шагов
actions = ['up', 'down', 'left', 'right', 'stay']  # массив с возможными шагами ('up', 'down', 'left', 'right', 'stay')
shapes = []

online = dqn(shapes, actions)
online.compile(optimizer=Adam(learning_rate), loss='mse')
target = clone_model(online)
target.set_weights(online.get_weights())

# тренируем модель
step = 0  # our start
iteration = 0
do = True
while step < number_of_steps:
    if do:
        observation = env.reset()
    iter += 1
    q = online.predict(np.array([get_state(observation)]))[0]
    epsilon_for_training = max(epsilon_minimum,
                               epsilon_maximum - (epsilon_maximum - epsilon_minimum) * step / epsilon_decay_steps)
    action_go = epsilon_greedy(q, epsilon_for_training, actions)
    next_observation = env.make_action(action_go + 1)
    r = next_observation["reward"]
    do = next_observation["end_game"]
    memory.append((observation, action_go, r, next_observation, do))
    observation = next_observation

    if iter >= w and iter % interval_of_training == 0:
        step += 1
        min_batch = random.sample(memory, batch)
        state = np.array([get_state(x[0]) for x in min_batch])
        action = np.array([x[1] for x in min_batch])
        rewards = np.array([x[2] for x in min_batch])
        next_state = np.array([get_state(x[3]) for x in min_batch])
        replay_done = np.array([x[4] for x in min_batch], dtype=int)
        target_for_action = rewards + (1 - replay_done) * g * \
                            np.amax(target.predict(next_state), axis=1)
        target = online.predict(state)
        target[np.arange(batch), action] = target_for_action
        online.fit(state, target, epochs=step, verbose=1, initial_epoch=step - 1)
        if step % new_steps == 0:
            target.set_weights(online.get_weights())
