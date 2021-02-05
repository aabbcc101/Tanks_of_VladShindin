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

    def draw(self,new_rect, direction, fire):
        if direction == 'right' and fire == False:
            new_rect.x += 20
            new_rect.y += 55
            self.screen.blit(self.gun1_Right, new_rect)
        elif direction == 'left' and fire == False:
            new_rect.x -= 20
            new_rect.y += 55    
            self.screen.blit(self.gun1_Left, new_rect)
        elif direction == 'right' and fire == True:
            new_rect.x += 20
            new_rect.y += 55
            self.screen.blit(self.gun1R_fire, new_rect)
        elif direction == 'left' and fire == True:
            new_rect.x -= 20
            new_rect.y += 55    
            self.screen.blit(self.gun1L_fire, new_rect)
            
