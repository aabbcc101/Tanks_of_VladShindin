import sys
import pygame
from settings import *
import time
from map import World_map
from robot import Robot
from bot1 import Bot1
from bot2 import Bot2
from guns import Guns
import math
from bullet import Bullet

class Game():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Future")
        
        self.clock = pygame.time.Clock()
        
        self.a_map = World_map()
        
        self.bender = Robot(self)
        self.angle = 0
        self.angle_minus = False
        self.angle_plus = False
        self.mouse_pos_x, self.mouse_pos_y = 0,0
        #self.mouse_sin = 0
        #self.mouse_cos = 0
        
        self.bullets = pygame.sprite.Group()
        self.bots1 = pygame.sprite.Group()
        
        
        bot1 = Bot1(self)
        bot1.rect.x =  904
        bot1.rect.y = 282
        bot1.real_x =  904
        bot1.real_y = 282
        bot1.x_on_a_map  = 904 
        bot1.y_on_a_map  = 282
        
        self.bots1.add(bot1)
        
        bot1 = Bot1(self)
        bot1.rect.x =  104
        bot1.rect.y = 292
        bot1.real_x =  104
        bot1.real_y = 292
        bot1.x_on_a_map  = 104 
        bot1.y_on_a_map  = 292
               
        self.bots1.add(bot1)
        
        
        #self.bot2 = Bot2(self)
        
        self.gun1 = Guns(self)
        self.fire = False
        self.gun1_status = False
        
        self.gap = 0
        self.gap_y = 0
        self.gap_left = False
        self.gap_right = False
        
        
     
     
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #self.fire_direction(mouse_pos)
                self.fire_bullets(mouse_pos)
                
                #self.fire_direction(mouse_pos)
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.bender.jump()
                if event.key == pygame.K_a:  
                    self.bender.direction = 'left'
                    #self.bender.moving_left = True
                    self.gap_left = True
                if event.key == pygame.K_d:
                    #self.bender.moving_right = True
                    self.bender.direction = 'right'
                    self.gap_right = True
                if event.key == pygame.K_f:
                    self.bender.shot_f =True
                    print(f'self.bender.real_x = {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
                    for bot1 in self.bots1:
                        print(f'self.bot1.x_on_a_map = {bot1.x_on_a_map} self.bot1._on_a_map_y = {bot1.y_on_a_map}')
                        print(f'self.bot1.rect.x = {bot1.rect.x} self.bot1.rect.y = {bot1.rect.y}')                   

                if event.key == pygame.K_k:
                    pass
                if event.key == pygame.K_l:
                    self.fire = True
                    mouse_pos = pygame.mouse.get_pos()
                    #self.fire_direction(mouse_pos)
                    self.fire_bullets(mouse_pos)
                    #self.fire_bullets()
                if event.key == pygame.K_1:
                    if self.gun1_status == False:
                        self.gun1_status = True
                    elif self.gun1_status == True:
                        self.gun1_status = False
                        
                if event.key == pygame.K_LEFT:
                    self.angle_minus = True
                if event.key == pygame.K_RIGHT:
                    self.angle_plus = True

            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:                    
                    #self.bender.moving_left = False
                    self.gap_left = False
                if event.key == pygame.K_d:
                    #self.bender.moving_right = False 
                    self.gap_right = False
                if event.key == pygame.K_f:
                    self.bender.shot_f = False
                #if event.key == pygame.K_k:
                    #self.fire = False
                    
                if event.key == pygame.K_LEFT:
                    self.angle_minus = False
                if event.key == pygame.K_RIGHT:
                    self.angle_plus = False
                    
    def fire_bullets(self, mouse_pos):
        if len(self.bullets) <= 999999:#BULLET_LIMIT: #my fire limit
            self.rect = pygame.draw.circle(self.screen, RED, (0, 0), 6)
            
            if self.bender.direction == 'right':
                #self.rect.midright = self.bender.rect.midright
                self.rect.x = self.bender.rect.x
                self.rect.y = self.bender.rect.y
                self.rect.x += 80
                self.rect.y += 60
                
                #self.rect.midleft = self.bender.rect.midleft
                
                self.mouse_pos_x, self.mouse_pos_y = mouse_pos
            
                self.mouse_pos_x  = self.mouse_pos_x - self.rect.x
                self.mouse_pos_y  = self.mouse_pos_y - self.rect.y
                
                print(f'self.mouse_pos_x = {self.mouse_pos_x}, self.mouse_pos_y = {self.mouse_pos_y}')

                xx = self.mouse_pos_x
                yy = self.mouse_pos_y
                line = (math.sqrt(xx**2 + yy**2))
                
                print(f'line = {line} xx == {xx} yy== {yy}')
                print(f'self.bender.real_x = {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
            
                self.mouse_cos = xx/line
                self.mouse_sin = yy/line
            
                if -1 <= self.mouse_cos <= 1 and -1 <= self.mouse_sin <= 1 and self.gun1_status == True:
                    new_bullet = Bullet(self, self.bender.direction)
                    self.bullets.add(new_bullet)
                
            if self.bender.direction == 'left' :
                #self.rect.midleft = self.bender.rect.midleft
                self.rect.x = self.bender.rect.x
                self.rect.y = self.bender.rect.y
                self.rect.x -= 25
                self.rect.y += 60
                
                #self.rect.midleft = self.bender.rect.midleft
                
                self.mouse_pos_x, self.mouse_pos_y = mouse_pos
            
                self.mouse_pos_x  = self.mouse_pos_x - self.rect.x
                self.mouse_pos_y  = self.mouse_pos_y - self.rect.y
                
                print(f'self.mouse_pos_x = {self.mouse_pos_x}, self.mouse_pos_y = {self.mouse_pos_y}')

                xx = self.mouse_pos_x
                yy = self.mouse_pos_y
                line = (math.sqrt(xx**2 + yy**2))
                
                print(f'line = {line} xx == {xx} yy== {yy}')
                print(f'self.bender.real_x = {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
            
                self.mouse_cos = xx/line
                self.mouse_sin = yy/line
            
                if -1 <= self.mouse_cos <= 1 and -1 <= self.mouse_sin <= 1 and self.gun1_status == True:
                    new_bullet = Bullet(self, self.bender.direction)
                    self.bullets.add(new_bullet)
                
                #if -1 <= self.mouse_sin <= 1 and -1 <= self.mouse_cos <= 1 and self.gun1_status == True:
                #new_bullet = Bullet(self, self.bender.direction)
                #self.bullets.add(new_bullet)
                    
                    
    #def fire_direction(self, mouse_pos):
        #self.mouse_pos_x, self.mouse_pos_y = mouse_pos
        
        #self.mouse_pos_x  = self.mouse_pos_x - 400#self.rect.x
        #self.mouse_pos_y  = self.mouse_pos_y - 400#self.rect.y
        ##self.mouse_pos_x -= self.bender.real_x
        ##self.mouse_pos_y -= self.bender.real_y
        
        #print(f'self.mouse_pos_x = {self.mouse_pos_x}, self.mouse_pos_y = {self.mouse_pos_y}')
        #pass
    
                    
    def run(self):
        #gap = 0
        while True:
            
            for r in range(1000):
                self._check_events()
                
                self.screen.fill(BGR_COLOR)
                
                temp_bullet_x = 0
                temp_bullet_y = 0               
                            
                temp_bot1_x = 0  
                temp_bot1_y = 0 
                
                
                
                if self.angle_minus == True:
                    self.angle -= 0.05
                if self.angle_plus == True:
                    self.angle += 0.05              
                
                
                if self.bender.jump_activate < self.bender.height_jump and self.bender.jump_up == True:
                    self.gap_y -= self.bender.size_of_jump
                    self.bender.real_y -= self.bender.size_of_jump # real
                    self.bender.jump_activate += 1
                    #print(f'{self.bender.jump_activate}  {self.bender.jump_up}')
                    
                    temp_bot1_y   += self.bender.size_of_jump
                    #self.bot2.rect.y  += self.bender.size_of_jump
                    temp_bullet_y  += self.bender.size_of_jump 
                
                elif self.bender.jump_activate == self.bender.height_jump and self.bender.jump_up == True:
                    self.bender.jump_up = False 
                    self.bender.jump_activate -= 1 
                    self.gap_y += self.bender.size_of_jump
                    self.bender.real_y += self.bender.size_of_jump
                    
                    temp_bot1_y   -= self.bender.size_of_jump
                    #self.bot2.rect.y  -= self.bender.size_of_jump
                    temp_bullet_y  -= self.bender.size_of_jump 
                    #print(f'{self.bender.jump_activate}  {self.bender.jump_up}')
                    #print(f'temp_bot1_y  = {temp_bot1_y }  self.bender.rect.y = {self.bender.rect.y}')
                elif self.bender.jump_activate > 0 and self.bender.jump_up == False:
                    self.gap_y += self.bender.size_of_jump
                    self.bender.real_y += self.bender.size_of_jump
                    self.bender.jump_activate -= 1
                    
                    temp_bot1_y   -= self.bender.size_of_jump
                    #self.bot2.rect.y  -= self.bender.size_of_jump 
                    temp_bullet_y  -= self.bender.size_of_jump 
                    #print(f'temp_bot1_y  = {temp_bot1_y } self.bender.rect.y = {self.bender.rec7t.y}')
                elif self.bender.jump_activate == 0 and self.bender.jump_up == False:
                    self.bender.jump_act = False
                
               
                if self.gap_right == True:
                    self.gap += 0.25
                    self.bender.real_x += 0.25 *  TILE # right
                    
                    temp_bullet_x -= 0.25 *  TILE
                    #for bullet in self.bullets:
                        #bullet.real_x -= 0.25 *  TILE
                    
                    temp_bot1_x -= 0.25 *  TILE
                    #print(f'self.bender.real_x= {self.bender.real_x} temp_bot1_x = {temp_bot1_x} xxx= {temp_bot1_x - TILE*self.gap}')
                    #self.bot2.rect.x  = self.bot2.rect.x - 0.25 * TILE
                    #print(f' self.bender.real_x= {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
                if self.gap_left == True:
                    self.gap -= 0.25
                    self.bender.real_x -= 0.25 * TILE # right
                    temp_bot1_x += 0.25 *  TILE#0.25 * TILE
                    
                    temp_bullet_x += 0.25 *  TILE
                    #for bullet in self.bullets:
                        #bullet.real_x += 0.25 *  TILE
                    #self.bot2.rect.x  = self.bot2.rect.x + 0.25 * TILE
                    #print(f'self.bender.real_x= {self.bender.real_x} temp_bot1_x = {temp_bot1_x}')
                    #print(f' self.bender.real_x= {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
                

                
                #falling
                fall = False
                for row in range(len(self.a_map.hard_wall)):
                    for xy in range(len(self.a_map.hard_wall[row])):
                        x = self.a_map.hard_wall[row][xy][1]# -  self.gap
                        y = self.a_map.hard_wall[row][xy][0] #- self.gap_y
                        #print(f'x = {x} y= {y} self.bender.real_x= {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT <= y + 5: # LEFT DOWN
                            #print(f'x = {x} y= {y} self.bender.real_x= {self.bender.real_x } self.bender.real_y = {self.bender.real_y + self.bender.Y_HEIGHT}')
                            fall = True
                            self.bender.jump_activate = 0
                            self.bender.jump_up = False
                        elif x <= self.bender.real_x+ self.bender.X_WIGHT/2  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT <= y + 5: # MIDLE DOWN
                            #print(f'x = {x} y= {y} self.bender.real_x= {self.bender.real_x+ self.bender.X_WIGHT  } self.bender.real_y = {self.bender.real_y + self.bender.Y_HEIGHT}')
                            fall = True
                            self.bender.jump_activate = 0
                            self.bender.jump_up = False
                        
                        elif x <= self.bender.real_x+ self.bender.X_WIGHT  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT <= y + 5: # RIGHT DOWN
                            #print(f'x = {x} y= {y} self.bender.real_x= {self.bender.real_x+ self.bender.X_WIGHT  } self.bender.real_y = {self.bender.real_y + self.bender.Y_HEIGHT}')
                            fall = True
                            self.bender.jump_activate = 0
                            self.bender.jump_up = False
                            
                        #hit in a celling
                        
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y <= y +  TILE: # LEFT TOP
                            self.bender.jump_up = False
                        if x <= self.bender.real_x + self.bender.X_WIGHT/2  <= x + TILE and y <= self.bender.real_y <= y +  TILE: # LEFT MIDLE
                            self.bender.jump_up = False
                        if x <= self.bender.real_x + self.bender.X_WIGHT  <= x + TILE and y <= self.bender.real_y <= y +  TILE: # RIGHT TOP
                            self.bender.jump_up = False
                            
                        #hit left 
                        
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y <= y +TILE and self.gap_left == True: # LEFT TOP
                            self.gap_left = False
                            self.gap += 0.25
                            self.bender.real_x += 0.25 *  TILE # right
                            temp_bot1_x -= 0.25 *  TILE
                            temp_bullet_x -= 0.25 *  TILE
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y  + TILE <= y + TILE and self.gap_left == True:  # LEFT MIDLE
                            self.gap_left = False
                            self.gap += 0.25
                            self.bender.real_x += 0.25 *  TILE # right
                            temp_bot1_x -= 0.25 *  TILE
                            temp_bullet_x -= 0.25 *  TILE
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y  + TILE*2 <= y + TILE and self.gap_left == True:  # LEFT MIDLE
                            self.gap_left = False
                            self.gap += 0.25
                            self.bender.real_x += 0.25 *  TILE # right
                            temp_bot1_x -= 0.25 *  TILE
                            temp_bullet_x -= 0.25 *  TILE
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y  + TILE*3 <= y + TILE and self.gap_left == True:  # LEFT MIDLE
                            self.gap_left = False
                            self.gap += 0.25
                            self.bender.real_x += 0.25 *  TILE # right
                            temp_bot1_x -= 0.25 *  TILE
                            temp_bullet_x -= 0.25 *  TILE
                        if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y + TILE*4 <= y + TILE and self.gap_left == True: # LEFT MIDLE
                            self.gap_left = False
                            self.gap += 0.25
                            self.bender.real_x += 0.25 *  TILE# right
                            temp_bot1_x -= 0.25 *  TILE
                            temp_bullet_x -= 0.25 *  TILE



                        #hit right
                        
                        if x <= self.bender.real_x + self.bender.X_WIGHT <= x + TILE and y <= self.bender.real_y <= y + TILE and self.gap_right == True: # LEFT TOP
                            self.gap_right = False
                            self.gap -= 0.25
                            self.bender.real_x -= 0.25 *  TILE # left
                            temp_bot1_x += 0.25 *  TILE
                            temp_bullet_x += 0.25 *  TILE
                            
                        if x <= self.bender.real_x + self.bender.X_WIGHT <= x + TILE and y <= self.bender.real_y + TILE <= y + TILE and self.gap_right == True: 
                            self.gap_right = False
                            self.gap -= 0.25
                            self.bender.real_x -= 0.25 *  TILE # left
                            temp_bot1_x +=0.25 *  TILE
                            temp_bullet_x += 0.25 *  TILE
                            
                        if x <= self.bender.real_x + self.bender.X_WIGHT <= x + TILE and y <= self.bender.real_y + TILE * 2 <= y + TILE and self.gap_right == True:
                            self.gap_right = False
                            self.gap -= 0.25
                            self.bender.real_x -= 0.25 *  TILE # left
                            temp_bot1_x += 0.25 *  TILE
                            temp_bullet_x += 0.25 *  TILE
                            
                        if x <= self.bender.real_x + self.bender.X_WIGHT <= x + TILE and y <= self.bender.real_y + TILE *3 <= y + TILE and self.gap_right == True: 
                            self.gap_right = False
                            self.gap -= 0.25
                            self.bender.real_x -= 0.25 *  TILE # left
                            
                            temp_bot1_x += 0.25 *  TILE
                            
                            temp_bullet_x += 0.25 *  TILE
                            
                        if x <= self.bender.real_x + self.bender.X_WIGHT <= x + TILE and y <= self.bender.real_y +TILE *4 <= y + TILE and self.gap_right == True:
                            self.gap_right = False
                            self.gap -= 0.25
                            self.bender.real_x -= 0.25 *  TILE # left
                            
                            temp_bot1_x += 0.25 *  TILE
                            
                            temp_bullet_x += 0.25 *  TILE
                            
                            #stairs
                        for i in  range(len(self.a_map.hard_wall[row-1])):
                            right_x = self.a_map.hard_wall[row-1][i][1]
                            right_y = self.a_map.hard_wall[row-1][i][0]
                            if right_x <= self.bender.real_x + self.bender.X_WIGHT +10  <= right_x + TILE and  right_y <= self.bender.real_y + self.bender.Y_HEIGHT -5 <= right_y +TILE and self.gap_right == True: # RIGHT DOWN
                                self.bender.real_x += 0.25 *  TILE
                                self.gap += 0.25#
                                self.bender.real_y += -25
                                self.gap_y += -25
                                
                                temp_bot1_x -= 0.25 *  TILE
                                temp_bot1_y  += 25
                                
                                temp_bullet_x -= 0.25 *  TILE
                                temp_bullet_y += 25
                                
                            if right_x <= self.bender.real_x -10  <= right_x + TILE and  right_y <= self.bender.real_y + self.bender.Y_HEIGHT -5 <= right_y +TILE and self.gap_left == True: # LEFT DOWN
                                self.bender.real_x -= 0.25 *  TILE 
                                self.gap -= 0.25#
                                self.bender.real_y += -25
                                self.gap_y += -25
                                
                                temp_bot1_x += 0.25 *  TILE
                                temp_bot1_y  += 25
                                
                                temp_bullet_x += 0.25 *  TILE
                                temp_bullet_y += 25
                    
                #print(fall)
                if not fall and self.bender.jump_act == False:
                    self.bender.real_y += self.bender.size_of_jump#self.bender.speed
                    self.gap_y += self.bender.size_of_jump#self.bender.speed
                    temp_bot1_y   -= self.bender.size_of_jump
                    temp_bullet_y -= self.bender.size_of_jump


                
                self.a_map.draw(self,self.gap, self.gap_y)

           
                if r % 20 == 0:
                    #print(f'i= {r}')
                    #self.bot2.bore() 
                    pass
                if r % 6 == 0:
                    self.bender.bore()
                
                for bot1 in self.bots1:
                    bot1.real_x += temp_bot1_x #+ 904  #last change
                    bot1.real_y += temp_bot1_y #+ 282
                    bot1.blitme() 
                    
                #self.bot2.rect.x = temp_bot1_x + 1024  #last change
                #self.bot2.rect.y = temp_bot1_y + 300
                #self.bot2.blitme()

                self.bender.blitme()

                if self.gun1_status == True:
                    self.gun1.draw(self.bender.rect.x, self.bender.rect.y, self.bender.direction, self.fire)
                    if self.fire == True:
                        self.fire = False
                        

                    #pygame.draw.rect(self.screen, DARKGRAY, (x - TILE*gap, y - gap_y, TILE, TILE),2)
                for bullet in self.bullets:
                    bullet.real_x += temp_bullet_x
                    bullet.real_y += temp_bullet_y
                    for bot1 in self.bots1:
                        if  bot1.x_on_a_map <= bullet.x_on_a_map  <= bot1.x_on_a_map + bot1.size_x and bot1.y_on_a_map <= bullet.y_on_a_map <= bot1.y_on_a_map + bot1.size_y:
                            self.bots1.remove(bot1)
                            self.bullets.remove(bullet)
                            
                    # If you wanna destroy black and white squares       
                            
                    ##for row in range(len(self.a_map.world_map_left_to_right)):
                        ##for xy in range(len(self.a_map.world_map_left_to_right[row])):
                            ###print(self.a_map.world_map_left_to_right[row][xy])
                            ##if  self.a_map.world_map_left_to_right[row][xy][0] <= bullet.x_on_a_map  <= self.a_map.world_map_left_to_right[row][xy][0] +TILE and self.a_map.world_map_left_to_right[row][xy][1] <= bullet.y_on_a_map <= self.a_map.world_map_left_to_right[row][xy][1] +TILE:
                                ##self.bullets.remove(bullet)
                                ###print(dir(self.a_map.world_map_left_to_right))
                                ##self.a_map.world_map_left_to_right[row].pop(xy)
                                ##break
                                ###print(self.a_map.world_map_left_to_right)
                    
                    for row in range(len(self.a_map.hard_wall)):
                        for xy in range(len(self.a_map.hard_wall[row])):
                            #print(self.a_map.world_map_list[row][xy])
                            
                            if  self.a_map.hard_wall[row][xy][1] <= bullet.x_on_a_map  <= self.a_map.hard_wall[row][xy][1] +TILE and self.a_map.hard_wall[row][xy][0] <= bullet.y_on_a_map <= self.a_map.hard_wall[row][xy][0] +TILE:
                                self.bullets.remove(bullet)
                                ##print(dir(self.a_map.world_map_left_to_right))
                                self.a_map.hard_wall[row].pop(xy)
                                break
                    if bullet.need_to_delete() == True:
                        self.bullets.remove(bullet)
                        
                    bullet.update()
                    
                  
                for bullet in self.bullets:
                    bullet.draw_bullet()
                    
                #pygame.draw.rect(self.screen, DARKGRAY, (self.bender.rect.x, self.bender.rect.y, TILE, TILE))
                
                ##if self.bender.rect.x == self.bender.real_x:
                    #self.rect = pygame.draw.line(self.screen, GREEN, (self.bender.rect.x, self.bender.rect.y), (self.mouse_pos_x, self.mouse_pos_y), 2)
                #pygame.draw.line(self.screen, GREEN, (self.bender.rect.x, self.bender.rect.y), (self.bender.rect.x + 300 * math.cos(self.angle),
                
                pygame.display.flip() 
                self.clock.tick(FPS)
                #time.sleep(2)

if __name__ == '__main__':
    future = Game()
    future.run()
