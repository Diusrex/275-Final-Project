import pygame
import random
import button

name = "Pong"
playText = "Play the Game"
tutorialText = "How to Play"
exitText = "Exit"


def RunMenu(screen, screenSize):
    """
    Will return one of playText, tutorialText, or exitText
    """
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 50)
    
    infoSize = myfont.size(name)
    nameRenderText = myfont.render(name, 50, (255,255,0))
    
    screen.blit(nameRenderText, ( (screenSize[0] - infoSize[0]) / 2, 0))
    
    buttonGroup = CreateButtons(infoSize[1] + 100, screenSize)
    
    
    buttonGroup.draw(screen)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        # proceed events
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                for currentButton in buttonGroup.sprites():
                    value = currentButton.HandleMousePress(pos)
                    if value != None:
                        return value
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return exitText
                
            elif event.type == pygame.QUIT:
                return exitText


def CreateButtons(posY, screenSize):
    """
    Will create a pygame.sprite.Group that contains all of the buttons. The top buttons will appear at posY
    """
    buttonGroup = pygame.sprite.Group()
    
    myfont = pygame.font.SysFont("monospace", 25)
    
    tempRenderedText = myfont.render(playText, 50, (255,255,0))
    tempSize = myfont.size(playText)
    
    buttonGroup.add(button.Button(
                        (screenSize[0] //2, posY), 
                        (tempSize[0] + 10, tempSize[1] + 10), 
                        playText, tempRenderedText, tempSize))
    
    posY += tempSize[1] + 60
    
    tempRenderedText = myfont.render(tutorialText, 50, (255,255,0))
    tempSize = myfont.size(tutorialText)
    
    buttonGroup.add(button.Button(
                        (screenSize[0] //2, posY), 
                        (tempSize[0] + 10, tempSize[1] + 10), 
                        tutorialText, tempRenderedText, tempSize))
    
    posY += tempSize[1] + 60
    
    tempRenderedText = myfont.render(exitText, 50, (255,255,0))
    tempSize = myfont.size(exitText)
    
    buttonGroup.add(button.Button(
                        (screenSize[0] //2, posY), 
                        (tempSize[0] + 10, tempSize[1] + 10), 
                        exitText, tempRenderedText, tempSize))
                        
    return buttonGroup