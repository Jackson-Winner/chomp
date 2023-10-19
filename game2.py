import pygame
import sys
import random
# Initialize PYGAME
pygame.init()

# Screen Dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# Create Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FISHY!")

# Load our game font
custom_font = pygame.font.Font("assets/fonts/From Cartoon Blocks.ttf", 48)

# Define Function to Draw the Background
def draw_background(surf):
    # Load Our Files
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

    # Use PNG transparency
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # Fill the Screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    # Draw Sand
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))

    for _ in range(7):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x,screen_height-tile_size*2))

    # Draw the text
    text = custom_font.render("CHOMP", True, (255, 0, 0))
    surf.blit(text,(screen_width/2-text.get_width()/2, screen_height/20-text.get_height()/2))

def draw_fishes(surf):
    # Load some fish tiles from sprites
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    green_fish.set_colorkey((0, 0, 0))
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png").convert()
    puffer_fish.set_colorkey((0, 0, 0))

    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(tile_size, screen_height-(2*tile_size))
        if random.randint(0,1) == 0:
            green_fish = pygame.transform.flip(green_fish, True, False)
        surf.blit(green_fish, (x, y))

    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(tile_size, screen_height-(2*tile_size))
        if random.randint(0,1) == 0:
            puffer_fish = pygame.transform.flip(puffer_fish, True, False)
        surf.blit(puffer_fish, (x, y))

# Main Loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Background
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit
pygame.QUIT()