from SimpleCV import Image
import pyscreeze

import gym
import universe # register the universe environments
import random

reward = 0
score = 0

#k = [0,1]
env = gym.make('flashgames.HarvestDay-v0')
env.configure(remotes=1) # create one flashgames Docker container
observation_n = env.reset()
c = 0
x = 0
y = 0

e = 0
img = Image("continue.png")
img = img.binarize()

while True:
  # your agent generates action_n at 60 frames per second
	
			
	 
	x = random.randint(0,600)
	y = random.randint(100,400)
	e += 1
	if e >= 800:
		x = random.randint(0,600)
		y = random.randint(300,400)
	        
	action_n = [universe.spaces.PointerEvent(x, y, 0),
            universe.spaces.PointerEvent(x, y, 1),
            universe.spaces.PointerEvent(x, y, 0)]

	                	
        action_n = [action_n for ob in observation_n]
        observation_n, reward_n, done_n, info = env.step(action_n)

# doesn't work yet
	
	if e > 600:
		screen = Image(pyscreeze.screenshot())
        	screen = screen.binarize()
			
       	
		imga = str(img)
        
        	imgo = str([screen])
        	d = [s for s in imgo if imga in s]
        	if imga in s :
			x = 250
			y = 200
			e = 0
			action_n = [action_n for ob in observation_n]
	        	observation_n, reward_n, done_n, info = env.step(action_n)


			
        env.render()

