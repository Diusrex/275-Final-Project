import pygame
from pygame.locals import *

import BoxContainer
import Player
import Calculations
import PositionInfo

# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3

    
def main(screen, size):
    wantsToExit = False
    
    while not wantsToExit:
        playerOutput = run_game(screen, size)
        
        # They wanted to exit while in game
        if playerOutput == None:
            return
            
        
        myfont = pygame.font.SysFont("monospace", 15)
        
        label = myfont.render("Congratulations " + playerOutput + ", you won the game!", 50, (255,255,0))
        
        screen.blit(label, (300, 0))
        
        label = myfont.render("To play another game press enter. To exit press escape", 50, (255,255,0))
        screen.blit(label, (300, myfont.size("hi")[1] + 5))
        
        pygame.display.flip()
        
        valid = False
        
        while not valid:
            ev = pygame.event.get()

            # proceed events
            for event in ev:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        valid = True
                        wantsToExit = True
                    
                    elif event.key == K_RETURN:
                        valid = True
                        
                elif event.type == QUIT:
                    return

                    
                    
def run_game(screen, size):    
    """
    If there was a winner, will draw the game before returning
    
    """
    
    players = [Player.Player("Player 1", 1, pygame.image.load('xPressed.png')),
               Player.Player("Player 2", 2, pygame.image.load('oPressed.png'))]
    
    
    imageSize = BoxContainer.BoxContainer.notPressedImage.get_rect()
    
    spacer = 20
    miniSpacer = 15
    
    # Want to make it so the box will be centred
    xStart = (size[0] - (imageSize.width * 9 + spacer * 2 + miniSpacer * 6)) / 2
    yStart = (size[1] - (imageSize.height * 9 + spacer * 2 + miniSpacer * 6)) / 2
    
    
    allBoxContainers, allBoxOwners, positionInfo = CreateBoxes(15, spacer, miniSpacer, xStart, yStart)
    
    
    # Will be the size of one box
    currentIdentifier = pygame.Surface((positionInfo.startPosX[1] - positionInfo.startPosX[0] - spacer, positionInfo.startPosY[1] - positionInfo.startPosY[0] - spacer))
    
    currentIdentifier.set_alpha(128)
    currentIdentifier.fill((0, 0, 0))
    
    currentPlayer = 0
    
    currentBox = 4
    
    
    redraw = True
    
    while True:
        ev = pygame.event.get()
        
        # proceed events
        for event in ev:
            # Means user wanted to press button here
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                
                # if it was a valid press, x will be a tuple containing (boxStatus, boxPressedIn)
                x = allBoxContainers[currentBox].HandleClicked(pos, players[currentPlayer])
                
                # It is possible that it is impossible to place in current box, in which case any box is valid
                if (not allBoxContainers[currentBox].CanBeClickedIn()):
                    for box in allBoxContainers:
                        temp = box.HandleClicked(pos, players[currentPlayer])
                        if temp != None:
                            x = temp
                
                    
                    
                if x != None:   
                    allBoxOwners[currentBox] = x[0]
                    winner = Calculations.CheckIfWin(allBoxOwners)
                    
                    # This is to display special information about who won, this function will be exited from
                    if (winner[0] != 0):
                        DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer)
                        
                        # Draw the winning line
                        startBoxNum = winner[1][0]
                        endBoxNum = winner[1][1]
                        
                        startPos = allBoxContainers[startBoxNum].GetCenter()
                       
                        endPos = allBoxContainers[endBoxNum].GetCenter()
                        
                        pygame.draw.line(screen, (0, 255, 0), startPos, endPos, 15)
                        
                        # winner is just the player id that won, so guaranteed to return
                        for player in players:
                            if player.id == winner[0]:
                                return player.name
                            
                    redraw = True
                    
                    currentPlayer = 1 - currentPlayer
                    
                    currentBox = x[1]
                    
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            
            elif event.type == QUIT:
                return
                
        if redraw:
            
            DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer)
            DrawCurrentPlayer(screen, players[currentPlayer])
            
            if allBoxContainers[currentBox].CanBeClickedIn():
                screen.blit(currentIdentifier, (positionInfo.startPosX[currentBox %3], positionInfo.startPosY[currentBox//3]))
            
            pygame.display.flip()
            
            redraw = False


def DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer):
    """
    Will draw all of the standard information to the screen
    Note: To finish drawing, must call pygame.display.flip() after calling this function
    """
    
    screen.fill((0, 0, 0))
            
    for drawBox in allBoxContainers:
        drawBox.Draw(screen)
    
    DrawLines(screen, positionInfo, spacer)
    
    
def CreateBoxes(linesExtraLength, spacer, miniSpacer, xStart, yStart):
    allBoxContainers = []
    allBoxOwners = []
    
    positionInfo = PositionInfo.PositionInfo(xStart, yStart)
    
    for y in range(3):
        for x in range(3):
            allBoxContainers.append(BoxContainer.BoxContainer((positionInfo.startPosX[x],  positionInfo.startPosY[y]), miniSpacer))
            
            # Want the bottom right corner of the box
            tempRect = allBoxContainers[-1].GetBottomRight()
            
            positionInfo.startPosX[x + 1] = tempRect[0] + spacer
            positionInfo.startPosY[y + 1] = tempRect[1] + spacer
            
            positionInfo.lineSideStartX[x] = tempRect[0]
            positionInfo.lineSideStartY[y] = tempRect[1]
            
            allBoxOwners.append(0)
            
    
    positionInfo.lineStartX = positionInfo.startPosX[0] - linesExtraLength
    positionInfo.lineStartY = positionInfo.startPosY[0] - linesExtraLength
    
    
    # The startPos[3] is the start pos immediately after the final box
    positionInfo.lineLengthX = positionInfo.startPosX[3] - positionInfo.startPosX[0] + linesExtraLength * 2 - spacer
    positionInfo.lineLengthY = positionInfo.startPosY[3] - positionInfo.startPosY[0] + linesExtraLength * 2 - spacer
    
    
    positionInfo.lineSideStartX.pop()
    positionInfo.lineSideStartY.pop()
    
    return allBoxContainers, allBoxOwners, positionInfo

    
    
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
    myfont = pygame.font.SysFont("monospace", 15)
    
    text = "Current player is " + currentPlayerInfo.name + ": "
    
    label = myfont.render(text, 50, (255,255,0))
    
    rect = currentPlayerInfo.image.get_rect()
    
    screen.blit(label, (0, (rect.height - myfont.size(text)[1]) / 2))
    
    
    
    rect.left = myfont.size(text)[0]
    rect.top = 0
    
    screen.blit(currentPlayerInfo.image, rect)
            
if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    