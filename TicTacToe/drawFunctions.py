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
    
    
    
    
    
def DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer):
    """
    Will draw all of the standard information to the screen
    Note: To finish drawing, must call pygame.display.flip() after calling this function
    """
    for drawBox in allBoxContainers:
        drawBox.Draw(screen)
    
    DrawLines(screen, positionInfo, spacer)
    
    
    
    
    
def DrawLines(screen, positionInfo, spacer):
    for xStart in positionInfo.lineSideStartX:
        pygame.draw.line(screen, (255, 0, 0), 
            (xStart + spacer / 2, positionInfo.lineStartY), 
            (xStart + spacer / 2, positionInfo.lineStartY + positionInfo.lineLengthY), spacer)
        
    for yStart in positionInfo.lineSideStartY:
        pygame.draw.line(screen, (255, 0, 0), 
            (positionInfo.lineStartX, yStart + spacer / 2), 
            (positionInfo.lineStartX + positionInfo.lineLengthX, yStart + spacer / 2), spacer)


            
            
            
def DrawCurrentPlayer(screen, currentPlayerInfo):
    myfont = pygame.font.SysFont("monospace", 20)
    
    text = "Current player is " + currentPlayerInfo.name + ": "
    
    label = myfont.render(text, 50, (255,255,0))
    
    rect = currentPlayerInfo.image.get_rect()
    
    screen.blit(label, (0, (rect.height - myfont.size(text)[1]) / 2))
    
    rect.left = myfont.size(text)[0]
    rect.top = 0
    
    screen.blit(currentPlayerInfo.image, rect)