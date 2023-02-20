import pygame.font
from settings import *

class Score():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.text_color = (150,30,30)
        self.font =pygame.font.SysFont(None,48)
        
        self.prepare(game)
        
    def prepare(self, game):
        # turn into an msg_image
        self.score = game.score
        live_str =' Wrecked enemies: ' + str(self.score) + " "
        self.live_image = self.font.render(live_str, True,
            self.text_color, (230, 230, 230))
        
        #show in the right top angle
        self.live_rect = self.live_image.get_rect()
        self.live_rect.left = self.screen_rect.left + 20
        self.live_rect.top = self.screen_rect.top + 7
    
    def draw(self):
        self.screen.blit(self.live_image, self.live_rect)
