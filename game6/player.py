import pygame
from game_parameters import *
# Create class for player

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # TODO Flip fish if going other way
        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png")
        self.reversed_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_up(self):
        self.y_velocity = -1*PLAYER_SPEED

    def move_down(self):
        self.y_velocity = PLAYER_SPEED

    def move_left(self):
        self.x_velocity = -1*PLAYER_SPEED
        self.image = self.reversed_image
    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self):
        # TODO Make sure the orange fish stays on the screen
        if self.x > SCREEN_WIDTH-TILE_SIZE:
            self.x = SCREEN_WIDTH-TILE_SIZE
        if self.x < 0:
            self.x = 0
        if self.y > SCREEN_HEIGHT-(2*TILE_SIZE):
            self.y = SCREEN_HEIGHT-(2*TILE_SIZE)
        if self.y < 0:
            self.y = 0
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)