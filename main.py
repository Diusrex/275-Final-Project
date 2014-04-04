import pygame
import random

import menu
    
def main(screen, screenSize):
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.pongText:
            pass
        
        elif decision == menu.ticTacToeText:
            pass
            
        elif decision == menu.tetrisText:
            pass
            
        else:
            tryingToExit = True
            
    
    
if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    screenSize = (1024, 650)
    screen = pygame.display.set_mode(screenSize)
    main(screen, screenSize)
    
    