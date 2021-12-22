import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """Init button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and props
        self.width, self.height = 200, 50
        self.button_color = (100,100,100)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button msg needs to be prepped once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered image and center text"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
