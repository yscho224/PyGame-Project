import sys # module that provides all the info/functions 
           # related to the python interpreter
from time import sleep #import sleep() to pause the game for a moment when the ship is hit
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship # (calling class Ship from ship.py)
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

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
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #Create an instance to store game statistics.
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # giving argument of an instance of Alien invasion to Ship()
        # assigning Ship instance to self.ship
        self.ship = Ship(self) 
        # assigning 'Group bullet' instance to self.bullet
        self.bullets = pygame.sprite.Group()
        # assigning 'Alien instance group to self.aliens
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        #Make the play button
        self.play_button = Button(self, "Play")
    
    # refactoring makes it easier to add new rows and create an entier fleet
    def _create_fleet(self): #create a group to hold the fleet of aliens
        '''create the fleet of aliens.'''
        #make an alien.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            #create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        #create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self): #check whether any aliens are at the left or right edge
        '''Respond appropriately if any aliens have reached an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break #break out the loop
    
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed #origin is top left corner so y-coordinate increases when goes down
        self.settings.fleet_direction *= -1 #move left


    def run_game(self):
        '''Start the main loop for the game.'''
        '''event - what user performs such as pressing a key or moving mouse'''
        '''to make program respond to events'''
        while True:
            # separating run_game() for better managing separated events
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update() #updates the ship moving right/left passed through the loop
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            

                   
    def _check_events(self):        
        for event in pygame.event.get(): #event loop
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #KEYDOWN = pressing the key
                self._check_keydown_events(event)
                 
            elif event.type == pygame.KEYUP: #KEYUP = releasing the key
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() #returns a tuple containing the mouse cursor's x and y coordinates
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        '''start a new game when the player clicks play'''
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.stats.game_active = True
            #get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
        #set the game to start only when game_active is False.
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            pygame.mouse.set_visible(False)
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right.
            #moves the image(rectangle) on the screen
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
        #add() written specifically for Pygame groups == append()
            self.bullets.add(new_bullet)
    
    #update method
    def _update_bullets(self): #to keep the AlienInvasion class reasonably well organized
        '''update position of bullets and get rid of old bullets'''
        # update bullet positions         
        self.bullets.update()

         #Get rid of bullets that have disappeared.
         #B/C we can't remove items from a list or group
         #within a for loop, make a copy()!!
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #Check for any bullets that have hit aliens
        #If so, get rid of the bullet and the alien.
        #Compares the positions of all the bullets and aliens
        #and identify any that overlap. 
        # **groupcollide() adds a key-value pair to the dictionary it returns
        collisions = pygame.sprite.groupcollide(
                    self.bullets, self.aliens, True, True)# two true arguments tell to delete the bullets and aliens that have collided.
        #Repopulating the Fleet
        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    
    def _update_aliens(self):
        '''Update the positions of all aliens in the fleet'''
        self._check_fleet_edges()
        self.aliens.update() #update on aliens group
        
        #look for alien-ship collisions.
        #spritecollideany() look for collision
        #if there aren't any, if statement won't execute
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!") #didn't replace it
            self._ship_hit()
        
        self._check_aliens_bottom()
        
    def _ship_hit(self):
        '''Respond to the ship being hit by an alien'''
        #Decrement ships_left.
        if self.stats.ships_left > 0: 
            self.stats.ships_left -= 1
            #Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship() 
            #Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        '''check if any aliens have reached the bottom of the screen.'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break



    def _update_screen(self):              
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) #Pygame draws each element in the group at the position defined by rect attribute.
        #Make the most recently drawn screen visible
        #Draw the score information.
        self.sb.show_score() 
        #Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip() #flip() continually updates the display to show the new positions of game elements
                                # and hide the old ones. 
                                # make the most recently drawn screen visible.
if __name__ == '__main__':
    #make a game instance, and run the game
    #only runs if the file is called directly
    ai = AlienInvasion()
    ai.run_game()








