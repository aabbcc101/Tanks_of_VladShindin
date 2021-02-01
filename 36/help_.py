import pygame.font
from settings import *

class Help():
    def __init__(self,game):
        x = 250
        y = 200
        color = BLACK
        #color_of_text = (0,0,0)
        msg = "'BACKSPACE' is NEW GAME"
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
        self.rect.y -= 125
        
        
        self._prep_msg(msg)
        msg2 = "'SPACE' is shoting"
        
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        
        self._prep_msg2(msg2)
        
        msg3 = "'R' is RESTART GAME"
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y -= 65
        
        #create message only one time
        self._prep_msg3(msg3)
        
        msg4 = "Moving is using arrows"
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += 65
        
        #create message only one time
        self._prep_msg4(msg4)
        
        msg5 = "'Q' is quit"
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += 125
        
        #create message only one time
        self._prep_msg5(msg5)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)#, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def _prep_msg2(self, msg2):
        self.msg_image2 = self.font.render(msg2, True, self.text_color)#, self.button_color)
        self.msg_image2_rect = self.msg_image2.get_rect()
        self.msg_image2_rect.center = self.rect.center
        
    def _prep_msg3(self, msg3):
        self.msg_image3 = self.font.render(msg3, True, self.text_color)#, self.button_color)
        self.msg_image3_rect = self.msg_image3.get_rect()
        self.msg_image3_rect.center = self.rect.center
        
    def _prep_msg4(self, msg4):
        self.msg_image4 = self.font.render(msg4, True, self.text_color)#, self.button_color)
        self.msg_image4_rect = self.msg_image4.get_rect()
        self.msg_image4_rect.center = self.rect.center
        
    def _prep_msg5(self, msg5):
        self.msg_image5 = self.font.render(msg5, True, self.text_color)#, self.button_color)
        self.msg_image5_rect = self.msg_image5.get_rect()
        self.msg_image5_rect.center = self.rect.center
        
    def draw_title(self):
        self.screen.fill(BLACK)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)
        self.screen.blit(self.msg_image3, self.msg_image3_rect)
        self.screen.blit(self.msg_image4, self.msg_image4_rect)
        self.screen.blit(self.msg_image5, self.msg_image5_rect)

        
        
        
