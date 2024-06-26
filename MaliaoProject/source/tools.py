# 工具和游戏主题

import pygame 
import random 
import os

wide, height = 800, 600

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
    def run(self, GRAPHICS):
       
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            image = get_image(GRAPHICS['mario_bros'], 145, 32, 16, 16, (0,0,0), random.randint(5,15))
            self.screen.blit(image, (300,300))
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