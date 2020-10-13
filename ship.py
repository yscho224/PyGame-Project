import pygame

class Ship:
    #class to manage the ship
    def __init__(self, ai_game):
        #initialize the ship and set its starting position
        # ai_game gives ship access to alien invastion object
        self.screen = ai_game.screen#self.screen = object called surface
        self.screen_rect = ai_game.screen.get_rect() # treat like rectangle
        #Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False
    def update(self):
        #update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.x += 1
    def blitme(self):
        # Draw the ship at its current location
        # blitme () does draws the image to the screen specified to self.rect
        self.screen.blit(self.image, self.rect)