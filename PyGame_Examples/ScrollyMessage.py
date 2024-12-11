import pygame
from pygame.locals import *
from sys import exit

# Inizializzazione variabili necessarie
background_image_filename = 'img_1.jpg'
SCREEN_SIZE = (640,480)
message = "    Script Messaggio A Scorrimento"

# Creazione del display, del font e della superficie di testo
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.SysFont("arial",80)
text_surface = font.render(message,True,(0,0,255))

# Set delle coordinate x,y per il testo (y = in mezzo)
x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2

# Caricamento dell'immagine a video
background = pygame.image.load(background_image_filename).convert()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	# Ricarica l'immagine di sfondo
	screen.blit(background,(0,0))
	
	# Varia valore di x per creare lo scorrimento ( il valore che viene decrementato influenza la velocita' di scorrimento )
	x -= 0.2
	if x < -text_surface.get_width():
		x = 0
	
	# riproduce il testo sullo schermo facendolo scorrere
	screen.blit(text_surface,(x,y))
	# a fine scorrimento fa riapparire il testo sulla destra invece che direttamente al centro
	screen.blit(text_surface, ( x + text_surface.get_width(),y ))
	pygame.display.update()