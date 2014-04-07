import pygame

# This file exists in most of the games, but the functions in it are mostly specialized for that specific game

def WriteText(screen, screenSize, font, text, posY, center):
    """
    Will return the new posY, after the increase from the recently added text.
    
    This function is standard among the games with text
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
    myfont = pygame.font.SysFont("monospace", 50)
    
    output = "%d : %d" % (score.leftPlayerScore, score.rightPlayerScore)
    
    WriteText(screen, screenSize, myfont, output, 0, True)