import pygame
import random
import button

# Use these imports if running from base menu
from Tetris.drawFunctions import WriteText

"""
# Use these imports if running this game alone
from drawFunctions import WriteText
"""

name = "Tetris"

def RunTutorial(screen, screenSize):
    """
    Will display the tutorial/information needed for the user to be able to play properly.
    
    Will return True if the user wanted to go to the menu, otherwise will return False (and thus wants to exit)
    """
    # Only need to draw once, because the screen will not change after
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 50)
    
    posY = 10
    
    posY = WriteText(screen, screenSize, myfont, name, posY, True)
    
    posY += 100
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    posY = WriteText(screen, screenSize, myfont, "Rules for the game: ", posY, True)
    posY += 10
    
    posY = WriteText(screen, screenSize, myfont, "Standard Tetris rules, filling a full row removes that row.", posY, False)
    
    posY = WriteText(screen, screenSize, myfont, "Filling multiple rows earns bonus points.", posY, False)
    
    posY = WriteText(screen, screenSize, myfont, "The game will continue until a block cannot be spawned in the usual spawn point.", posY, False)
    
    posY += 20
    
    posY = WriteText(screen, screenSize, myfont, "Controls for the game: ", posY, True)
    
    posY += 10
    
    posY = WriteText(screen, screenSize, myfont, "Press the up arrow to rotate the block clockwise.", posY, False)
    
    posY = WriteText(screen, screenSize, myfont, "Use the left and right arrows to move the block in that direction.", posY, False)
    
    posY = WriteText(screen, screenSize, myfont, "Press the down arrow to drop the current piece all the way to the bottom of the board", posY, False)

    posY = WriteText(screen, screenSize, myfont, "Hold shift to increase the descent speed.", posY, False)
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    continueText = "Continue"
    continueRenderedText = myfont.render(continueText, 50, (255,255,0))
    continueSize = myfont.size(continueText)
    
    continueButton = button.Button(
        (screenSize[0] // 2, posY + 20), 
        (continueSize[0] + 10, continueSize[1] + 10), 
        continueText, continueRenderedText, continueSize)
    
    screen.blit(continueButton.image, continueButton.rect)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        # proceed events
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                value = continueButton.HandleMousePress(pos)
                
                if value != None:
                    return True
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
                
            elif event.type == pygame.QUIT:
                return False
        
    

    