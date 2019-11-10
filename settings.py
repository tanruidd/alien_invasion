class Settings():
    """ save setting's all class """

    def __init__(self):
        """ init settings"""
        # setting screnn
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 0.2

        #bullet settings
        self.bullet_speed_factor = 0.1
        self.bullet_width = 2
        self.bullet_height = 6
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
