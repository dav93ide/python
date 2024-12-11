''' Ridimensionamento della finestra '''
import pygame
from pygame.locals import *
from sys import exit

# Inizializza la finestra
background_image_filename = 'img_1.jpg'
pygame.init()
SCREEN_SIZE = (640,680)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()

while True:
	# Attende un evento
	event = pygame.event.wait()
	if event.type == QUIT:
		exit()
	# Se l'evento e' un ridimensionamento del display
	if event.type == VIDEORESIZE:
		# Prende la nuova dimensione e cambia la dimensione del display alla nuova dimensione poi stampa un messaggio a video
		SCREEN_SIZE = event.size
		screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
		pygame.display.set_caption("Window resized to " + str(event.size))
	
	# Recupera altezza-larghezza
	screen_width, screen_height = SCREEN_SIZE
	# Ripete l'immagine dello sfondo tante volte quante necessarie per coprire la nuova dimensione
	for y in range(0,screen_height,background.get_height()):	
		for x in range(0,screen_width,background.get_width()):
			screen.blit(background, (x,y))
			
	pygame.display.update()