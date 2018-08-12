import gym
import random
env = gym.make('GridWorld-v0')
actions = ['n','e','s','w']
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action_temp=actions[int(random.random() * len(actions))]
        print(action_temp)
        observation, reward, done, info = env.step(action_temp)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
env.close()