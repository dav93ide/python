''' Mostra graficamente l'andamento della funzione "randint()" ''' 

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time
import os

x=0
visual = False
px = None
Full_Screen = False
Start = False
listY = []

def rePrint():
	px = None
	for n in range(0,x,2):
		y = listY[n/2 + n%2]
		if px != None:
			pygame.draw.line(screen, col, (n,y), (px,py))
		px = n
		py = y



if __name__ == '__main__':

	os.system("cls")
	print \
	"/-------------------------------------------------------------------------------\\\n" \
	"\t\t\t\t[> Random Function <]\n" \
	"\\------------------------------------------------------------------------------/\n\n\n" \
	"/-------------------------------------------------------------------------------\\\n" \
	"+] Banalissimo Script Che Stampa A Video L'Andamento Della Funzione \"RandomInt\"\n Randomizzando I Valori Sull'Asse Y\n\n" \
	"+] Funzionamento:\n"\
	"\t- Premere 'A' per avviare\n"\
	"\t- Premere 'Q' per interrompere\n" \
	"\t- Premere 'F' per entrare e/o uscire da schermo intero\n" \
	"\t- Premere 'R' per riavviare\n" \
	"\t- Premere 'V' per visualizzare i valori sul grafico\n" \
	"\\------------------------------------------------------------------------------/\n\n\n" \
	"\t\t\t\t--[ Enjoy! ]--\n\n\n" \
	"[+] Premi Invio Per Inizializzare La Schermata (: "

	raw_input()
	txt = True
	pygame.init()
	screen = pygame.display.set_mode((1024,768), 0, 32)
	col = (255,0,255)
	font = pygame.font.SysFont("arial",45)
	text = font.render("Let's Rock!",True,(255,255,255))
	screen.blit(text, ( 500,330))
	font = pygame.font.SysFont("Times New Roman", 15)
	text = font.render("Press A",True,(255,255,255))
	screen.blit(text, ( 540,383))
				
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_f:
					Full_Screen = not Full_Screen
					if Full_Screen == True:
						screen = pygame.display.set_mode((1024,768), 0, 32)
					else:	
						screen = pygame.display.set_mode((1024,768), FULLSCREEN, 32)
					screen.fill((0,0,0))
					rePrint()
					pygame.display.update()
				elif event.key == K_q:
					exit()
				elif event.key == K_a:
					if txt == True:
						screen.fill((0,0,0))
						font = pygame.font.SysFont("arial",10)
						txt = False
					Start = not Start
				elif event.key == K_r:
					screen.fill((0,0,0))
					x = 0
					px = 0
					listY= []
				elif event.key == K_v:
					screen.fill((0,0,0))
					rePrint()
					visual = not visual
					if visual == True:
						for n in range(0,x,2):
							ny = listY[n/2 + n%2]
							text = font.render(str(ny),True,(255,255,255))
							screen.blit(text, ( n + text.get_width(),ny ))
					pygame.display.update()
					
		if Start and x<=1024:
			x += 2
			y = randint(0,767)
			listY.append(y)
			rand_pos = (x,y)
			screen.set_at(rand_pos, (255,255,255))
			if px != None:
				pygame.draw.line(screen, col, (x,y), (px,py))
			px = x
			py = y
			print y
			time.sleep(0.05)
		if visual == True:
			text = font.render(str(y),True,(255,255,255))
			screen.blit(text, ( x + text.get_width(),y ))
		pygame.display.update()