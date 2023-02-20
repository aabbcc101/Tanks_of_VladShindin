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
from lives import Lives
from score import Score
from title import Title
from help_ import Help
import time
#from aid import Aid

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
        temp_color = (0, 100, 0)
        temp_text_color =(255, 255, 255)
        self.play_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "PLAY")
        self.play_button.rect.y -= 65
        self.play_button._prep_msg("NEW GAME")
        
        
        temp_x, temp_y = 200, 50
        temp_color = (20, 40, 0)
        temp_text_color =(255, 255, 255)
        self.exit_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "EXIT")
        self.exit_button.rect.y += 185
        self.exit_button._prep_msg("EXIT")
        
        temp_x, temp_y = 200, 50
        temp_color = (80, 60, 0)
        temp_text_color =(255, 255, 255)
        self.title_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "TITLE")
        self.title_button.rect.y += 125
        self.title_button._prep_msg("TITLE")
        self.title = Title(self)
        self.title_active = False
        
        temp_x, temp_y = 200, 50
        temp_color = (150, 200, 0)
        temp_text_color =(255, 255, 255)
        self.help_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "HELP")
        self.help_button.rect.y += 65
        self.help_button._prep_msg("HELP")
        self.help_ = Help(self)
        self.help_active = False
        
        temp_x, temp_y = 200, 50
        temp_color = (150, 200, 0)
        temp_text_color =(255, 255, 255)
        self.back_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "BACK")
        self.back_button.rect.y += 185
        self.back_button._prep_msg("BACK")

        
        
        temp_x, temp_y = 250, 50
        temp_color = (0, 240, 0)
        temp_text_color =(255, 255, 255)
        self.restart_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "Restart level")
        
        temp_x, temp_y = 350, 50
        temp_color = (100, 100, 100)
        temp_text_color =(255, 0, 0)
        self.win_button = Button(self, temp_x, temp_y, temp_color, temp_text_color, "YOU ARE A WINNER!")
        
        self.myTank = Ship(self)
        self.myTank.live  = 0
        
        #interface
        self.liveboard = Lives(self)
        self.score = 0
        self.scoreboard = Score(self)

        self.image = pygame.image.load('images/brick_wall3.png')        
        self.rect = self.image.get_rect()
        
        self.aid = pygame.image.load('images/aid.png')   

    def delete_all_bullets(self):
        self.evil_bullets.empty()
        self.bullets.empty()

        
    def level_1(self):
        self.level = 1
        #show lives
        self.liveboard.prepare(self)
        
        # destroyd enemies
        self.score = 0
        self.scoreboard.prepare(self)
        
        self.a_map.create_map() #create a map 1
        self.delete_all_bullets()
        #self.myTank.out_coordinates = []
        self.myTank.create_map() #create a map 
        self.myTank.right_coordinates() # set new coordinates

        #self.myEnemy = Enemy(self)
        #print('LEVEL 111111111111111111111111111111') doNE

        self.enemies_list_coordinate = [] 
        
                
        for i in range(15): #20
            #self.create_an_enemy()
            self.create_an_enemy2()
                    #add coordianates

        self.settings.bgr_color = WHITE 
        self.image = pygame.image.load('images/brick_wall3.png')  
        #self.image = pygame.image.load('images/brick_wall.png')
 
    def level_2(self):
        self.delete_all_bullets()
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall2.png')
        self.enemies_list_coordinate = [] 
        for i in range(6): # 10 9
            #self.create_an_enemy()
            self.create_an_enemy2()

        
    def level_3(self):
        self.delete_all_bullets()
        
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall.png')
        self.enemies_list_coordinate = [] 
        for i in range(10): #12
            #self.create_an_enemy()
            self.create_an_enemy2()
            
            
    def level_4(self):
        self.delete_all_bullets()
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall2.png')
        self.enemies_list_coordinate = [] 
        for i in range(8): #10 15
            #self.create_an_enemy()
            self.create_an_enemy2()

        
    def level_5(self):
        self.delete_all_bullets()
        
        self.settings.bgr_color = LIGHTGRAY
        self.image = pygame.image.load('images/brick_wall.png')
        self.enemies_list_coordinate = [] 
        for i in range(10): #10 17
            #self.create_an_enemy()
            self.create_an_enemy2()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_exit_button(mouse_pos)
                self._check_title_button(mouse_pos)
                self._check_help_button(mouse_pos)
                self._check_restart_button(mouse_pos)
                self._check_back_button(mouse_pos)
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
                if event.key == pygame.K_r:
                    self._check_restart()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.myTank.moving_right = False 
                if event.key == pygame.K_LEFT:
                    self.myTank.moving_left = False
                if event.key == pygame.K_UP:
                    self.myTank.moving_up = False 
                if event.key == pygame.K_DOWN:
                    self.myTank.moving_down = False

    def _check_exit_button(self,mouse_pos):
        if self.exit_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            sys.exit()
                    
    def _check_enter(self):
        self.enemies.empty()
        self.stats.game_active = True
        self.myTank.live  = LIVE_OF_TANK
        self.level_1()
        pygame.mouse.set_visible(False)
        
    def _check_restart(self):
        if self.level == 0:
            return 0
        self.enemies.empty()
        self.stats.game_active = True
        self.myTank.live  = LIVE_OF_TANK
        #show lives
        self.liveboard.prepare(self)
        
        # destroyd enemies
        self.score = 0
        self.scoreboard.prepare(self)
        if self.level == 1:
            self.level_1()
        elif self.level == 2:
            self.level_2()
        elif self.level == 3:
            self.level_3()
        elif self.level == 4:
            self.level_4()
        elif self.level == 5:
            self.level_5()
        pygame.mouse.set_visible(False)

    def _check_restart_button(self,mouse_pos):
        if self.restart_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            if self.level == 0:
                return 0
            self.enemies.empty()
            self.stats.game_active = True
            self.myTank.live  = LIVE_OF_TANK
            #show lives
            self.liveboard.prepare(self)
            
            # destroyd enemies
            self.score = 0
            self.scoreboard.prepare(self)
            if self.level == 1:
                self.level_1()
            elif self.level == 2:
                self.level_2()
            elif self.level == 3:
                self.level_3()
            elif self.level == 4:
                self.level_4()
            elif self.level == 5:
                self.level_5()
            pygame.mouse.set_visible(False)
            
    def _check_title_button(self, mouse_pos):
        if self.title_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            self.title_active = True
            pygame.mouse.set_visible(False)
            
    def _check_help_button(self, mouse_pos):
        if self.help_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            self.help_active = True
            
            #pygame.mouse.set_visible(False)
            
    def _check_back_button(self, mouse_pos):
        if self.back_button.rect.collidepoint(mouse_pos) and self.help_active == True and not self.stats.game_active: # invisible button musnt be worked
            self.help_active = False
            #pygame.mouse.set_visible(False)
 
    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and self.myTank.live  == 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            self.enemies.empty()
            self.stats.game_active = True
            self.myTank.live  = LIVE_OF_TANK
            self.level_1()
            pygame.mouse.set_visible(False)
            #print(dir(self.enemies))
            
    def _check_win_button(self,mouse_pos):
        if self.win_button.rect.collidepoint(mouse_pos) and self.myTank.live  > 0 and not self.stats.game_active and not self.help_active: # invisible button musnt be worked
            self.enemies.empty()
            self.stats.game_active = True
            self.myTank.live  = LIVE_OF_TANK
            self.level_1()
            pygame.mouse.set_visible(False)
                    
    def fire_bullets(self):
        if len(self.bullets) <= BULLET_LIMIT: #my fire limit
            new_bullet = Bullet(self, self.myTank.direction,self.level)
            self.bullets.add(new_bullet)
        
    def fire_evil_bullets(self,enemy):
        new_bullet = Evil_bullet(self, enemy.rect.x, enemy.rect.y, enemy.direction,self.level)
        self.evil_bullets.add(new_bullet)
    
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
        
        #for temp in self.a_map.aid_list:
            #new_enemy.(temp[0],temp[1])
        
        for x,y in self.enemies_list_coordinate: 
            new_enemy.add_coordinates(x,y)
            
 
            
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
        
        for row in self.a_map.world_map_list: # CAN I update this one?
            for x,y in row:
                self.rect.x = x
                self.rect.y = y
                self.screen.blit(self.image, self.rect)
            #pygame.draw.rect(self.screen, DARKGRAY, (x, y, TILE, TILE),2)

        #for bullet in self.bullets.sprites():
            #bullet.draw_bullet()
            
        #for bullet in self.evil_bullets.sprites():
            #bullet.draw_bullet()
        
        #self.myEnemy.blitme()
        #for enemy in self.enemies.sprites():
            #enemy.blitme()

        if not self.stats.game_active and self.myTank.live == 0 :
            self.play_button.draw_button()
            self.restart_button.draw_button()
            self.help_button.draw_button()
            self.title_button.draw_button()
            self.exit_button.draw_button()

        if self.title_active == True:
            self.title.draw_title()
            pygame.display.flip()   #SHOW ALL update_screen
            time.sleep(2)
            self.title_active = False
            
        if self.help_active == True:
            self.help_.draw_title()
            self.back_button.draw_button()
            pygame.display.flip()   #SHOW ALL update_screen
            #time.sleep(3)
            #self.help_active = False
        else:
            self.liveboard.draw()
            self.scoreboard.draw()
            
            
        if not self.stats.game_active and self.myTank.live > 0 and len(self.enemies) == 0 :
            self.win_button.draw_button()
            
            
        #pygame.display.flip()       
    
    
    def run(self):
        #self.level = 1
        while(True):
            for i in range(100):
                #if not self.stats.game_active:
                self.lose_or_win()
                self._check_events()
                self.myTank.empty_coordinates_others()
                
                #self.liveboard.prepare()
                
                #SHOW ALL update_screen
                self._update_screen()          
                               
                
                #animation of destroy and Delete
                if self.stats.game_active == True: #or self.stats.game_active == True: # self.myTank.live > 0 or not winner
                    #for temp in self.a_map.aid_list:
                        #print(temp[0],temp[1])                            
                    self.levels()
                    
                    
                    for enemy in self.enemies:
                        #update coordinates into enemies and myTank
                        enemy.coordinates_others = []
                        self.myTank.coordinates_others = []
                        
                        #for temp in self.a_map.aid_list:
                            #self.myTank.add_coordinates(temp[0],temp[1])
                            #print(temp[0],temp[1])
                        
                        for enemy_update in self.enemies:
                            enemy.add_coordinates(enemy_update.rect.x, enemy_update.rect.y)
                            enemy.add_coordinates(self.myTank.rect.x, self.myTank.rect.y)
                            
                            for temp in self.a_map.aid_list:
                                enemy.add_coordinates(temp[0],temp[1])
                                
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
                            self.score += 1
                            self.scoreboard.prepare(self)
                            self.enemies.remove(enemy)
                            
                    #SHOW ALL update_screen
                        enemy.blitme()
                    
                    #for in 
                    if len(self.a_map.aid_list) != 0:
                        myTank_rightTopX = self.myTank.rect.x  + self.myTank.SIZE
                        myTank_lefttBottomY  = self.myTank.rect.y  + self.myTank.SIZE
                        #temp = 0
                        for a in self.a_map.aid_list:
                            x = a[0]
                            y = a[1]
                            self.rect.x = x
                            self.rect.y = y
                            rightTopX = x + 31
                            lefttBottomY = y + 31
                            if (rightTopX >= myTank_rightTopX >= x) and (lefttBottomY >= self.myTank.rect.y >= y) or (rightTopX >= myTank_rightTopX >= x) and (lefttBottomY >= myTank_lefttBottomY >= y) or (rightTopX >= self.myTank.rect.x >= x) and (lefttBottomY >= myTank_lefttBottomY >= y) or (rightTopX >= self.myTank.rect.x >= x) and (lefttBottomY >= self.myTank.rect.y >= y):
                                #temp += 2    ################???????????????????????????
                                self.a_map.aid_list.remove(a)
                                #temp += 2
                                self.myTank.live += 2
                                self.liveboard.prepare(self)
                            #break
                            else:
                                self.screen.blit(self.aid, self.rect)

                    
                    self.myTank.update()
                    #self.bullets.update()
                    
                    for bullet in self.evil_bullets.sprites():
                        if (self.myTank.rect.x + self.myTank.SIZE >= bullet.x >= self.myTank.rect.x) and (self.myTank.rect.y + self.myTank.SIZE >= bullet.y >= self.myTank.rect.y):
                            #enemy.live = False
                                #self.enemies.remove(enemy)
                                print('You has been attacked')
                                self.myTank.live -= 1
                                        #show lives
                                self.liveboard.prepare(self)
                                self.evil_bullets.remove(bullet)
                            
                        #wall
                        if bullet.update():
                            self.evil_bullets.remove(bullet)
                        else:
                            bullet.draw_bullet()      #SHOW ALL update_screen          
                
                    # How to move and delete bullet
                    for bullet in self.bullets.sprites():
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
                        else:
                            bullet.draw_bullet()    #SHOW ALL update_screen
                    
                    
                    
                pygame.display.flip()   #SHOW ALL update_screen
                    #for bullet in self.bullets.sprites():
                        #bullet.draw_bullet()                


            
        
if __name__ == '__main__':
    inv = Invasion()
    inv.run()
