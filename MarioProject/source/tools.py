# 工具和游戏主题

import pygame 
import random 
import os

wide, height = 800, 600

class Game:
    def __init__(self, state_dict, start_state ):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]
    
    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False 
            self.state  = self.state_dict[next_state]
        self.state.update(self.screen, self.keys)

    def run(self):
       
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            # self.screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            # image = get_image(GRAPHICS['mario_bros'], 145, 32, 16, 16, (0,0,0), random.randint(5,15))
            # self.screen.blit(image, (300,300))
            
            self.update()
            pygame.display.update()
            self.clock.tick(60)

def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.git')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img 
    return graphics

def get_image(sheet, x, y, width, height, colorkey, scale):
    img = pygame.Surface((width, height))
    img.blit(sheet, (0,0), (x,y,width,height))
    img.set_colorkey(colorkey)
    img = pygame.transform.scale(img, (int(width*scale), int(height*scale)))
    return img 