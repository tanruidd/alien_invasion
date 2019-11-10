import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # init
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # set backgroud color
    bg_color = (230, 230, 230)

    # create a ship
    ship = Ship(ai_settings, screen)

    #storage bullets
    bullets = Group()

    # start
    while True:

        # event
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        
        #update bullets
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)

        # view
        pygame.display.flip()

run_game()
