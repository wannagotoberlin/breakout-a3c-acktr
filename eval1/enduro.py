import gym
from gym import wrappers

env = gym.make("EnduroNoFrameskip-v4")
env = wrappers.Monitor(env, "./gym-results")
observation = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)
    if done:
        env.reset()

