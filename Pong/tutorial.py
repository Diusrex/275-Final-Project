import pygame
import random
import button

name = "Pong"

def RunTutorial(screen, size):
    """
    Will display the tutorial/information needed for the user to be able to play properly.
    
    Will return True if the user wanted to go to the menu, otherwise will return False (and thus wants to exit)
    """
    # Only need to draw once, because the screen will not change after
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 50)
    
    posY = 10
    
    posY = WriteText(screen, size, myfont, name, posY, True)
    
    posY += 100
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    posY = WriteText(screen, size, myfont, "Rules for the game: ", posY, True)
    posY += 10
    
    posY = WriteText(screen, size, myfont, "To score a point, the ball must hit the opposite wall from your paddle.", posY, False)
    
    posY = WriteText(screen, size, myfont, "The first player to score 7 points wins.", posY, False)
    
    posY = WriteText(screen, size, myfont, "The ball will slowly increase its speed, and will start in a random direction.", posY, False)
    
    posY += 20
    
    posY = WriteText(screen, size, myfont, "Controls for the game: ", posY, True)
    
    posY += 10
    
    posY = WriteText(screen, size, myfont, "The first player (paddle on left) conrols their paddle with w and s.", posY, False)
    
    posY = WriteText(screen, size, myfont, "The second player (paddle on right) conrols their paddle with left and right arrows.", posY, False)
    
    posY = WriteText(screen, size, myfont, "To exit, press exit", posY, False)
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    continueText = "Continue"
    continueRenderedText = myfont.render(continueText, 50, (255,255,0))
    continueSize = myfont.size(continueText)
    
    continueButton = button.Button(
        (size[0] // 2, posY + 20), 
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
        
    
def WriteText(screen, screenSize, font, text, posY, center):
    """
    Will return the new posY, after the increase from the recently added text
    """
    toRender = font.render(text, 50, (255, 255, 0))
    
    size = font.size(text)
    
    if center:
        posX = (screenSize[0] - size[0]) / 2
    else:
        posX = 0
    
    screen.blit(toRender, (posX, posY))
    
    
    return posY + size[1] + 5
    