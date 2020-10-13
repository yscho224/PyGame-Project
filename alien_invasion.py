import sys # module that provides all the info/functions 
           # related to the python interpreter

import pygame
from settings import Settings
from ship import Ship # (calling class Ship from ship.py)


class AlienInvasion:
#overall class to manage game assets and behavior
    def __init__(self):
        '''Initialize the game, and create game resources.'''
        '''define attributes in an object'''
        '''self is instance of the class'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().screen_width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # giving argument of an instance of Alien invasion to Ship()
        # assigning Ship instance to self.ship
        self.ship = Ship(self) 
        #setting the display mode. tuples -> dimensions of the game window
    def run_game(self):
        '''Start the main loop for the game.'''
        '''event - what user performs such as pressing a key or moving mouse'''
        '''to make program respond to events'''
        while True:
            # separating run_game() for better managing separated events
            self._check_events()
            self.ship.update() #updates the ship moving right/left passed through the loop
            self._update_screen()
            #Watch for keyboard and mouse events.
    def _check_events(self):        
        for event in pygame.event.get(): #event loop
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #KEYDOWN = pressing the key
                self._check_keydown_events(event)
                 
            elif event.type == pygame.KEYUP: #KEYUP = releasing the key
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right.
            #moves the image(rectangle) on the screen
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                
    def _update_screen(self):              
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() 
        #Make the most recently drawn screen visible
        pygame.display.flip() #flip() continually updates the display to show the new positions of game elements
                                # and hide the old ones. 
                                # make the most recently drawn screen visible.
if __name__ == '__main__':
    #make a game instance, and run the game
    #only runs if the file is called directly
    ai = AlienInvasion()
    ai.run_game()








