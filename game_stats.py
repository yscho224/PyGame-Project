class GameStats:
    '''Track statistics for Alien invasion.'''

    def __init__(self, ai_game):
        '''initialize statistics'''
        self.settings = ai_game.settings
        self.reset_stats()
    #when players start a new game
    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
    #start Alien invasion in an active state.
    # game_active flag
        self.game_active = True

    #Start game in an inactive state
        self.game_active = False








