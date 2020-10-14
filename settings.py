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
        
        #Ship Settings
        self.ship_speed = 1.5 #1.5 pixels rather than 1 pixel

        #Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60) #gray
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        # using numbers 1, -1 better b/c makes sense that it addes/subtracts to each alien's x coordinate value
        self.fleet_direction = 1