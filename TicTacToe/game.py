import pygame

import drawFunctions
import boxContainer

import calculations

# EDIT: Probably a bad idea to have a module that shares a name with many variables
from positionInfo import PositionInfo
from player import Player  
        
def RunGame(screen, screenSize):    
    """
    If there was a winner, will leave the screen drawn and return the score info
    
    If the user wanted to exit, then will return None
    """
    
    players = [Player("Player 1", 1, pygame.image.load('xPressed.png')),
               Player("Player 2", 2, pygame.image.load('oPressed.png'))]
    
    
    imageSize = boxContainer.BoxContainer.notPressedImage.get_rect()
    
    spacer = 20
    miniSpacer = 15
    
    # Want to make it so the box will be centred
    xStart = (screenSize[0] - (imageSize.width * 9 + spacer * 2 + miniSpacer * 6)) / 2
    yStart = (screenSize[1] - (imageSize.height * 9 + spacer * 2 + miniSpacer * 6)) / 2
    
    
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
                if (allBoxContainers[currentBox].CanBeClickedIn()):
                    x = allBoxContainers[currentBox].HandleClicked(pos, players[currentPlayer])
                
                # It is possible that it is impossible to place in current box, in which case any box is valid
                else:
                    for box in allBoxContainers:
                        temp = box.HandleClicked(pos, players[currentPlayer])
                        if temp != None:
                            x = temp
                
                    
                    
                if x != None:   
                    allBoxOwners[currentBox] = x[0]
                    winner = calculations.CheckIfWin(allBoxOwners)
                    
                    # This is to display special information about who won, this function will be exited from
                    if (winner[0] != 0):
                        screen.fill((0, 0, 0))
                        drawFunctions.DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer)
                        
                        # Draw the winning line
                        startBoxNum = winner[1][0]
                        endBoxNum = winner[1][1]
                        
                        startPos = allBoxContainers[startBoxNum].GetCenter()
                       
                        endPos = allBoxContainers[endBoxNum].GetCenter()
                        
                        pygame.draw.line(screen, (0, 255, 0), startPos, endPos, 15)
                        
                        # winner is just the player id that won, so guaranteed to return
                        for user in players:
                            if user.id == winner[0]:
                                return user.name
                            
                    redraw = True
                    
                    currentPlayer = 1 - currentPlayer
                    
                    currentBox = x[1]
                    
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
            elif event.type == pygame.QUIT:
                return
                
        if redraw:
            screen.fill((0, 0, 0))
            drawFunctions.DrawBoxesAndLinesToScreen(screen, allBoxContainers, positionInfo, spacer)
            drawFunctions.DrawCurrentPlayer(screen, players[currentPlayer])
            
            if allBoxContainers[currentBox].CanBeClickedIn():
                screen.blit(currentIdentifier, (positionInfo.startPosX[currentBox %3], positionInfo.startPosY[currentBox//3]))
            
            pygame.display.flip()
            
            redraw = False

def CreateBoxes(linesExtraLength, spacer, miniSpacer, xStart, yStart):
    allBoxContainers = []
    allBoxOwners = []
    
    positionInfo = PositionInfo(xStart, yStart)
    
    for y in range(3):
        for x in range(3):
            allBoxContainers.append(boxContainer.BoxContainer((positionInfo.startPosX[x],  positionInfo.startPosY[y]), miniSpacer))
            
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