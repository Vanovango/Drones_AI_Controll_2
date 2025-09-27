"""
Здесь происходит обучение и сохранение модели
"""

import os
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import EvalCallback

from ModelMaxArea import ModelMaxArea
from ModelPtP import ModelPtP

from time import time

def chose_model(model_name):
    if model_name == 'Максимальная площадь':
        return ModelMaxArea()
    elif model_name == 'Точка - точка':
        return ModelPtP()


if __name__ == "__main__":
    model_name = 'Максимальная площадь'
    save_path = './models'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # educate one of two possible models
    env = chose_model(model_name)
    
    env = DummyVecEnv([lambda: env])  # Векторизация окружения

    # Настройка гиперпараметров
    model = A2C('MlpPolicy', env, verbose=1, 
            learning_rate=0.01,  
            n_steps=512,         
            ent_coef=0.01,        
            gamma=0.99)

    total_timesteps = 10_000
    iters = 0

    # Логирование и мониторинг
    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path=save_path, name_prefix='model')
    eval_callback = EvalCallback(env, eval_freq=1000, best_model_save_path='./best_model')
        
    while True:
        iters += 1
        start = time()
        model.learn(total_timesteps=total_timesteps, callback=[checkpoint_callback, eval_callback])
        # model.learn(total_timesteps=total_timesteps, callback=checkpoint_callback)
        end = time()

        if iters % 10 == 0:
            model.save(f"{save_path}/{iters % 10}")
            print(f'Epoch {iters % 10} is Saved!!!')
            print(f'Time taken for epoch {iters % 10}: {end - start} seconds')
