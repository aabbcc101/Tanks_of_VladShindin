import sys
import pygame
from ship import Ship
from settings import *
#import turret
from map import World_map
from bullet import Bullet
from enemy import Enemy
from bullet_of_an_enemy import Evil_bullet
from button import Button
from stats import Stats

class Invasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.evil_bullets = pygame.sprite.Group()
        
        self.a_map = World_map()
                
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Invasion")
               
        self.level = 0
        self.stats = Stats(self)
        
        temp_x, temp_y = 200, 50
        temp_color = (0, 255, 0)
        temp_text_color =(255, 255, 255)
        self.play_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "PLAY")
        
        temp_x, temp_y = 350, 50
        temp_color = (100, 100, 100)
        temp_text_color =(255, 0, 0)
        self.win_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "YOU ARE A WINNER!")
        
        self.myTank = Ship(self)
        self.myTank.live  = 0

        self.image = pygame.image.load('images/brick_wall3.png')        
        self.rect = self.image.get_rect()

    def delete_all_bullets(self):
        self.evil_bullets.empty()
        self.bullets.empty()

        
    def level_1(self):
        self.level = 1
        self.a_map.create_map() #create a map 1
        self.delete_all_bullets()
        #self.myTank.out_coordinates = []
        self.myTank.create_map() #create a map 
        self.myTank.right_coordinates() # set new coordinates

        #self.myEnemy = Enemy(self)
        #print('LEVEL 111111111111111111111111111111') doNE

        self.enemies_list_coordinate = [] 
        
                
        for i in range(6):
            #self.create_an_enemy()
            self.create_an_enemy2()
                    #add coordianates

        self.settings.bgr_color = WHITE 
        self.image = pygame.image.load('images/brick_wall3.png')  
 
    def level_2(self):
        self.delete_all_bullets()
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall2.png')
        self.enemies_list_coordinate = [] 
        for i in range(9):
            #self.create_an_enemy()
            self.create_an_enemy2()

        
    def level_3(self):
        self.delete_all_bullets()
        
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall.png')
        self.enemies_list_coordinate = [] 
        for i in range(12):
            #self.create_an_enemy()
            self.create_an_enemy2()
            
            
    def level_4(self):
        self.delete_all_bullets()
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall2.png')
        self.enemies_list_coordinate = [] 
        for i in range(15):
            #self.create_an_enemy()
            self.create_an_enemy2()

        
    def level_5(self):
        self.delete_all_bullets()
        
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall.png')
        self.enemies_list_coordinate = [] 
        for i in range(17):
            #self.create_an_enemy()
            self.create_an_enemy2()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_win_button(mouse_pos)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()                
                if event.key == pygame.K_RIGHT:
                    #self.myTank.rect.x += self.myTank.ship_speed
                    self.myTank.moving_right = True
                if event.key == pygame.K_LEFT:
                    #self.myTank.rect.x -= self.myTank.ship_speed
                    self.myTank.moving_left = True
                if event.key == pygame.K_UP:
                    #self.myTank.rect.y -= self.myTank.ship_speed
                    self.myTank.moving_up = True
                if event.key == pygame.K_DOWN:
                    #self.myTank.rect.y += self.myTank.ship_speed
                    self.myTank.moving_down = True
                if event.key == pygame.K_SPACE:
                    self.fire_bullets()
                if event.key == pygame.K_BACKSPACE:
                    self._check_enter()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.myTank.moving_right = False 
                if event.key == pygame.K_LEFT:
                    self.myTank.moving_left = False
                if event.key == pygame.K_UP:
                    self.myTank.moving_up = False 
                if event.key == pygame.K_DOWN:
                    self.myTank.moving_down = False
                    
    def _check_enter(self):
        self.enemies.empty()
        self.stats.game_active = True
        self.myTank.live  = LIVE_OF_TANK
        self.level_1()
        pygame.mouse.set_visible(False)
 
    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active: # invisible button musnt be worked
            self.enemies.empty()
            self.stats.game_active = True
            self.myTank.live  = LIVE_OF_TANK
            self.level_1()
            pygame.mouse.set_visible(False)
            #print(dir(self.enemies))
            
    def _check_win_button(self,mouse_pos):
        if self.win_button.rect.collidepoint(mouse_pos) and self.myTank.live  > 0 and not self.stats.game_active: # invisible button musnt be worked
            self.enemies.empty()
            self.stats.game_active = True
            self.myTank.live  = LIVE_OF_TANK
            self.level_1()
            pygame.mouse.set_visible(False)
                    
    def fire_bullets(self):
        if len(self.bullets) <= BULLET_LIMIT: #my fire limit
            new_bullet = Bullet(self, self.myTank.direction,self.level)
        #if self.level == 2:
            ##new_bullet.change_map()
            self.bullets.add(new_bullet)
        
    def fire_evil_bullets(self,enemy):
        new_bullet = Evil_bullet(self, enemy.rect.x, enemy.rect.y, enemy.direction,self.level)
        #if self.level == 2:
            ##new_bullet.change_map()
        self.evil_bullets.add(new_bullet)
        
    #def create_an_enemy(self):
        #new_enemy = Enemy(self)
        #self.enemies.add(new_enemy)
    
    def create_an_enemy2(self): 
        new_enemy = Enemy(self)
        if self.level == 1:
            new_enemy.create_map() #CHANGE a map
            #new_enemy.ship_speed = 0.25 #CHANGE LEVEL DIFICULTY
            #print('ITTTTTTTTTTTTTTTTTTTTT')
            pass
        elif self.level == 2:
            new_enemy.change_map()
        elif self.level == 3:
            new_enemy.change_map_3()
        elif self.level == 4:
            new_enemy.change_map_4()
        elif self.level == 5:
            new_enemy.change_map_5()
            
            #new_enemy.ship_speed = 0.5
        new_enemy.add_coordinates(self.myTank.rect.x, self.myTank.rect.y)
        for x,y in self.enemies_list_coordinate: 
            new_enemy.add_coordinates(x,y)
        #new_enemy.get_direction()
        #new_enemy.update() #????????????????
        
        #new_enemy.set_zero_coordinates()
        # return False if limit is out
        temp = new_enemy.right_coordinates()
        x = new_enemy.rect.x
        y= new_enemy.rect.y
        if temp != False:
            ###for enemy_update in self.enemies:
                ##enemy_update.add_coordinates(x, y)dd
            self.enemies_list_coordinate.append([x,y])
            #self.add_coordinates(x,y)
            self.enemies.add(new_enemy)
        
    def levels(self):
        if len(self.enemies) == 0 and self.level == 1:
        #print(dir(self.evil_bullets))# == 0:
            #print('WIN WIN')
            self.level = 2
            self.myTank.change_map()
            self.myTank.right_coordinates() # set new coordinates for my tank
            self.a_map.level_2_world_map()
            
            self.level_2()
            
        elif len(self.enemies) == 0 and self.level == 2:
        #print(dir(self.evil_bullets))# == 0:
            #print('WIN WIN')
            self.level = 3
            self.myTank.change_map_3()
            self.myTank.right_coordinates() # set new coordinates for my tank
            self.a_map.level_3_world_map()
            self.level_3()
            
        elif len(self.enemies) == 0 and self.level == 3:
        #print(dir(self.evil_bullets))# == 0:
            #print('WIN WIN')
            self.level = 4
            self.myTank.change_map_4()
            self.myTank.right_coordinates() # set new coordinates for my tank
            self.a_map.level_4_world_map()
            self.level_4()
            
        elif len(self.enemies) == 0 and self.level == 4:
        #print(dir(self.evil_bullets))# == 0:
            #print('WIN WIN')
            self.level = 5
            self.myTank.change_map_5()
            self.myTank.right_coordinates() # set new coordinates for my tank
            self.a_map.level_5_world_map()
            self.level_5()
            
        elif len(self.enemies) == 0 and self.level == 5:
            pass
            #print(dir(self.evil_bullets))
            #print('WIN WIN')
            #self.level_4()
            
     #restart game       
    def lose_or_win(self):
        if self.myTank.live == 0:
            self.stats.game_active = False 
            pygame.mouse.set_visible(True)
            pass
            #del self.myTank
        elif self.myTank.live > 0 and len(self.enemies) == 0 and self.level == 5:     # IF WIN  CHANGE LEVEL
            self.stats.game_active = False # IF WIN
            pygame.mouse.set_visible(True)   # IF WIN
            

    
    def _update_screen(self):
        self.screen.fill(self.settings.bgr_color)
        self.myTank.blitme()
        for x,y in self.a_map.world_map:
            self.rect.x = x
            self.rect.y = y
            self.screen.blit(self.image, self.rect)
            #pygame.draw.rect(self.screen, DARKGRAY, (x, y, TILE, TILE),2)
             
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        for bullet in self.evil_bullets.sprites():
            bullet.draw_bullet()
        
        #self.myEnemy.blitme()
        for enemy in self.enemies.sprites():
            enemy.blitme()
            
        if not self.stats.game_active and self.myTank.live == 0 :
            self.play_button.draw_button()
        if not self.stats.game_active and self.myTank.live > 0 and len(self.enemies) == 0 :
            self.win_button.draw_button()
            
        pygame.display.flip()       
    
    
    def run(self):
        #self.level = 1
        while(True):
            for i in range(100):
                #if not self.stats.game_active:
                self.lose_or_win()
                self._check_events()
                self.myTank.empty_coordinates_others()
                
                #animation of destroy and Delete
                if self.stats.game_active == True: # self.myTank.live > 0 or not winner
                    
                    self.levels()
                    for enemy in self.enemies:
                        #update coordinates into enemies and myTank
                        enemy.coordinates_others = []
                        self.myTank.coordinates_others = []
                        
                        for enemy_update in self.enemies:
                            enemy.add_coordinates(enemy_update.rect.x, enemy_update.rect.y)
                            enemy.add_coordinates(self.myTank.rect.x, self.myTank.rect.y)
                            
                            self.myTank.add_coordinates(enemy_update.rect.x, enemy_update.rect.y)
                        #live circle of enemy
                        if enemy.live == True and i == 0:
                            pass
                            enemy.rand_direction()
                            #enemy is shoting
                            self.fire_evil_bullets(enemy)
                        if i != 0:
                            if enemy.live == True and i%2  == 0 or i%3  == 0: # speed enemies added or i%3  == 0
                            #  print(f'i= {i}')# speed enemie3s
                                enemy.update()
                        
                        if enemy.live == False and i == 0:
                            self.enemies.remove(enemy)
                
                    self.myTank.update()
                    #self.bullets.update()
                    
                    for bullet in self.evil_bullets:
                        if (self.myTank.rect.x + self.myTank.SIZE >= bullet.x >= self.myTank.rect.x) and (self.myTank.rect.y + self.myTank.SIZE >= bullet.y >= self.myTank.rect.y):
                            #enemy.live = False
                                #self.enemies.remove(enemy)
                                print('You has been attacked')
                                self.myTank.live -= 1
                                self.evil_bullets.remove(bullet)
                            
                        #wall
                        if bullet.update():
                            self.evil_bullets.remove(bullet)
                        pass
                
                
                    # How to move and delete bullet
                    for bullet in self.bullets:
                        #FIRE FIRE FIRE to enemies
                        #step = True
                        for enemy in self.enemies:
                            if (enemy.rect.x + enemy.SIZE >= bullet.x >= enemy.rect.x) and (enemy.rect.y + enemy.SIZE >= bullet.y >= enemy.rect.y):
                                #step = False
                                enemy.live = False
                                #self.enemies.remove(enemy)
                                self.bullets.remove(bullet)
                        
                        #wall
                        temp = bullet.update()
                        if temp == True:
                            self.bullets.remove(bullet)
                
                self._update_screen()

            
        
if __name__ == '__main__':
    inv = Invasion()
    inv.run()
