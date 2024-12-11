''' Crea un testo utilizzando un oggetto font e lo salva come immagine '''

import pygame

text = "Prova Font"
pygame.init()
my_font = pygame.font.SysFont("arial",64)
text_surface = my_font.render( text, True, (0,0,0), (255,255,255))
pygame.image.save(text_surface, "name.png")