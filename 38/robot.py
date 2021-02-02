import pygame
from settings import*

class Robot():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.imageRight1 = pygame.image.load('images/bender5_4_R.png')
        self.imageRight2 = pygame.image.load('images/bender5_4.png')
        self.imageLeft1 = pygame.image.load('images/bender5_4L.png')
        self.imageLeft2 = pygame.image.load('images/bender5_4LR.png')
        self.imageLeftF = pygame.image.load('images/bender5_4LR-F.png')
        self.imageRightF = pygame.image.load('images/bender5_4RR-F.png')
        
        self.direction = 'right'
        self.step_direction = 'right'
        self.moving_left = False
        self.moving_right = False
        self.jump_activate = 0
        self.jump_act = False
        self.jump_up = False
        self.height_jump = 20 # 5 * 20 = 100 pixel
        self.speed = 5
        self.size_of_jump = 10
        self.shot_f = False
        
        self.live = True
        
        self.rect =self.imageRight2.get_rect()
        
                #start coordinates
        self.rect.topleft = self.screen_rect.topleft
        self.rect.x = 452
        self.rect.y = 250
 
        self.Y_HEIGHT = 120
        self.X_WIGHT = 50
         
        self.real_x = self.rect.x
        self.real_y = self.rect.y   
        
    def bore(self):
        if self.jump_up == False and self.jump_activate == 0 and self.shot_f == False:
            if self.step_direction == 'right':
                self.step_direction = 'left'
            elif self.step_direction =='left':
                self.step_direction = 'right'
                
            
    def jump(self):
        if self.jump_up == False and self.jump_activate == 0:
            self.jump_up = True
            self.jump_act = True

            
        
        
    def blitme(self):
        if self.shot_f == True and self.direction == 'right':
            self.screen.blit(self.imageRightF, self.rect)
        elif self.shot_f == True and self.direction == 'left':
            self.screen.blit(self.imageLeftF, self.rect)
        if self.shot_f == False:
            if self.direction == 'right':
                if self.step_direction == 'left':
                    self.screen.blit(self.imageRight2, self.rect)
                    #self.step_direction = 'right'
                elif self.step_direction == 'right':
                    self.screen.blit(self.imageRight1, self.rect)
                    #self.step_direction = 'left'
            elif self.direction == 'left':
                if self.step_direction == 'left':
                    self.screen.blit(self.imageLeft2, self.rect)
                elif self.step_direction == 'right':
                    self.screen.blit(self.imageLeft1, self.rect)
                   
        #if self.live == False:
            #self.screen.blit(self.imageExplode, self.rect)
