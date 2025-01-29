"""
Здесь происходит обучение и сохранение модели

"""
import os
from stable_baselines3 import A2C

from Model_max_area import ModelMaxArea
from ModelPtP import ModelPtP

from time import time


if __name__ == "__main__":
    save_path = './models'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # educate one of two possible models
    env = ModelMaxArea()
    # env = ModelPtP()
    env.reset()

    model = A2C('MlpPolicy', env, verbose=1)

    steps_to_save = 100000
    iters = 0
    while True:
        iters += 1
        start = time()
        model.learn(total_timesteps=steps_to_save)
        model.save(f"{save_path}/{iters}_epoch_2")
