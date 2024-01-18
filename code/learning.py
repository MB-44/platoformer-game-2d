import pygame, sys, os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(1,11):
            file_path = os.path.join(os.path.dirname(__file__), '..','assets','frog',f'attack_{i}.png')
            self.sprites.append(pygame.image.load(file_path))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect =  self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    # def stop_animation(self):
    #     self.is_animating = False

    # updating the image like changing the image
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

# general setup
pygame.init()
clock = pygame.time.Clock()

# game screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Learning")

# creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            player.animate()

    # drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)