import pygame
from pygame.locals import *
from sys import exit
from Vettore import Vector2
import time
import random

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
font = pygame.font.SysFont("arial",10)


A = (100.0, 150.0)
B = (600.0, 435.0)
C = (150.0, 200.0)
D = (400.0, 500.0)
AB = Vector2.from_points(A,B)
CD = Vector2.from_points(C,D)
step = AB * .01
step2 = CD * .01
position = Vector2(A[0],A[1])
position2 = Vector2(C[0],C[1])
color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
start = A
start2 = C
text_surface2 =  font.render("|A = %s || B = %s ||| C = %s || D = %s|" % (A,B,C,D),True, (0,0,0))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	if position.x >= B[0] or position.y >= B [1]:
		temp = color1
		color1 = color2
		color2 = temp
		position = Vector2(B[0],B[1])
		step = -step
		step2 = -step2
		start = B
		start2 = D
	elif position.x < A[0] or position.y < A[1]:
		color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		A = (random.randint(0,540),random.randint(0,400))
		B = (random.randint(0,600),random.randint(0,480))
		C = (random.randint(0,540),random.randint(0,450))
		D = (random.randint(0,540),random.randint(0,450))
		while (A[0] > B[0] or A[1] > B[1]):
			B = (random.randint(0,640),random.randint(0,480))
		while (C[0] > D[0] or C[1] > D[1]):
			D = (random.randint(0,640),random.randint(0,480))
		AB = Vector2.from_points(A,B)
		CD = Vector2.from_points(C,D)
		text_surface2 =  font.render("|A = %s || B = %s ||| C = %s || D = %s|" % (A,B,C,D),True, (0,0,0))
		position = Vector2(A[0],A[1])
		position2 = Vector2(C[0],C[1])
		step = AB * .01
		step2 = CD * .01
		start = A 		
		start2 = C
			
		
	screen.fill((255,255,255))
	text_surfaceAB = font.render("%s" % position, True, (0,0,0))
	text_surfaceCD = font.render("%s" % position2, True, (0,0,0))
	position += step
	position2 += step2
	pygame.draw.line(screen,color1, start, (position.x,position.y), 5)
	pygame.draw.circle(screen, color1, (int(position.x),int(position.y)), 5)
	pygame.draw.line(screen,color2, start2, (position2.x,position2.y), 5)
	pygame.draw.circle(screen, color2, (int(position2.x),int(position2.y)), 5)
	
	time.sleep(0.02)
	screen.blit(text_surfaceAB,(position.x,position.y))
	screen.blit(text_surfaceCD,(position2.x,position2.y))
	screen.blit(text_surface2,(10,10))
	pygame.display.update()