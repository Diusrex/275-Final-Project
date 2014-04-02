import pygame

import menu
import tutorial
import game

from player import Player

    
def main(screen, size):
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, size)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, size)
        
        elif decision == menu.playText:
            scoreInfo = game.RunGame(screen, size)
            
            if scoreInfo == None:
                tryingToExit = True
            
            else: 
                ShowWinScreen(screen, size, scoreInfo)
            
        else:
            tryingToExit = True
            
        

def ShowWinScreen(screen, size, scoreInfo):
    """
    screen should already have the background set up
    """
    
    if scoreInfo.leftPlayerScore > scoreInfo.rightPlayerScore:
        winner = "first player"
    else:
        winner = "second player"
    
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 300
    posY = tutorial.WriteText(screen, size, myfont, "Congratulations " + winner + " you have won!", posY, True)
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = tutorial.WriteText(screen, size, myfont, "Press any button to return to the main menu", posY, True)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return
    
if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    