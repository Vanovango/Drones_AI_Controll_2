"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

Load model and test it
"""
from stable_baselines3 import A2C
from Model import Model


if __name__ == "__main__":
    load_model_path = './models/models/130_epoch.zip'

    env = Model()
    env.reset()

    model = A2C('MlpPolicy', env, verbose=1)
    model.load(path=load_model_path)

    episodes = 50

    for episode in range(episodes):
        done = False
        obs, info = env.reset()
        while True:  # not done:
            actions = model.predict(obs)[0]
            print("action", actions)
            obs, reward, done, truncated, info = env.step(actions)
            print('reward', reward)
