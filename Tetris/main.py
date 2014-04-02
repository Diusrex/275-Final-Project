import pygame
import game
import random

import menu
import tutorial
from coordinate import Coordinate



def main(screen, size):
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, size)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, size)
        
        elif decision == menu.playText:
            score = RunGame(screen, size)
            
            # They wanted to exit
            if score == None:
                tryingToExit = True
            else:
                ShowScoreScreen(screen, size, score)
        else:
            tryingToExit = True

    
    
def RunGame(screen, size):    
    """
    Will run the game
    """
    theGame = game.Game(size, 30)
    theGame.SetUpNewGame()
    theGame.RunUntilLoss(screen)

    
def ShowScoreScreen(screen, size, score):
    """
    Will overwrite the screen createdy by the game
    """
    screen.fill((0, 0, 0))



if __name__ == "__main__":
    random.seed()
    
    pygame.init()
    size = (1024, 650)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    