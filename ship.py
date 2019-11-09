import pygame

class Ship():

    def __init__(self, screen):
        """init and setting position"""
        self.screen = screen

        # Loading ship
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Place the ship in the center of the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw"""
        self.screen.blit(self.image, self.rect)
