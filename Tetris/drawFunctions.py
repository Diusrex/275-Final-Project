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
    
    
    
    
    
def DisplayHighScores(screen, allocatedSize, posY, highScores, fontSize):
    """
    Will display all of the high scores, and will return the final posY below the text.
    """
    myfont = pygame.font.SysFont("monospace", fontSize)
    
    posY = WriteText(screen, allocatedSize, myfont, "High Scores:", posY, True)
    
    place = 1
    for score in highScores:
        # No point in continuing to draw
        if score[0] == "":
            break
                
        output = "%d: %s %7d" % (place, score[0], score[1])
        posY = WriteText(screen, allocatedSize, myfont, output, posY, True)
        place += 1
        
    return posY   