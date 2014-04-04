import pygame
import random

import button

# These are all of the names associated with this menu.
name = "Mini Games"
pongText = "Play Pong"
ticTacToeText = "Play Novem Tic Tac Toe"
tetrisText = "Play Tetris"
exitText = "Exit"


def RunMenu(screen, screenSize):
    """
    Will return one of pongText, ticTacToeText, tetrisText, or exitText
    """
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 50)
    
    infoSize = myfont.size(name)
    nameRenderText = myfont.render(name, 50, (255,255,0))
    
    screen.blit(nameRenderText, ( (screenSize[0] - infoSize[0]) / 2, 0))
    
    myfont = pygame.font.SysFont("monospace", 25)
    
    buttonGroup = pygame.sprite.Group()
    
    posY = 300
    ticTacToeImage = pygame.image.load("Assets/TicTacToe_Main.png")
    ticTacToeRect = ticTacToeImage.get_rect()
    ticTacToeRect.center = (screenSize[0] // 2, posY)
    
    posY = ticTacToeRect.bottom + 30
    
    posY = CreateButtonAndAdd(buttonGroup, (ticTacToeRect.center[0], posY), myfont, ticTacToeText)
    CreateButtonAndAdd(buttonGroup, (screenSize[0] // 2, posY + 20), myfont, exitText)
    
    
    # This is to be centered within either side of the ticTacToe rect
    xPos = (screenSize[0] - ticTacToeRect.width) / 4
    CreateButtonAndAdd(buttonGroup, (xPos, screenSize[1] // 2), myfont, pongText)
    
    CreateButtonAndAdd(buttonGroup, (screenSize[0] - xPos, screenSize[1] // 2), myfont, tetrisText)
    
    
    
    
    screen.blit(ticTacToeImage, ticTacToeRect)
    
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


def CreateButtonAndAdd(buttonGroup, centerPosition, font, text):
    """
    Will create the wanted button, and will add it to the given buttonGroup.
    Will return the yPos immediately below the button
    """
    tempRenderedText = font.render(text, 50, (255,255,0))
    tempSize = font.size(text)
    
    buttonGroup.add(button.Button(
                        centerPosition, 
                        (tempSize[0] + 10, tempSize[1] + 10), 
                        text, tempRenderedText, tempSize))
                        
    return centerPosition[1] + (tempSize[1] + 10)