"""
Файл для связывания проекта воедино
Из него будет происходить запуск всей программы

Load model and test it
"""
from stable_baselines3 import A2C
from Model import Model


if __name__ == "__main__":
    load_model_path = './models/models/130_epoch.zip'
    print(f"load model - {load_model_path}")

    env = Model()
    env.reset()

    model = A2C('MlpPolicy', env, verbose=1)
    model.load(path=load_model_path)

    obs, info = env.reset()
    while True:  # not done:
        actions = model.predict(obs)[0]
        obs, reward = env.step(actions)[:2]
        # test print
        # print("action", actions)
        # print('reward', reward)


