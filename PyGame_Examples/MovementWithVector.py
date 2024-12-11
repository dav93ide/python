import pygame
from pygame.locals import *
from sys import exit
from Vettore import Vector2

background_image_filename = "img_1.jpg"
sprite_image_filename = "img_4.png"
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
clock = pygame.time.Clock()

position = Vector2(100.0,100.0)
speed = 250.
heading = Vector2()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			destination = Vector2(*event.pos) - Vector2(*sprite.get_size())/2
			heading = Vector2.from_points((position.x,position.y), (destination.x,destination.y))
			heading.normalize()
			if speed < 0:
				speed = -speed
	
	screen.blit(background, (0,0))
	screen.blit(sprite, (position.x,position.y))
	
	time_passed = clock.tick()
	time_passed_seconds = time_passed / 1000.0
	
	if position.x >= 620 or position.y >= 460:
		speed = -speed
	elif position.x <= 2 or position.y <= 2:
		speed = -speed
	distance_moved = time_passed_seconds * speed
	position += heading * distance_moved
	
	pygame.display.update()