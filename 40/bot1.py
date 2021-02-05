import pygame
from settings import*
from pygame.sprite import Sprite 

class Bot1(Sprite):
    def __init__(self,game):
        Sprite.__init__(self)
     
        self.direction_list = ['up','down', 'right', 'left']
    
        self.screen = game.screen

        self.imageLeft = pygame.image.load('images/bender5_3.png')
        self.imageRight = pygame.image.load('images/bender5_3.png')
    
        self.rect =self.imageRight.get_rect()
        
        self.rect.x += 0
        self.rect.y += 0
        self.size_x = 40
        self.size_y = 80
        self.x_on_a_map = 0
        self.y_on_a_map = 0
        
        self.real_x =  self.rect.x
        self.real_y = self.rect.y
        
        self.direction = 'right'
        self.live = True
        
    def bore(self):
        #if self.jump_up == False and self.jump_activate == 0:
        if self.direction == 'right':
            self.direction = 'left'
        elif self.direction =='left':
            self.direction = 'right'
        
    def blitme(self, new_rect):
        
        #self.rect.x = self.real_x
        #self.rect.y = self.real_y
        if self.direction == 'right':
            #if self.step_direction == 'left':
            self.screen.blit(self.imageRight, new_rect)
                    #elif self.direction == 'left':
        elif self.direction == 'left':
            self.screen.blit(self.imageLeft, new_rect)
            #elif self.step_direction == 'right':
                #self.screen.blit(self.imageLeft1, self.rect)
