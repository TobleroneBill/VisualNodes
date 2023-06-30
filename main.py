import DataStruct
import visualise

import pygame
import sys

pygame.init()

width = 960
height = 540
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Template")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()



    screen.fill()

    pygame.display.flip()

