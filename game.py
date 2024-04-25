import pygame
import sys
from player import Player
from config import *

# Initialize Pygame
pygame.init()

# Set up the display with potential hardware acceleration
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Pygame Game with Player and Bullets')

# Create a player instance
player = Player(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire_bullet()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move('left')
    if keys[pygame.K_d]:
        player.move('right')
    if keys[pygame.K_w]:
        player.jump()

    player.apply_gravity()

    screen.fill(BLACK)  # Clear the screen with black
    player.draw(screen)  # Draw the player
    player.update_bullets(screen)  # Update and draw bullets
    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
