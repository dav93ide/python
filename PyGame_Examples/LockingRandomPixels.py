''' Riempie un display di pixels con colori casuali effettuando il lock ogni qualvolta si disegna sulla superficie e l'unlock quando la si rilascia. In questo modo Pygame non deve effettuare il lock e l'unlock automaticamente ogni qualvolta viene richiamato il metodo "set_at" pertanto vi � un'esecuzione pi� veloce. '''

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	rand_col = (randint(0,255),randint(0,255),randint(0,255))
	screen.lock()
	for _ in range (100):
		rand_pos = (randint(0,639), randint(0,479))
		screen.set_at(rand_pos, rand_col)
	screen.unlock()
	pygame.display.update()