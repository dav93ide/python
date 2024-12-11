import pygame


pygame.init()
my_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE, mod=0, unicode=u' ', message="Keydown")
pygame.event.post(my_event)
# Creazione nuovo evento
CATONKEYBOARD = pygame.USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad Cat!")
# Aggiunge l'evento alla fine della coda degli eventi
pygame.event.post(my_event)

for event in pygame.event.get():
	if event.type == CATONKEYBOARD:
		print event.message
	elif event.type == pygame.KEYDOWN:
			print event.message