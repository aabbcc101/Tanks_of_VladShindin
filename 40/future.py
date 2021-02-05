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
from camera import Camera

class Game():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Future")
        
        self.clock = pygame.time.Clock()
        
        self.a_map = World_map()
        
        self.bender = Robot(self)
        
        self.mouse_pos_x, self.mouse_pos_y = 0,0

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
        
        
        self.bots2 = pygame.sprite.Group()
        self.bot2 = Bot2(self)
        self.bot2.rect.x =  600
        self.bot2.rect.y = 92
        self.bots2.add(self.bot2)
        
        self.gun1 = Guns(self)
        self.fire = False
        self.gun1_status = False

        self.move_left = False
        self.move_right = False
        
        self.camera = Camera(self.camera_configure,self)
        
     
     
    def camera_configure(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l+SCREEN_WIDTH / 2, -t+SCREEN_HEIGHT / 2

        l = min(0, l)                           # Не движемся дальше левой границы
        l = max(-(self.a_map.level_wight * TILE - camera.width), l)   # Не движемся дальше правой границы
        t = max(-(self.a_map.level_height * TILE - camera.height), t) # Не движемся дальше нижней границы
        t = min(0, t)                           # Не движемся дальше верхней границы

        return pygame.Rect(l, t, w, h)
     
     
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
                    self.move_left = True
                if event.key == pygame.K_d:
                    #self.bender.moving_right = True
                    self.bender.direction = 'right'
                    self.move_right = True
                if event.key == pygame.K_f:
                    self.bender.shot_f =True
                    print(f'self.bender.real_x = {self.bender.real_x} self.bender.real_y = {self.bender.real_y}')
                    #for bot1 in self.bots1:
                        #print(f'self.bot1.x_on_a_map = {bot1.x_on_a_map} self.bot1._on_a_map_y = {bot1.y_on_a_map}')
                        #print(f'self.bot1.rect.x = {bot1.rect.x} self.bot1.rect.y = {bot1.rect.y}')                   

                if event.key == pygame.K_k:
                    pass
                if event.key == pygame.K_l:
                    self.fire = True
                    mouse_pos = pygame.mouse.get_pos()
                    self.fire_bullets(mouse_pos)
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
                    self.move_left = False
                if event.key == pygame.K_d:
                    self.move_right = False
                if event.key == pygame.K_f:
                    self.bender.shot_f = False
                if event.key == pygame.K_k:
                    pass                    
                if event.key == pygame.K_LEFT:
                    self.angle_minus = False
                if event.key == pygame.K_RIGHT:
                    self.angle_plus = False
                    
    def fire_bullets(self, mouse_pos):
        if len(self.bullets) <= 999999:#BULLET_LIMIT: #my fire limit
            self.rect = pygame.draw.circle(self.screen, RED, (0, 0), 6)
            
            if self.bender.direction == 'right':
        
                self.rect = self.camera.apply(self.bender)
                self.rect.x += 80
                self.rect.y += 60
                
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

                self.rect = self.camera.apply(self.bender)
                self.rect.x -= 25
                self.rect.y += 60
                
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

    def jump_of_hero(self):
        ##hit in a celling during a jump
        self.checking_for_a_celling()
        
        if self.bender.jump_activate < self.bender.height_jump and self.bender.jump_up == True:
            self.bender.real_y -= self.bender.size_of_jump # real
            self.bender.jump_activate += 1
        
        elif self.bender.jump_activate == self.bender.height_jump and self.bender.jump_up == True:
            self.bender.jump_up = False 
            self.bender.jump_activate -= 1 
            self.bender.real_y += self.bender.size_of_jump
        elif self.bender.jump_activate > 0 and self.bender.jump_up == False:
            self.bender.real_y += self.bender.size_of_jump
            self.bender.jump_activate -= 1
        elif self.bender.jump_activate == 0 and self.bender.jump_up == False:
            self.bender.jump_act = False

                
    def checking_for_a_celling(self):
        self.bender.celling = False
        for x,y in self.a_map.hard_wall_left_to_right[((self.bender.real_y) // TILE)-1]:    
            if x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y -self.bender.size_of_jump <= y +  TILE: # LEFT TOP
                self.bender.jump_up = False
                self.bender.celling = True
            if x <= self.bender.real_x + self.bender.X_WIGHT/2  <= x + TILE and y <= self.bender.real_y-self.bender.size_of_jump <= y +  TILE: # LEFT MIDLE
                self.bender.jump_up = False
                self.bender.celling = True
            if x <= self.bender.real_x + self.bender.X_WIGHT  <= x + TILE and y <= self.bender.real_y-self.bender.size_of_jump <= y +  TILE: # RIGHT TOP
                self.bender.jump_up = False 
                self.bender.celling = True
                 
                 
    def run(self):
        while True:
            for r in range(1000):
                self._check_events()
        
                self.screen.fill(BGR_COLOR)          
                
                self.jump_of_hero()
                
                #BOTTOM
                #looking for a surface
                fall = True
                for x,y in self.a_map.hard_wall_left_to_right[((self.bender.real_y +self.bender.Y_HEIGHT) // TILE)]:
                    if (x <= self.bender.real_x  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT+ self.bender.size_of_jump <= y +5 # LEFT DOWN
                        or x <= self.bender.real_x+ self.bender.X_WIGHT/2  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT <= y +5  # MIDLE DOWN
                        or x <= self.bender.real_x+ self.bender.X_WIGHT  <= x + TILE and y <= self.bender.real_y + self.bender.Y_HEIGHT <= y +5): # RIGHT DOWN
                        self.bender.jump_activate = 0
                        self.bender.jump_up = False 
                        fall = False
                        

                # LEFT SIDE
                #checking_for_the_left_brick
                step_left = False
                step_right = False
                if self.move_left == True:
                    
                    if  fall or self.bender.jump_activate != 0: #to avoid akward momens in the air
                        for y,x in self.a_map.hard_wall[((self.bender.real_x ) // TILE)-1]:
                            if (x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y <= y +TILE # LEFT TOP
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE <= y + TILE            # LEFT MIDLE
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*2 <= y + TILE          # downer LEFT MIDLE    
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*3 <= y + TILE          # mode downer LEFT MIDLE    
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y + TILE*4 <= y + TILE):         # bottom LEFT MIDLE    
                                self.move_left = False
                                
                    elif not fall or self.bender.jump_activate == 0:
                        for y,x in self.a_map.hard_wall[((self.bender.real_x ) // TILE)-1]:
                            if (x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y <= y +TILE # LEFT TOP
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE <= y + TILE            # LEFT MIDLE
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*2 <= y + TILE          # downer LEFT MIDLE    
                                or x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*3 <= y + TILE):          # mode downer LEFT MIDLE       
                                self.move_left = False
                        #checking_for_a_step
                        for y,x in self.a_map.hard_wall[((self.bender.real_x ) // TILE)]:
                            if x <= self.bender.real_x - self.bender.speed  <= x + TILE and y <= self.bender.real_y + TILE*4 <= y + TILE: #step
                                step_left = True
                                print(True)
                                break
                        
                        self.checking_for_a_celling() #during climing
                        if step_left == True and self.move_left != False and self.bender.celling != True:
                            if r % 2 == 0: #it is for hard climing!!!!
                                self.bender.real_x -= TILE
                                self.bender.real_y += -TILE

                    ##moving to left
                    if step_left == False and self.move_left == True:
                        self.bender.real_x -= self.bender.speed 
                        print('moving left')
                         


                # RIGHT
                #checking_for_the_right_brick
                if self.move_right == True:
                    
                    if fall or self.bender.jump_activate != 0: #to avoid akward momens in the air
                        for y,x in self.a_map.hard_wall[((self.bender.real_x + self.bender.X_WIGHT) // TILE)+1]:
                            if (x <= self.bender.real_x + self.bender.X_WIGHT + self.bender.speed  <= x + TILE and y <= self.bender.real_y <= y +TILE # right TOP
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE <= y + TILE            # right MIDLE
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*2 <= y + TILE          # downer right MIDLE    
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*3 <= y + TILE          # mode downer right MIDLE    
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y + TILE*4 <= y + TILE):         # bottom right MIDLE    
                                self.move_right = False
                                
                    elif not fall or self.bender.jump_activate == 0:
                        for y,x in self.a_map.hard_wall[((self.bender.real_x + self.bender.X_WIGHT) // TILE)+1]:
                            if (x <= self.bender.real_x + self.bender.X_WIGHT + self.bender.speed  <= x + TILE and y <= self.bender.real_y <= y +TILE # right TOP
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE <= y + TILE            # right MIDLE
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*2 <= y + TILE          # downer right MIDLE    
                                or x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y  + TILE*3 <= y + TILE):          # mode downer right MIDLE    
                                self.move_right = False
                            
                        #checking_for_a_step
                        for y,x in self.a_map.hard_wall[((self.bender.real_x + self.bender.X_WIGHT) // TILE)]:
                            if x <= self.bender.real_x + self.bender.X_WIGHT+ self.bender.speed  <= x + TILE and y <= self.bender.real_y + TILE*4 <= y + TILE:   #step 
                                step_right = True
                                print(True)
                                break
                        
                        self.checking_for_a_celling() #during climing
                        if step_right == True and self.move_right != False and self.bender.celling != True:
                            if r % 2 == 0: #it is for hard climing!!!!
                                self.bender.real_x += TILE
                                self.bender.real_y += -TILE

                    ##moving to right
                    if step_right == False and self.move_right == True:
                        self.bender.real_x += self.bender.speed 
                        print('moving right')
     
                   
                ### fallen 
                if fall and self.bender.jump_act == False:
                    self.bender.real_y += self.bender.size_of_jump      
                        

                self.bender.rect.x = self.bender.real_x
                self.bender.rect.y = self.bender.real_y 

                self.camera.update(self.bender)
                self.a_map.draw(self)
                
                
                
                #TESTING I am watching neded row that way
                #for y,x in self.a_map.hard_wall[((self.bender.real_x + self.bender.X_WIGHT) // TILE)+1]:#self.bender.real_y // TILE]: for x,y in self.a_map.hard_wall_left_to_right[(self.bender.real_y // TILE)-1]:
                #for x,y in self.a_map.hard_wall_left_to_right[((self.bender.real_y)  // TILE)]:
                #for y,x in self.a_map.hard_wall[((self.bender.real_x + self.bender.X_WIGHT) // TILE)+1]:
                for y,x in self.a_map.hard_wall[((self.bender.real_x ) // TILE)-1]:
                    square = pygame.Rect(x, y, TILE, TILE)
                    pygame.draw.rect(self.screen, DARKGRAY, self.camera.apply_wall(square),2)
           
                if r % 20 == 0:
                    self.bot2.bore()
                    
                if r % 6 == 0:
                    self.bender.bore()

                
                self.bender.blitme(self.camera.apply(self.bender))

                for bot1 in self.bots1:
                    bot1.blitme(self.camera.apply(bot1)) 
                
                for bot2 in self.bots2:
                    bot2.blitme(self.camera.apply(bot2)) 
                
                if self.gun1_status == True:
                    self.gun1.draw(self.camera.apply(self.bender), self.bender.direction, self.fire)
                    if self.fire == True:
                        self.fire = False

                for bullet in self.bullets:
                    for bot1 in self.bots1:
                        if  bot1.x_on_a_map <= bullet.x_on_a_map  <= bot1.x_on_a_map + bot1.size_x and bot1.y_on_a_map <= bullet.y_on_a_map <= bot1.y_on_a_map + bot1.size_y:
                            self.bots1.remove(bot1)
                            self.bullets.remove(bullet)
                            
                    for bot2 in self.bots2:
                        if  bot2.rect.x <= bullet.x_on_a_map  <= bot2.rect.x + bot2.size_x and bot2.rect.y <= bullet.y_on_a_map <= bot2.rect.y + bot2.size_y:
                            self.bots2.remove(bot2)
                            self.bullets.remove(bullet)
                                    
                    ## If you wanna destroy black and white squares       
                            
                    ##for row in range(len(self.a_map.world_map_left_to_right)):
                        ##for xy in range(len(self.a_map.world_map_left_to_right[row])):
                            ##if  self.a_map.world_map_left_to_right[row][xy][0] <= bullet.x_on_a_map  <= self.a_map.world_map_left_to_right[row][xy][0] +TILE and self.a_map.world_map_left_to_right[row][xy][1] <= bullet.y_on_a_map <= self.a_map.world_map_left_to_right[row][xy][1] +TILE:
                                ##self.bullets.remove(bullet)
                                ##self.a_map.world_map_left_to_right[row].pop(xy)
                                ##break
                    
                    first_flag_break = False
                    for row in range(len(self.a_map.hard_wall)):
                        if first_flag_break == True:
                            break
                        for xy in range(len(self.a_map.hard_wall[row])):
                            if  self.a_map.hard_wall[row][xy][1] <= bullet.x_on_a_map  <= self.a_map.hard_wall[row][xy][1] +TILE and self.a_map.hard_wall[row][xy][0] <= bullet.y_on_a_map <= self.a_map.hard_wall[row][xy][0] +TILE:
                                self.bullets.remove(bullet)
                                #print(f'self.a_map.hard_wall[row][xy] {self.a_map.hard_wall[row][xy]}')

                                flag_break = False
                                for lr_row in range(len(self.a_map.hard_wall_left_to_right)):
                                    if flag_break == True:
                                        break
                                    for xy_lr in range(len(self.a_map.hard_wall_left_to_right[lr_row])):
                                        if (self.a_map.hard_wall[row][xy][1] == self.a_map.hard_wall_left_to_right[lr_row][xy_lr][0]
                                            and self.a_map.hard_wall[row][xy][0] == self.a_map.hard_wall_left_to_right[lr_row][xy_lr][1]):
                                            self.a_map.hard_wall_left_to_right[lr_row].pop(xy_lr)
                                            flag_break = True
                                            break
                    
                                self.a_map.hard_wall[row].pop(xy)
                                first_flag_break = True
                                break
                    if bullet.need_to_delete() == True:
                        self.bullets.remove(bullet)
                        
                    bullet.update()
                    
                  
                for bullet in self.bullets:
                    bullet.draw_bullet(self.camera.apply(bullet))
            
            
                pygame.display.flip() 
                self.clock.tick(FPS)
    
if __name__ == '__main__':
    future = Game()
    future.run()
