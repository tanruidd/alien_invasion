import sys

import pygame

def run_game():
    # init
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Alien Invasion")
    
    # set backgroud color
    bg_color = (230, 230, 230)

    # start
    while True:

        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        # view
        pygame.display.flip()

run_game()
