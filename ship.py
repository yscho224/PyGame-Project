import pygame

class Ship:
    #class to manage the ship
    def __init__(self, ai_game):
        #initialize the ship and set its starting position
        # ai_game gives ship access to alien invasion object
        self.screen = ai_game.screen#self.screen = object called surface
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # treat like rectangle
        #Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        #update the ship's position based on the movement flag
        #update the ship's x values, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x.
        self.rect.x = self.x 
    def blitme(self):
        # Draw the ship at its current location
        # blitme () does draws the image to the screen specified to self.rect
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship on the screen.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)