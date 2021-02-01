import pygame
from pygame.sprite import Sprite 

class Aid(Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/aid.png')  
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
