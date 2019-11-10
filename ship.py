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
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)

        #moving tag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ adjust the position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y

    def blitme(self):
        """Draw"""
        self.screen.blit(self.image, self.rect)
