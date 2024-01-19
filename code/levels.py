import pygame
from tiles import Tile
from player import Player
from settings import *


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 10
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                X = col_index * TILE_SIZE
                Y = row_index * TILE_SIZE

                if col == "X":
                    tile = Tile((X,Y), TILE_SIZE)
                    self.tiles.add(tile)
                elif col == "P":
                    player = Player((X, Y))
                    self.tiles.add(player)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)