import pygame

import random

# Use these imports when running the main program (not individual games)

scorefilePath = "Tetris/scores.txt"

import Tetris.menu as menu
import Tetris.tutorial as tutorial
import Tetris.scoreFunctions as scoreFunctions
import Tetris.game as game
 
"""
# Use these imports when running the game individually

scorefilePath = "scores.txt"

import menu
import tutorial
import scoreFunctions
import game
"""

def Main(screen, screenSize):
    
    highScores = scoreFunctions.LoadHighScores(scorefilePath)

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
                scoreFunctions.UpdateHighScores(screen, screenSize, score, highScores, scorefilePath)
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
    
    