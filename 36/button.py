import pygame.font

class Button():
    def __init__(self,game, x, y, color, color_of_text, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        #sizes
        self.wight, self.height = x,y #200,50
        self.button_color = color   #(0, 255, 0)
        self.text_color = color_of_text  #(255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #build and set whereabouts
        
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = self.screen_rect.center
        
        #create message only one time
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        
        
