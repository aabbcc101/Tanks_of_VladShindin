import pygame
#from map import world_map
from map import World_map
from settings import*
import random

class Ship():
    def __init__(self, game):
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.a_map = World_map()
        
        self.image = pygame.image.load('images/greenBattle32.png')
        self.imageLeft = pygame.image.load('images/greenBattleLeft32.png')
        self.imageRight = pygame.image.load('images/greenBattleRight32.png')
        self.imageDown = pygame.image.load('images/greenBattleDown32.png')
        self.imageExplode = pygame.image.load('images/shotRed32.png')
        # for images
        self.direction = 'up'
        #self.live = True
        
        self.rect =self.image.get_rect()
        
        self.SIZE = 32
        
        #start coordinates
        self.rect.topleft = self.screen_rect.topleft
        self.rect.x += 52
        self.rect.y += 52
        
        #temporary
        self.rightTop = [self.rect.x + self.SIZE, self.rect.y]
        self.rightBottom = [self.rect.x + self.SIZE, self.rect.y + self.SIZE]
        self.lefttBottom = [self.rect.x, self.rect.y + self.SIZE]
 
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.ship_speed = 1.5
        self.live = 3
        
        self.out_coordinates = []
        self.coordinates_others = []

    def create_map(self):
        self.out_coordinates = []
        self.coordinates_others = []
        self.a_map.create_map()
        
    def change_map(self):
        self.a_map.level_2_world_map()
        #print ('IT ITTTTTTTTTTTTTTTTTTTTTTTTTTTTsdsdsds')
        
    def change_map_3(self):
        self.a_map.level_3_world_map()
        
    def change_map_4(self):
        self.a_map.level_4_world_map()
        
    def change_map_5(self):
        self.a_map.level_5_world_map()
        
    def empty_coordinates_others(self):
        self.coordinates_others = []
        
    def add_coordinates(self,x,y):
        self.coordinates_others.append([x,y])
     
    def random_coordinates(self):
        list_x = [ x for x in range(0, self.settings.screen_width,self.SIZE)]
        list_y = [ y for y in range(0, self.settings.screen_height,self.SIZE)]   
        self.rect.x = random.choice(list_x)
        self.rect.y = random.choice(list_y)
        if len(self.out_coordinates) < self.a_map.space:
            for x, y in self.out_coordinates: # checked space not to do
                if self.rect.x == x and self.rect.y  == y:
                    self.random_coordinates()

    # creating a tank into empy place
    def right_coordinates(self):
        for i in range(500): #while does not needed
            if i < self.a_map.space: # chack every space in a map
                if self.apear_coordinates():
                    self.out_coordinates.append((self.rect.x, self.rect.y)) # checked space
                    #self.rect.x = 0 #test
                    #self.rect.y = 0 #test
                    pass
                else:
                    print('ELSE')
                    return True
            else:
                print('limit is out')
                return False
        return False  # important tanks have to be into a map
            

    def apear_coordinates(self):
               
        self.random_coordinates()
        #print(f'x = {self.rect.x} y = {self.rect.y}')
        
        
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        
        # walls
        
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            # left top
            if (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            # right top
            elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            # left bottom
            elif (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
            # right bottom
            elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
            
            #coordinates_others

        for x, y in self.coordinates_others: #I need to add my Tank into enemy
            if self.rect.x == x and self.rect.y == y:
                return True
            
            # the same thing But a little harder 
            #rightTopX = x + self.SIZE
            #lefttBottomY = y + self.SIZE   
            ## left top
            #if (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.rect.y >= y):
                #return True
            ## right top
            #elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.rect.y >= y):
                #return True
            ## left bottom
            #elif (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                #return True
            ## right bottom
            #elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                #return True
            
        return False   
            

    def check_coordinates_right(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        
        for x, y in self.coordinates_others:
            rightTopX = x + self.SIZE
            lefttBottomY = y + self.SIZE
            if (rightTopX >= self.rightTopX+self.ship_speed >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rightTopX+self.ship_speed >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
        return False
        
    def check_coordinates_top(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        
        for x, y in self.coordinates_others:
            rightTopX = x + self.SIZE
            lefttBottomY = y + self.SIZE
            if (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.rect.y-self.ship_speed >= y):
                return True
            elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.rect.y-self.ship_speed >= y):
                return True
        return False
            
            
    def check_coordinates_left(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        
        for x, y in self.coordinates_others:
            rightTopX = x + self.SIZE
            lefttBottomY = y + self.SIZE
            if (rightTopX >= self.rect.x-self.ship_speed >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rect.x-self.ship_speed >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True 
        return False
            
    def check_coordinates_bottom(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        
        for x, y in self.coordinates_others:
            rightTopX = x + self.SIZE
            lefttBottomY = y + self.SIZE
            if (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.lefttBottomY+self.ship_speed >= y):
                return True
            elif (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.lefttBottomY+self.ship_speed >= y):
                return True
        return False

        
    def check_top_wall(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.rect.y-self.ship_speed >= y):
                return True
            elif (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.rect.y-self.ship_speed >= y):
                return True
   
        return False
    
    def check_left_wall(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rect.x-self.ship_speed >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rect.x-self.ship_speed >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
        return False
    
    def check_right_wall(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rightTopX+self.ship_speed >= x) and (lefttBottomY >= self.rect.y >= y):
                return True
            elif (rightTopX >= self.rightTopX+self.ship_speed >= x) and (lefttBottomY >= self.lefttBottomY >= y):
                return True
        return False
    
    def check_bottom_wall(self):
        self.rightTopX = self.rect.x + self.SIZE
        self.lefttBottomY = self.rect.y + self.SIZE
        for x,y in self.a_map.world_map:
            rightTopX = x + TILE
            lefttBottomY = y + TILE
            
            if (rightTopX >= self.rightTopX >= x) and (lefttBottomY >= self.lefttBottomY+self.ship_speed >= y):
                return True
            elif (rightTopX >= self.rect.x >= x) and (lefttBottomY >= self.lefttBottomY+self.ship_speed >= y):
                return True
        return False
        
        
    def blitme(self):
        if self.direction == 'up':
            self.screen.blit(self.image, self.rect)
        elif self.direction == 'left':
            self.screen.blit(self.imageLeft, self.rect)
        elif self.direction == 'right':
            self.screen.blit(self.imageRight, self.rect)
        elif self.direction == 'down':
            self.screen.blit(self.imageDown, self.rect)
        if self.live == False:
            self.screen.blit(self.imageExplode, self.rect)
            
        
    def update(self):
        
        if self.moving_down:
            if self.check_bottom_wall() == False and self.check_coordinates_bottom() == False:
                self.rect.y += self.ship_speed 
                self.direction = 'down'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'down'
        elif self.moving_up:
            if self.check_top_wall() == False and self.check_coordinates_top() == False:
                self.rect.y -= self.ship_speed
                self.direction = 'up'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'up'
                
        elif self.moving_left:
            if self.check_left_wall() == False and self.check_coordinates_left() == False:
                self.rect.x -= self.ship_speed 
                self.direction = 'left'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'left'
        elif self.moving_right:
            if self.check_right_wall() == False and self.check_coordinates_right() == False:
                self.rect.x += self.ship_speed
                self.direction = 'right'
                #print(self.rect.x, self.rect.y)
            else:
                self.direction = 'right'
            
        
      
