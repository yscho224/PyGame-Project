# each time new functionality is introduced,
#allows to work with just one settings object any time we need
#to access an individual setting.

class Settings:
    #stores all settings for Alien Invasion
    def __init__(self):
        #initialize the game's settings
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #ship settings
        self.ship_speed = 1.5