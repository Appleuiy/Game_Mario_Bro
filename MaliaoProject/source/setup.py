import pygame
from . import constants as C
from . import tools

pygame.init()
pygame.display.set_mode(C.SCREEN_SIZE)

GRAPHICS = tools.load_graphics('resources/graphics')
