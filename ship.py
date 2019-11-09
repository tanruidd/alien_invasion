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

        #moving tag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ adjust the position of the ship"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw"""
        self.screen.blit(self.image, self.rect)
