import pygame

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
    

def DrawScore(screen, score, screenSize):
    """
    Will draw the players score to the top center of the screen
    """
    myfont = pygame.font.SysFont("monospace", 200)
        
    firstScore = myfont.render(str(score.leftPlayerScore), 200, (255,255,255))
        
        
    secondScore = myfont.render(str(score.rightPlayerScore), 200, (255,255,255))
    
    separator = myfont.render(':', 200, (255,255,255))
    
    middle = screenSize[0] / 2
    spacer = 15
    
    firstPosx = middle - spacer - myfont.size(str(score.leftPlayerScore))[0]
    secondPosx = middle + spacer
    separatorPosx = middle - myfont.size(':')[0] / 2
    
    screen.blit(firstScore, (firstPosx, 0))
    screen.blit(separator, (separatorPosX, 0))
    screen.blit(secondScore, (secondPosx, 0))