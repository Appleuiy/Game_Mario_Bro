import pygame 
from .. import setup, tools
from .. import constants as C 
from ..components import info
class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')


    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect() 
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * C.BG_MULTI), int(self.background_rect.height * C.BG_MULTI)))
        
        self.viewport = setup.SCREEN.get_rect()

        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], *C.CAPTION_ARGS)
        self.caption_pos = C.CAPTION_POS

    def setup_player(self):
        self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'],*C.PLAYER_ARGS)
        self.player_pos = C.PLAYER_POS
    def setup_cursor(self):
        self.cursor = tools.get_image(setup.GRAPHICS['item_objects'], *C.CURSOR_ARGS)
        self.cursor_pos = C.CURSOR_POS
    def update(self, surface):
        
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, self.caption_pos)  
        surface.blit(self.player_image, self.player_pos)
        surface.blit(self.cursor, self.cursor_pos)



        self.info.update()
        self.info.draw(surface)
    