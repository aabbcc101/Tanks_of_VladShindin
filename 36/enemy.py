import pygame
#from map import world_map
from settings import*
from ship import Ship
from pygame.sprite import Sprite 
#from map import World_map
import random
#import threading

class Enemy(Sprite, Ship):
    def __init__(self,game):
        Sprite.__init__(self)
        Ship.__init__(self,game)
        self.direction_list = ['up','down', 'right', 'left']
    
        self.rect.topleft = self.screen_rect.topleft
        self.rect.x += 104
        self.rect.y += 102
        
        self.image = pygame.image.load('images/battle32.png')
        self.imageLeft = pygame.image.load('images/battleLeft32.png')
        self.imageRight = pygame.image.load('images/battleRight32.png')
        self.imageDown = pygame.image.load('images/battleDown32.png')
        
        self.live = True
    
    def rand_direction(self):
        self.direction = random.choice(self.direction_list)
         
    #def get_direction(self):
        #if self.direction == 'down':
            #self.rand_direction()
        #elif self.direction == 'up':
            #self.rand_direction()
        #elif self.direction == 'right':
            #self.rand_direction()
        #elif self.direction == 'left':
            #self.rand_direction()
        
        
        # moving

    def update(self):
        #t = threading.Timer(1.0, self.get)
        #t.start()
        #self.direction = random.choice(self.direction_list)
        #t.stop()
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        if self.direction == 'up':
            self.moving_up = True
        elif self.direction == 'down':
            self.moving_down = True
        elif self.direction == 'right':
            self.moving_right = True
        elif self.direction == 'left':
            self.moving_left = True
            
        if self.moving_down and self.live:
            if self.check_bottom_wall() == False and self.check_coordinates_bottom() == False:
                self.rect.y += self.ship_speed 
                self.direction = 'down'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'down'
        elif self.moving_up and self.live:
            if self.check_top_wall() == False and self.check_coordinates_top() == False:
                self.rect.y -= self.ship_speed
                self.direction = 'up'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'up'
                
        elif self.moving_left and self.live:
            if self.check_left_wall() == False and self.check_coordinates_left() == False:
                self.rect.x -= self.ship_speed 
                self.direction = 'left'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'left'
        elif self.moving_right and self.live:
            if self.check_right_wall() == False and self.check_coordinates_right() == False:
                self.rect.x += self.ship_speed
                self.direction = 'right'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'right'
        pass
    
    def set_zero_coordinates(self):
        self.rect.topleft = self.screen_rect.topleft
        self.rect.x += 254
        self.rect.y += 250
        
    
