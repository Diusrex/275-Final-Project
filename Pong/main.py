import pygame
import random

# Use these imports if running from base menu
import Pong.menu as menu
import Pong.tutorial as tutorial
import Pong.game as game
import Pong.drawFunctions as drawFunctions

"""
Use these imports if only running this game.

import menu
import tutorial
import game
import drawFunctions
"""


def Main(screen, screenSize):
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
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Congratulations " + winner + " you have won!", posY, True)
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return

        
    
    
if __name__ == "__main__":
    pygame.init()
    random.seed()
    
    screenSize = (1024, 650)
    screen = pygame.display.set_mode(screenSize)
    Main(screen, screenSize)
    
    