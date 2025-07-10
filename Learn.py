"""
Здесь происходит обучение и сохранение модели

"""
import os
from stable_baselines3 import A2C

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

    env.reset()

    model = A2C('MlpPolicy', env, verbose=1)

    total_timesteps = 10_000
    iters = 0

    while True:
        iters += 1
        start = time()
        model.learn(total_timesteps=total_timesteps)

        if iters % 10 == 0:
            model.save(f"{save_path}/{iters % 10}_1v")
            print(f'Epoch {iters % 10} is Saved!!!')
