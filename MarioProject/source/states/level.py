from ..components import info
from .. import tools, setup
from .. import constants as C 
from ..components import player, stuff
import pygame, json, os



class Level:
    def __init__(self):
        self.finished = False
        self.next = 'game_over'
        self.info = info.Info('level')
        self.load_map_data()
        self.setup_background()
        self.setup_start_positions()
        self.setup_player()
        self.setup_ground_items()
    
    def setup_ground_items(self):
        self.ground_items_group = pygame.sprite.Group()
        for name in ['ground', 'pipe', 'step']:
            for item in self.map_data[name]:
                self.ground_items_group.add(stuff.Item(item['x'], item['y'], item['width'], item['height'], name))

    
    def load_map_data(self):
        file_name = 'level_1.json'
        file_path = os.path.join('source/data/maps', file_name)
        with open(file_path) as f:
            self.map_data = json.load(f)



    def setup_start_positions(self):
        self.positions = []
        for data in self.map_data['maps']:
            self.positions.append((data['start_x'], data['end_x'], data['player_x'], data['player_y']))
        self.start_x, self.end_x, self.player_x, self.player_y = self.positions[0]
    
    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(rect.width * C.BG_MULTI),
                                                                   int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()
        self.game_window = setup.SCREEN.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = self.game_window.x + self.player_x
        self.player.rect.bottom = self.player_y

    def update(self, surface, keys):
        self.current_time = pygame.time.get_ticks()
        self.player.update(keys)

        if self.player.dead:
            if self.current_time - self.player.death_timer > 3000:
                self.finished = True
        else:
            self.update_player_position()
            self.update_game_window()
            self.check_if_go_die()
        
        self.draw(surface)

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        

        # x direction
        if self.player.rect.x < self.game_window.x:
            self.player.rect.x = self.game_window.x
        elif self.player.rect.right > self.end_x:
            self.player.rect.right = self.end_x

        self.check_x_collisions()

        # # y direction
        self.player.rect.y += self.player.y_vel
        self.check_y_collisions()

    def check_x_collisions(self):
        ground_item = pygame.sprite.spritecollideany(self.player, self.ground_items_group)
        if ground_item:
            self.adjust_player_x(ground_item)

    def adjust_player_x(self, sprite):
        if self.player.rect.x < sprite.rect.x:
            self.player.rect.right = sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_vel = 0

    def check_y_collisions(self):
        ground_item = pygame.sprite.spritecollideany(self.player, self.ground_items_group)
        if ground_item:
            self.adjust_player_y(ground_item)
        
        self.check_will_fall(self.player)

    def check_will_fall(self, sprite):
        sprite.rect.y += 1
        check_group = pygame.sprite.Group(self.ground_items_group)
        collied = pygame.sprite.spritecollideany(sprite, check_group)
        if not collied and sprite.state != 'jump':
            sprite.state = 'fall'
        sprite.rect.y -= 1 

    def adjust_player_y(self, sprite):
        # downwards
        if self.player.rect.bottom < sprite.rect.bottom:
            self.player.y_vel = 0
            self.player.rect.bottom = sprite.rect.top
            self.player.state = 'walk'
        # upwards
        else:
            self.player.y_vel = 7
            self.player.rect.top = sprite.rect.bottom
            self.player.state = 'fall'
        

    def update_game_window(self):
        third = self.game_window.x + self.game_window.width / 3
        if self.player.x_vel > 0 and self.player.rect.x > third and self.game_window.right < self.end_x:
            self.game_window.x += self.player.x_vel
        if self.game_window.right > self.end_x:
            self.game_window.right = self.end_x

    def draw(self, surface):
        self.game_ground.blit(self.background, self.game_window, self.game_window)
        self.game_ground.blit(self.player.image, self.player.rect)
        surface.blit(self.game_ground, (0, 0), self.game_window)
        
        self.info.update()
        self.info.draw(surface)


    def check_if_go_die(self):
        if self.player.rect.y > C.SCREEN_HEIGHT:
            self.player.go_die()