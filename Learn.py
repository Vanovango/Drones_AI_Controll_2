"""
Здесь описана логика агента, алгоритм расчета награды по выбранному действию,
а также изменение данных окружения
"""
import os
from stable_baselines3 import A2C

from Model import Model


if __name__ == "__main__":
    save_path = './models/models'
    # log_dir = './models/log'      verbose=1, tensorboard_log=log_dir,

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    env = Model()
    env.reset()

    model = A2C('MlpPolicy', env, device='cuda')

    steps_to_save = 10000
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=steps_to_save, reset_num_timesteps=False, tb_log_name=f"A2C")
        model.save(f"{save_path}/{iters}_epoch")
