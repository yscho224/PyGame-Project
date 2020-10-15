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

        self.ship_limit = 3
        #Bullet Settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60) #gray
        self.bullets_allowed = 3

        #Alien settings
        
        self.fleet_drop_speed = 10
        #How quickly the game speeds up
        self.speedup_scale = 1.1 #increases the game speed by each levels
        #How quickly the alien point values increases 
        self.score_scale = 1.5
        #initiliaze the values for attributes that need to change throughout the game 
        self.initialize_dynamic_settings()
    #setting up initial values for ship bullet alien speeds
    def initialize_dynamic_settings(self):
        '''initialize settings that change throughout the game'''
        self.ship_speed = 1.5 #1.5 pixels rather than 1 pixel
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        #scoring
        self.alien_points = 50
        # fleet_direction of 1 represents right; -1 represents left.
        # using numbers 1, -1 better b/c makes sense that it addes/subtracts to each alien's x coordinate value
        self.fleet_direction = 1
    def increase_speed(self):
        '''increase speed settings and alien point values'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)