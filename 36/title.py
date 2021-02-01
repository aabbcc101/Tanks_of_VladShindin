import pygame.font
from settings import *

class Title():
    def __init__(self,game):
        x = 250
        y = 200
        color = BLACK
        #color_of_text = (0,0,0)
        msg = "TANKS"
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        #sizes
        self.wight, self.height = x,y #200,50
        self.button_color = color   #(0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y -= 65
        
        
        self._prep_msg(msg)
        
        msg2 = "Developed by Vlad Shindin"
        
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        
        #create message only one time
        self._prep_msg2(msg2)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)#, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def _prep_msg2(self, msg2):
        self.msg_image2 = self.font.render(msg2, True, self.text_color)#, self.button_color)
        self.msg_image2_rect = self.msg_image2.get_rect()
        self.msg_image2_rect.center = self.rect.center
        
    def draw_title(self):
        self.screen.fill(BLACK)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)

        
        
        
