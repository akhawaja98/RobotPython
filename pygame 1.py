import sys, pygame
from pygame.locals import *


pygame.init()
pygame.background_colour = (255,255,255)
pygame.screen.fill(background_colour)
display = pygame.display.set_mode((600,600))

pygame.display.set_caption("Screen 1")

while True:

    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    
