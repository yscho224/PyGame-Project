class GameStats:
    '''Track statistics for Alien invasion.'''

    def __init__(self, ai_game):
        '''initialize statistics'''
        self.settings = ai_game.settings
        self.reset_status()
    #when players start a new game
    def reset_status(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit

    #start Alien invasion in an active state.
    self.game_active = True








