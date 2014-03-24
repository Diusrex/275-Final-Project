import pygame
import random

import menu

import Pong.main
import Tetris.main
import TicTacToe.main
import MineSweeper.main
    
def main(screen, screenSize):
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.pongText:
            Pong.main.Main(screen, screenSize)
        
        elif decision == menu.tetrisText:
            Tetris.main.Main(screen, screenSize)
            
        elif decision == menu.ticTacToeText:
            TicTacToe.main.Main(screen, screenSize)

        elif decision == menu.mineSweeperText:
            MineSweeper.main.Main(screen, screenSize)
            
        else:
            tryingToExit = True
            
    
    
if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    screenSize = (1024, 650)
    screen = pygame.display.set_mode(screenSize)
    main(screen, screenSize)
    
    
