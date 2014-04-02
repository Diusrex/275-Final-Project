import pygame
import game
import random

import menu
import tutorial
from coordinate import Coordinate



def main(screen, screenSize):
    highScores = LoadHighScores("scores.txt")

    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, screenSize)
        
        elif decision == menu.playText:
            score = RunGame(screen, screenSize)
            
            # They wanted to exit
            if score == None:
                tryingToExit = True
            else:
                ShowScoreScreen(screen, screenSize, score)
        else:
            tryingToExit = True

    
    
def RunGame(screen, screenSize):    
    """
    Will run the game
    """
    theGame = game.Game(screenSize, 30)
    theGame.SetUpNewGame()
    
    return theGame.RunUntilLoss(screen)

def LoadHighScores(file):
    #with file as open(file, 'r'):
    
    
def ShowScoreScreen(screen, screenSize, score):
    """
    Will overwrite the screen createdy by the game
    """
    
    # clear all of the events
    ev = pygame.event.get()
    
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 20
    posY = tutorial.WriteText(screen, screenSize, myfont, "Congratulations, you earned a score of " + str(score), posY, True)
    
    if score == 0:
        posY = tutorial.WriteText(screen, screenSize, myfont, "I'm sure you'll do better next time", posY, True)
    
    posY += 20
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = tutorial.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    # EDIT: Display all older high scores, and add option to add own high score?
    
    pygame.display.flip()
    
    
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return


if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    size = (1024, 650)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    