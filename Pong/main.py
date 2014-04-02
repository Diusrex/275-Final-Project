import pygame
import random

import menu
import tutorial
import game

    
def main(screen, screenSize):
    highScores = LoadHighScores("scores.txt")
    
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, screenSize)
        
        elif decision == menu.playText:
            scoreInfo = game.RunGame(screen, screenSize)
            
            if scoreInfo == None:
                tryingToExit = True
            
            else: 
                ShowWinScreen(screen, screenSize, scoreInfo)
            
        else:
            tryingToExit = True
            
        

def ShowWinScreen(screen, screenSize, scoreInfo):
    """
    screen should already have the background set up
    """
    
    if scoreInfo.leftPlayerScore > scoreInfo.rightPlayerScore:
        winner = "first player"
    else:
        winner = "second player"
    
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 300
    posY = tutorial.WriteText(screen, screenSize, myfont, "Congratulations " + winner + " you have won!", posY, True)
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = tutorial.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return

        
    
    
if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    