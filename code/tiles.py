from typing import Any
import pygame, os, sys
from settings import *
from maps import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size)) # x, y
        self.image.fill(GREY)
        self.rect = self.image.get_rect(topleft = position)
    
    def update(self, x_shift):
        self.rect.x += x_shift