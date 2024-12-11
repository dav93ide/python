''' Genera casualmente delle linee ed ogni 100 cambia colore di sfondo xD '''

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time

pygame.init()
screen = pygame.display.set_mode((640,480), 0, 32)

px = None
numLine = 0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	rand_col = (randint(0, 255), randint(0,255), randint(0,255))
	rand_col2 = (randint(0, 255), randint(0,255), randint(0,255))
	x = randint(0,639)
	y = randint(0,479)
	rand_pos = (x,y)
	screen.set_at(rand_pos, (255,255,255))
	if px != None:
		pygame.draw.line(screen, rand_col2, (x,y), (px,py))
		numLine +=1
	px = x
	py = y
	
	time.sleep(0.02)
	if numLine == 100:
		screen.fill((rand_col))
		numLine = 0
	pygame.display.update()