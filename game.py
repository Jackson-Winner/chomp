import pygame
import sys

# Initialize PYGAME
pygame.init()

# Screen Dimensions
screen_width = 800
screen_height = 600

# Define Colors
BLUE = (0, 0, 255)
BROWN = (224, 161, 52)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CHOMP CHOMP!")

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False

    screen.fill(BLUE)

    # Draw BROWN Rectangle
    rectangle_height = 200
    pygame.draw.rect(screen, BROWN, (0, screen_height-rectangle_height, screen_width, rectangle_height))

    # Update the display
    pygame.display.flip()
