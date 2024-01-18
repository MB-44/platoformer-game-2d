import pygame
from tiles import Tile
from settings import *


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == "X":
                    tile = Tile((col_index * TILE_SIZE, row_index * TILE_SIZE),TILE_SIZE)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)