import pygame

import boxContainer

import menu
import game
import tutorial

import drawFunctions


# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3
    # This is for this game only

    
def main(screen, screenSize):
    wantsToExit = False
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, screenSize)
        
        elif decision == menu.playText:
            winner = game.RunGame(screen, screenSize)
            
            if winner == None:
                tryingToExit = True
            else:
                ShowWinScreen(screen, screenSize, winner)
            
        else:
            tryingToExit = True


                    
def ShowWinScreen(screen, screenSize, winner):
    """
    screen should already have the background set up
    """
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 20
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
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    