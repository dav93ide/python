# Hello World Con PyGame - Non Visualizza L'Immagine Per Il Mouse

background_image_filename = 'img_1.jpg'
mouse_image_filename = 'img_4.png'

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
pygame.mouse.set_visible(False)
pygame.event.set_grab(False)

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	screen.blit(background,(0,0))
	
	x,y = pygame.mouse.get_pos()
	x -= mouse_cursor.get_width()/2
	y -= mouse_cursor.get_height()/2
	screen.blit(mouse_cursor,(x,y))
	
	pygame.display.update()