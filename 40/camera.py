from settings import *
import pygame

class Camera(object):
    def __init__(self, camera_func,game):
        self.screen = game.screen
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT) # of level
	
    def apply(self, target): #move objects
        return target.rect.move(self.state.topleft)
    
    def apply_wall(self, rect): #move objects
        return rect.move(self.state.topleft)
    
    def update(self, target): #update camera
        self.state = self.camera_func(self.state, target.rect)
        #pygame.draw.rect(self.screen, DARKGRAY, self.state,2)
                
        
