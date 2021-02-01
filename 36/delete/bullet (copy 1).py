import pygame
from pygame.sprite import Sprite 
from settings import *
#from map import world_map
from map import World_map

class Bullet(Sprite):
    def  __init__(self, game, direction, level):
        super().__init__()
        self.a_map = World_map()
        if level == 2:
            self.a_map.level_2_world_map()

        elif level == 3:
            self.a_map.level_3_world_map()
        
        elif level == 4:
            self.a_map.level_4_world_map()
            
        elif level == 5:
            self.a_map.level_5_world_map()
        
        
        self.screen = game.screen
        self.color = BULLET_COLOR
        if direction == 'up': 
            self.rect = pygame.Rect(0,0,BULLET_WIGHT, BULLET_HEIGHT)
            self.rect.midtop = game.myTank.rect.midtop
        elif direction == 'down': 
            self.rect = pygame.Rect(0,0,BULLET_WIGHT, BULLET_HEIGHT)
            self.rect.midbottom = game.myTank.rect.midbottom
        elif direction == 'left': 
            self.rect = pygame.Rect(0,0,BULLET_HEIGHT,BULLET_WIGHT)
            self.rect.midleft = game.myTank.rect.midleft
        elif direction == 'right': 
            self.rect = pygame.Rect(0,0,BULLET_HEIGHT,BULLET_WIGHT)
            self.rect.midright = game.myTank.rect.midright
        
        self.direction = direction
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
       
    def check_top_wall(self):
        self.rightTopX = self.rect.x + BULLET_WIGHT
        self.lefttBottomY = self.rect.y + BULLET_HEIGHT
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.rect.y-BULLET_SPEED >= y):
                return True
            elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.rect.y-BULLET_SPEED >= y):
                return True
        return False
            
    def check_left_wall(self):
        self.rightTopX = self.rect.x + BULLET_HEIGHT
        self.lefttBottomY = self.rect.y + BULLET_WIGHT
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rect.x-BULLET_SPEED >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rect.x-BULLET_SPEED >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
        return False
    
    def check_right_wall(self):
        self.rightTopX = self.rect.x + BULLET_HEIGHT
        self.lefttBottomY = self.rect.y + BULLET_WIGHT
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rightTopX+BULLET_SPEED >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rightTopX+BULLET_SPEED >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
        return False
    
    def check_bottom_wall(self):
        self.rightTopX = self.rect.x + BULLET_WIGHT
        self.lefttBottomY = self.rect.y + BULLET_HEIGHT
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.lefttBottomY+BULLET_SPEED >= y):
                return True
            elif (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.lefttBottomY+BULLET_SPEED >= y):
                return True
        return False
   
        return False    
    def update(self):
        if self.direction == 'up':
            if self.check_top_wall() == False:
                self.y -= BULLET_SPEED
                self.rect.y = self.y
            else:
                return True 
        elif self.direction == 'down':
            if self.check_bottom_wall() == False:       
                self.y += BULLET_SPEED
                self.rect.y = self.y
            else:
                return True 
        elif self.direction == 'left':
            if self.check_left_wall() == False:
                self.x -= BULLET_SPEED
                self.rect.x = self.x
            else:
                return True 
        elif self.direction == 'right':
            if self.check_right_wall() == False:
                self.x += BULLET_SPEED
                self.rect.x = self.x
            else:
                return True 
        return False
        
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
