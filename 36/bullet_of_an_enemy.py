import pygame
from pygame.sprite import Sprite 
from bullet import Bullet
from settings import *
from map import World_map

class Evil_bullet(Bullet):
    def __init__(self, game, enemy_x, enemy_y, direction,level):
        #Bullet.__init__(self, enemy, direction)
        Sprite.__init__(self)
        self.screen = game.screen
        self.color = BULLET_COLOR
        self.a_map = World_map()
        if level == 2:
            self.a_map.level_2_world_map()
        elif level == 3:
            self.a_map.level_3_world_map()
            
        elif level == 4:
            self.a_map.level_4_world_map()
            
        elif level == 5:
            self.a_map.level_5_world_map()
            
        
        if direction == 'up': 
            self.rect = pygame.Rect(0,0,BULLET_WIGHT, BULLET_HEIGHT)
            self.rect.x = enemy_x + 15
            self.rect.y = enemy_y
            #self.rect.midtop = game.myTank.rect.midtop
        elif direction == 'down': 
            self.rect = pygame.Rect(0,0,BULLET_WIGHT, BULLET_HEIGHT)
            self.rect.x = enemy_x + 15
            self.rect.y = enemy_y + 30
            #self.rect.midbottom = game.myTank.rect.midbottom
        elif direction == 'left': 
            self.rect = pygame.Rect(0,0,BULLET_HEIGHT,BULLET_WIGHT)
            #self.rect.midleft = game.myTank.rect.midleft
            self.rect.x = enemy_x 
            self.rect.y = enemy_y + 15
        elif direction == 'right': 
            self.rect = pygame.Rect(0,0,BULLET_HEIGHT,BULLET_WIGHT)
            #self.rect.midright = game.myTank.rect.midright
            self.rect.x = enemy_x + 30
            self.rect.y = enemy_y + 15
        
        self.direction = direction
        #self.rect.y = enemy_y + 16
        #self.rect.x = enemy_x + 16
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    
