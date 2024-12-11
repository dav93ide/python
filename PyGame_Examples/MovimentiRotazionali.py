import pygame
from pygame.locals import *
from sys import exit
from Vettore import Vector2
from math import *


background_image_filename = "img_1.jpg"
sprite_image_filename = "img_4.png"

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()


sprite_pos = Vector2(200,150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.		# Gradi al secondo


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	pressed_keys = pygame.key.get_pressed()
	rotation_direction = 0
	movement_direction = 0
	
	if pressed_keys[K_LEFT]:
		rotation_direction = +1.0
	elif pressed_keys[K_RIGHT]:
		rotation_direction = -1.0
		
	if pressed_keys[K_UP]:
		movement_direction = +1.0
	elif pressed_keys[K_DOWN]:
		movement_direction = -1.0
		
	screen.blit(background,(0,0))
	
	rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
	w, h =rotated_sprite.get_size()
	sprite_draw_pos = Vector2(sprite_pos.x-w/2,sprite_pos.y-h/2)
	screen.blit(rotated_sprite, (sprite_draw_pos.x,sprite_draw_pos.y))
	
	time_passed = clock.tick(30)
	time_passed_seconds = time_passed / 1000.0
	
	sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
	
	heading_x = sin(sprite_rotation*pi/180.0)
	heading_y = cos(sprite_rotation*pi/180.0)
	heading = Vector2(heading_x,heading_y)
	heading *= movement_direction
	
	sprite_pos += heading * sprite_speed * time_passed_seconds
	
	if sprite_pos.x >= 640:
		sprite_pos.x = 0
	elif sprite_pos.x <= 0:
		sprite_pos.x = 640
	
	if sprite_pos.y >= 480:
		sprite_pos.y = 0
	elif sprite_pos.y <= 0:
		sprite_pos.y = 480
	
	
	pygame.display.update()