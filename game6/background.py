import pygame
import random
from game_parameters import *
def draw_background(surf):
    # Load Our Files
    water = pygame.image.load('../assets/sprites/water.png').convert()
    sand = pygame.image.load('../assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('../assets/sprites/seagrass.png').convert()

    # Use PNG transparency
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # Fill the Screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(water, (x,y))

    # Draw Sand
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand, (x, SCREEN_HEIGHT-TILE_SIZE))

    for _ in range(7):
        x = random.randint(0, SCREEN_WIDTH)
        surf.blit(seagrass, (x,SCREEN_HEIGHT-TILE_SIZE*2))

    # Draw the text
    custom_font = pygame.font.Font("../assets/fonts/From Cartoon Blocks.ttf", 48)
    text = custom_font.render("CHOMP", True, (255, 0, 0))
    surf.blit(text,(SCREEN_WIDTH/2-text.get_width()/2, SCREEN_HEIGHT/20-text.get_height()/2))