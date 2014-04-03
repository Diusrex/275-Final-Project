import pygame
import game
import random

import menu
import tutorial
import drawFunctions
import scoreFunctions

from coordinate import Coordinate



def main(screen, screenSize):
    fileName = "scores.txt"
    highScores = scoreFunctions.LoadHighScores(fileName)

    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize, highScores)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, screenSize)
        
        elif decision == menu.playText:
            score = RunGame(screen, screenSize, highScores)
            
            # They wanted to exit
            if score == None:
                tryingToExit = True
            else:
                scoreFunctions.UpdateHighScores(screen, screenSize, score, highScores, fileName)
                scoreFunctions.ShowScoreScreen(screen, screenSize, score, highScores)
                
        else:
            tryingToExit = True

    
    
def RunGame(screen, screenSize, highScores):    
    """
    Will run the game
    """
    theGame = game.Game(screenSize, 30)
    theGame.SetUpNewGame()
    
    return theGame.RunUntilLoss(screen, highScores)
    





if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    screenSize = (1024, 650)
    screen = pygame.display.set_mode(screenSize)
    main(screen, screenSize)
    
    