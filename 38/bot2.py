import pygame
from settings import*
from pygame.sprite import Sprite 

class Bot2(Sprite):
    def __init__(self,game):
        Sprite.__init__(self)
        
        self.direction_list = ['up','down', 'right', 'left']
    
        self.screen = game.screen
        
        #self.image = pygame.image.load('images/bot1.png')
        self.imageLeft = pygame.image.load('images/bot1L.png')
        self.imageRight = pygame.image.load('images/bot1.png')
   
        self.rect =self.imageRight.get_rect()
        
        self.rect.x  = 0
        self.rect.y = 0
        
        self.direction = 'right'
        self.live = True
        
        
           
    def bore(self):
        #if self.jump_up == False and self.jump_activate == 0:
        if self.direction == 'right':
            self.direction = 'left'
        elif self.direction =='left':
            self.direction = 'right'
        
    def blitme(self):
        #if self.direction == 'up':
            #self.screen.blit(self.image, self.rect)
        #self.rect.x 
        if self.direction == 'right':
            #if self.step_direction == 'left':
            self.screen.blit(self.imageRight, self.rect)
                    #elif self.direction == 'left':
        elif self.direction == 'left':
            self.screen.blit(self.imageLeft, self.rect)
            #elif self.step_direction == 'right':
                #self.screen.blit(self.imageLeft1, self.rect)
