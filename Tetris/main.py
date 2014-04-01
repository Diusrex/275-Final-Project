import pygame
import game
import random

import menu

from coordinate import Coordinate



def main(screen, size):
    decision = menu.RunMenu(screen, size)
    
    if decision == menu.tutorialText:
        RunTutorial(screen, size)
    
    elif decision == menu.playText:
        RunGame(screen, size)

    

    
    
def RunGame(screen, size):    
    """
    Will run the game
    """
    theGame = game.Game(size, 30)
    theGame.SetUpNewGame()
    theGame.RunUntilLoss(screen)
    
    



if __name__ == "__main__":
    random.seed()
    
    pygame.init()
    size = (1024, 650)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    