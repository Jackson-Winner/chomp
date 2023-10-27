import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player

# Initialize pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stuff and things!")

# Clock object
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# Draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5),random.randint(TILE_SIZE, SCREEN_HEIGHT-(2*TILE_SIZE))))

# Create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        # Control Fish
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()


    # Draw Background
    screen.blit(background, (0, 0))

    # Update fish location
    fishes.update()

    # Update the player
    player.update()

    # Check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH+50),random.randint(TILE_SIZE, SCREEN_HEIGHT - (2 * TILE_SIZE))))

    # Draw the fish
    fishes.draw(screen)

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit Frame rate
    clock.tick(60)
# Quit
pygame.QUIT()