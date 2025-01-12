''' Identifica i tasti premuti da tastiera utilizzando la lista delle chiavi premute fornita da pygame.key.get_pressed() '''

import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

font = pygame.font.SysFont("arial",32)
font_height = font.get_linesize()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	
	screen.fill((255,255,255))
	
	pressed_key_text = []
	pressed_keys = pygame.key.get_pressed()
	y = font_height
	
	
	for key_costant, pressed in enumerate(pressed_keys):
		if pressed:	
			key_name = pygame.key.name(key_costant)
			text_surface = font.render(key_name+ " pressed ", True, (0,0,0))
			screen.blit(text_surface, (8,y))
			y += font_height
			
	pygame.display.update()