import pygame
from source import tools, setup
from source.states import main_menu, level, load_screen

def main():
    
    state_dict = {
        'main_menu' : main_menu.MainMenu(),
        'load_screen' : load_screen.LoadScreen(),
        'level' : level.Level(),
        'game_over': load_screen.GameOver()
    }
    game = tools.Game(state_dict, 'level')
    # state = main_menu.MainMenu()
    # state = level.Level();
    # state = load_screen.LoadScreen()
    game.run()


if __name__ == '__main__':
    main()   