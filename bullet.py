import pygame
# sprite - can group related elements in your game and act
# on all the grouped elements at once. 
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship'''

    def __init__(self, ai_game):
        '''create a bullet object at the ship's current position'''
        super().__init__() #super() interit properly from sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        # set the bullet's midtop attribute to match the ship's midtop attribute
        self.rect.midtop = ai_game.ship.rect.midtop 
        
        # store the bullet's position as a decimal value
        # y because bullets move up and down. 
        self.y = float(self.rect.y) 
    def draw_bullet(self):
        '''draw the bullet to the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)







