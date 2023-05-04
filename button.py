import pygame.font

class Button:
    
    def __init__(self,ai_game, msg):
        """Button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #dimension of button 
        self.width, self.height = 150,50
        self.button_color = (0,255,255)
        self.text_color = (255,255,255)
        self.font =pygame.font.SysFont(None,48)

        #builing the rect object and centering it. 
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #button message need to be done once.
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn msg into an image and center on the button"""
        self.msg_image = self.font.render(msg,True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)