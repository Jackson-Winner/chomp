import pygame
import sys
import random
from fish import Fish, fishes
# Initialize PYGAME
pygame.init()

# Screen Dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# Create Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FISHY!")

# Clock object
clock = pygame.time.Clock()
def draw_background(surf):
    # Load Our Files
    water = pygame.image.load('../assets/sprites/water.png').convert()
    sand = pygame.image.load('../assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('../assets/sprites/seagrass.png').convert()

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
    custom_font = pygame.font.Font("../assets/fonts/From Cartoon Blocks.ttf", 48)
    text = custom_font.render("CHOMP", True, (255, 0, 0))
    surf.blit(text,(screen_width/2-text.get_width()/2, screen_height/20-text.get_height()/2))

# Main Loop
running = True
background = screen.copy()
draw_background(background)
# Draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5),random.randint(tile_size, screen_height-(2*tile_size))))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Background
    screen.blit(background, (0, 0))

    # Update fish location
    fishes.update()

    # Check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width+50),random.randint(tile_size, screen_height - (2 * tile_size))))

    # Draw the fish
    fishes.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit Framerate
    clock.tick(60)
# Quit
pygame.QUIT()