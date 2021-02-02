import pygame
from pygame.sprite import Sprite 
from settings import *
import math

class Bullet(Sprite):
    def  __init__(self, game, direction):#, direction, level):
        super().__init__()
        #self.a_map = World_map()
        #if level == 2:
            #self.a_map.level_2_world_map()

        #elif level == 3:
            #self.a_map.level_3_world_map()
        
        #elif level == 4:
            #self.a_map.level_4_world_map()
            
        #elif level == 5:
            #self.a_map.level_5_world_map()
        
        
        self.screen = game.screen
        self.color = BULLET_COLOR
       
        self.rect = pygame.draw.circle(game.screen, RED, (0, 0), 6)
        
        if direction == 'right':
            self.rect.x = game.bender.rect.x
            self.rect.y = game.bender.rect.y
            self.rect.x += 80
            self.rect.y += 60
                     
            self.x_on_a_map = game.bender.real_x
            self.y_on_a_map  = game.bender.real_y
            self.x_on_a_map += 80  
            self.y_on_a_map += 60
         
        elif direction == 'left':
            self.rect.x = game.bender.rect.x
            self.rect.y = game.bender.rect.y
            self.rect.x -= 25
            self.rect.y += 60
            
            self.x_on_a_map = game.bender.real_x
            self.y_on_a_map  = game.bender.real_y
            self.x_on_a_map -= 25
            self.y_on_a_map += 60

        self.start_x = self.x_on_a_map
        self.start_y = self.y_on_a_map
        self.long_of_fire  = 400
        
        xx = game.mouse_pos_x 
        yy = game.mouse_pos_y
        line = (math.sqrt(xx**2 + yy**2))
        
        self.mouse_cos = xx/line
        self.mouse_sin = yy/line

        self.real_x = self.rect.x
        self.real_y = self.rect.y
        
        print(f'GGGGame.bender.real_x = {game.bender.real_x} game.bender.real_y = {game.bender.real_y} ')
        print(f'FIRST self.real_x = {self.real_x} self.rect.x = {self.rect.x} ')

        
    def need_to_delete(self):
                
        if  (math.sqrt((self.x_on_a_map - self.start_x)**2 + (self.y_on_a_map -self.start_y)**2) >= self.long_of_fire):
            print(f' long = {math.sqrt((- self.start_x + self.x_on_a_map)**2 + (- self.start_y + self.y_on_a_map)**2)}')
            return True
        else:
            return False

    def update(self):
        ##self.real_x = self.rect.x
        #self.real_y = self.rect.y
        #print(f' self.rect.x = {self.real_x} self.rect.y = {self.real_y}')
        self.x_on_a_map += (BULLET_SPEED + 2) * self.mouse_cos
        self.real_x += (BULLET_SPEED + 2) * self.mouse_cos
        self.y_on_a_map += (BULLET_SPEED + 2) * self.mouse_sin    
        self.real_y += (BULLET_SPEED + 2) * self.mouse_sin
        #print(f'x map = {self.x_on_a_map} y map = {self.y_on_a_map}')
        self.rect.x =  self.real_x
        self.rect.y =  self.real_y

          
        
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
