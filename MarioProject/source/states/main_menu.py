import pygame 
from .. import setup, tools
from .. import constants as C 
from ..components import info
class MainMenu:
    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'
        }
        self.start(game_info)

    def start(self, game_info):
        self.game_info = game_info
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu', self.game_info)
        self.finished = False
        self.next = 'load_screen'

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
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GRAPHICS['item_objects'], *C.CURSOR_ARGS)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = C.CURSOR_POS
        self.cursor.rect = rect
        self.cursor.state = '1P'
    
    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 365
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 410
        elif keys[pygame.K_RETURN]:
            self.reset_game_info()
            if self.cursor.state == '1P':
                self.finished = True
            elif self.cursor.state == '2P':
                self.finished = True

    
    
    def update(self, surface, keys):
        self.update_cursor(keys) 
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, self.caption_pos)  
        surface.blit(self.player_image, self.player_pos)
        surface.blit(self.cursor.image, self.cursor.rect)

        self.info.update()
        self.info.draw(surface)
    def reset_game_info(self):
        self.game_info['lives'] = 3