import gym
import universe # register the universe environments
import cv2
import numpy as np
import matplotlib as plt
import vnc_recorder
import pyscreenshot as ImageGrab
import pyscreeze
from universe.spaces.vnc_event import VNCEvent, KeyEvent, PointerEvent
import random

reward = 0
score = 0
g = True
h = True


env = gym.make('flashgames.SuperDash-v0')
env.configure(remotes=1) # create one flashgames Docker container
observation_n = env.reset()

x = 2
y = 0
z = 0
d = 0
p = 0

while True:
  # your agent generates action_n at 60 frames per second

        
        a = random.randint(30, 100)
        b = random.randint(1, 10)
	c = random.randint(1, 50)

	action_n = [[('KeyEvent','x',True),('KeyEvent','x',False)] for ob in observation_n]
        observation_n, reward_n, done_n, info = env.step(action_n)


        if  x > a and d < abs(50) and p < -50:
                x -= 1
                
                action_n = [[('KeyEvent','d',True),('KeyEvent','a',False)] for ob in observation_n]
                observation_n, reward_n, done_n, info = env.step(action_n)
		y += 2
		if y % 2 == 0:
			action_n = [[('KeyEvent','w',True),('KeyEvent','w',False)] for ob in observation_n]
                	observation_n, reward_n, done_n, info = env.step(action_n)
		d += 1
		p -= 10
		if p < -120:
			p = abs(p)
					
		if y > 1000:
			x -= 100
			y = 500
        else:
		p += 10
                if p > 80:
                	p = -p
                	action_n = [[('KeyEvent','a',True),('KeyEvent','d',False)] for ob in observation_n]
                	observation_n, reward_n, done_n, info = env.step(action_n)
			x += 2
			if y % 2 != 0:
				action_n = [[('KeyEvent','w',True),('KeyEvent','w',False)] for ob in observation_n]
                		observation_n, reward_n, done_n, info = env.step(action_n)
			if d == abs(50):
				d = 100
			d -= 3
	if c > 1:
		action_n = [[('KeyEvent','w',True),('KeyEvent','w',False)] for ob in observation_n]
                observation_n, reward_n, done_n, info = env.step(action_n)


	
        #print info['n'][0]['stats.reward.count']

        env.render()

