import pygame, os, sys
from settings import *

# game setup
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display.fill(DARK_BLUE)
    pygame.display.update()
    clock.tick(FPS)