from settings import *

class Stats():
    def __init__(self,game):
        self.settings = game.settings
        self.reset_stats()
        
        self.game_active = False
        
    def reset_stats(self):
        self.live = 3
