"""
Здесь происходит обучение и сохранение модели
"""

import os
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.vec_env import DummyVecEnv

from ModelMaxArea import ModelMaxArea
from ModelPtP import ModelPtP

from time import time

if __name__ == "__main__":
    save_path = './models'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # educate one of two possible models
    env = ModelMaxArea()
    # env = ModelPtP()

    env = DummyVecEnv([lambda: env])  # Векторизация окружения

    # Настройка гиперпараметров
    model = A2C('MlpPolicy', env, verbose=1, learning_rate=0.001, n_steps=2048)

    total_timesteps = 10_000
    iters = 0

    # Логирование и мониторинг
    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path=save_path, name_prefix='model')

    while True:
        iters += 1
        start = time()
        model.learn(total_timesteps=total_timesteps, callback=checkpoint_callback)
        end = time()

        if iters % 10 == 0:
            model.save(f"{save_path}/{iters % 10}")
            print(f'Epoch {iters % 10} is Saved!!!')
            print(f'Time taken for epoch {iters % 10}: {end - start} seconds')
