import random
import pygame
import sys

from background import draw_background
from game_parameters import *

# Initialize PYGAME
pygame.init()

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FUN STUFF!")

# Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed UP")
            if event.key == pygame.K_DOWN:
                print("You pressed DOWN")
            if event.key == pygame.K_LEFT:
                print("You pressed LEFT")
            if event.key == pygame.K_RIGHT:
                print("You pressed RIGHT")


    # Draw Background
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

    # Limit Frame rate
    #clock.tick(60)
# Quit
pygame.QUIT()