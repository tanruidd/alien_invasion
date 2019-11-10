import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """init and setting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading ship
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Place the ship in the center of the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float
        self.center = float(self.rect.centerx)

        #moving tag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ adjust the position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw"""
        self.screen.blit(self.image, self.rect)
