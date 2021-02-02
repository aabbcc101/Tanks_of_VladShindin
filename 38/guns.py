import pygame

class Guns():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.gun1_Right = pygame.image.load('images/gun1.png')
        self.gun1_Left = pygame.image.load('images/gun1L.png')
        self.gun1R_fire = pygame.image.load('images/gun1_fire.png')
        self.gun1L_fire = pygame.image.load('images/gun1L_fire.png')
        
        
        self.rect =self.gun1_Right.get_rect()

    def draw(self,x,y, direction, fire):
        if direction == 'right' and fire == False:
            self.rect.x = x + 20
            self.rect.y = y + 55
            self.screen.blit(self.gun1_Right, self.rect)
        elif direction == 'left' and fire == False:
            self.rect.x = x - 20
            self.rect.y = y + 55    
            self.screen.blit(self.gun1_Left, self.rect)
        elif direction == 'right' and fire == True:
            self.rect.x = x + 20
            self.rect.y = y + 55
            self.screen.blit(self.gun1R_fire, self.rect)
        elif direction == 'left' and fire == True:
            self.rect.x = x - 20
            self.rect.y = y + 55    
            self.screen.blit(self.gun1L_fire, self.rect)
            
