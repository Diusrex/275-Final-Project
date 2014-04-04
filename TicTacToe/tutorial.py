import pygame
import random
import button

# Use this import if running from base menu
import TicTacToe.drawFunctions as drawFunctions

"""
# Use this import if running individually
import drawFunctions
"""

name = "Novem Tic Tac Toe"
backText = "Back"
nextText = "Next"
finishText = "Finish"

def RunTutorial(screen, screenSize):
    """
    Will display the tutorial/information needed for the user to be able to play properly.
    
    Will return True if the user wanted to go to the menu, otherwise will return False (and thus wants to exit)
    """
    pageNum = 1
    myfont = pygame.font.SysFont("monospace", 50)
    
    while pageNum > 0 and pageNum < 3:
        if pageNum == 1:
            wanted = Page1(screen, screenSize, myfont)
        
        elif pageNum == 2:
            wanted = Page2(screen, screenSize, myfont)
        
        if wanted == nextText:
            pageNum += 1
        elif wanted == backText:
            pageNum -= 1
        else:
            return
    
    
def Page1(screen, screenSize, myfont):
    # Only need to draw once, because the screen will not change within this function
    screen.fill((0, 0, 0))
    posY = 10
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, name, posY, True)
    posY += 20
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Rules for the game: ", posY, True)
    posY += 10
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "The game board is a large Tic Tac Toe board which consists of 9 mini Tic Tac Toe boards.", posY, False)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "The mini Tic Tac Toe boards will be referred to as 'sections'", posY, True)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "The spots inside of a mini Tic Tac Toe board will be called a box.", posY, True)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "The current box to play in will be shaded a darker color.", posY, True)
    
    ticTacToeImage = pygame.image.load("Assets/TicTacToe_Main.png")
    ticTacToeRect = ticTacToeImage.get_rect()
    ticTacToeRect.center = (screenSize[0] // 2, posY + ticTacToeRect.height // 2)
    screen.blit(ticTacToeImage, ticTacToeRect)
    posY += ticTacToeRect.height + 30
    
    return RunRestOfMenu(screen, screenSize, posY)
    
    
def Page2(screen, screenSize, myfont):
    # Only need to draw once, because the screen will not change within this function
    screen.fill((0, 0, 0))
    posY = 10
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, name, posY, True)
    posY += 20
    
    myfont = pygame.font.SysFont("monospace", 20)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "When a player plays in a box,", posY, True)
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "the other player will then play in the section in the same position as that box", posY, True)
    posY += 10
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Example:", posY, True)
    
    # Don't need to save the image after it is drawn to screen
    ticTacToeImage = pygame.image.load("Assets/TicTacToe_HowPlayingWorks1.png")
    ticTacToeRect = ticTacToeImage.get_rect()
    ticTacToeRect.center = (screenSize[0] // 4, posY + ticTacToeRect.height // 2)
    screen.blit(ticTacToeImage, ticTacToeRect)
    
    
    ticTacToeImage = pygame.image.load("Assets/TicTacToe_HowPlayingWorks2.png")
    ticTacToeRect = ticTacToeImage.get_rect()
    ticTacToeRect.center = (screenSize[0] // 2 + screenSize[0] // 4, posY + ticTacToeRect.height // 2)
    screen.blit(ticTacToeImage, ticTacToeRect)
    posY += ticTacToeRect.height + 30
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "As can be seen...", posY, True)
    
    return RunRestOfMenu(screen, screenSize, posY + 15)
                
def RunRestOfMenu(screen, screenSize, posY):
    myfont = pygame.font.SysFont("monospace", 25)
    
    nextRenderedText = myfont.render(nextText, 50, (255,255,0))
    nextSize = myfont.size(nextText)
    
    backRenderedText = myfont.render(backText, 50, (255,255,0))
    backSize = myfont.size(backText)
    
    
    nextPos = ((screenSize[0] + backSize[0] + 20) // 2, posY) 
    backPos = ((screenSize[0] - nextSize[0] - 20) // 2, posY)
    
    buttonGroup = pygame.sprite.Group()
    
    buttonGroup.add(button.Button(
                        nextPos, 
                        (nextSize[0] + 10, nextSize[1] + 10), 
                        nextText, nextRenderedText, nextSize))
    
    buttonGroup.add(button.Button(
                        backPos, 
                        (backSize[0] + 10, backSize[1] + 10), 
                        backText, backRenderedText, backSize))
    
    finishRenderedText = myfont.render(finishText, 50, (255, 255, 0))
    finishSize = myfont.size(finishText)
    
    buttonGroup.add(button.Button(
                        (screenSize[0] // 2, posY + 40), 
                        (finishSize[0] + 10, finishSize[1] + 10), 
                        finishText, finishRenderedText, finishSize))
    
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
                return finishText
                
            elif event.type == pygame.QUIT:
                return finishText