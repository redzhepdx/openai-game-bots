import gym
import universe
import random

import numpy
import matplotlib

env = gym.make('flashgames.ObamaAlienDefense-v0')
env.configure(remotes=1) # create one flashgames Docker container
observation_n = env.reset()

#random vars
a = 0
b = 0
c = 0
# training lists
# doesn't work yet as intended
z = [0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,6,7]
# counter of actions
p = 0
d = 0
g = 0
h = 0
# reward/score
score = 1
tmp = 1
j = 30
f = 0
while True:	



	def randos(c):
		
		c = random.randint(0,10)
		return c


	keys = [('KeyEvent','ArrowRight',True),('KeyEvent','ArrowRight',False),('KeyEvent','ArrowUp',True),('KeyEvent','ArrowUp',False),('KeyEvent','lctrl',True),('KeyEvent','lctrl',False),('KeyEvent','ArrowLeft',True),('KeyEvent','ArrowLeft',False)]
	
	def count(p):
		
		p += 1
		return p

	def train(score,tmp):
		
		if count(p) > j:
			tmp += count(p) + score
			j = 0

 
		else:
			score += tmp		
			j = 30		
		return score,tmp

	
	def keyo(f):
		
		if f in z:
			f = random.randint(0,7)	

		return f	
		
		
	for i in xrange(count(p)):	
		action_n = [[keys[keyo(f)]] for ob in observation_n]
        	observation_n, reward_n, done_n, info = env.step(action_n)
		if  info['n'][0]['stats.reward.count'] > d:
			d += 1
			z.append(keyo(f))
				
	'''if randos(c) > 9:		
		if z.count(0) > z.count(4):
			z.append(4)
			z.append(4)
			z.append(1)
			z.append(1)
			z.append(2)
			z.append(2)
			z.append(3)
			
			
		if z.count(0) < z.count(4):
			z.append(0)
			z.append(0)
			z.append(5)
			z.append(5)	
			z.append(2)
			z.append(2)
			z.append(3)'''

	x = 300
        y = 330
        action_n = [universe.spaces.PointerEvent(x, y, 0),
            universe.spaces.PointerEvent(x, y, 1),
            universe.spaces.PointerEvent(x, y, 0)]
        action_n = [action_n for ob in observation_n]
        observation_n, reward_n, done_n, info = env.step(action_n)



	env.render()
	
	

