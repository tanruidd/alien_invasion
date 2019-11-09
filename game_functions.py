import sys
import pygame

def check_events(ship):
    """respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship to the right
                ship.rect.centerx += 1

def update_screen(ai_setttings, screen, ship):
    """update image and switch"""
    #
    screen.fill(ai_setttings.bg_color)
    ship.blitme()
    
    # view
    pygame.display.flip()
