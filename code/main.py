import pygame, os, sys
from settings import *
from tiles import Tile

# game setup
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100,100),200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display.fill(DARK_BLUE)
    test_tile.draw(display)
    pygame.display.update()
    clock.tick(FPS)