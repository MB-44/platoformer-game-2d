import pygame, os, sys
from levels import Level
from settings import *

# Game setup
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(LEVEL_MAP, display)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display.fill(DARK_BLUE)
    level.run()
    pygame.display.update()
    clock.tick(FPS)