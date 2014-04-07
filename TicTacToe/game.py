import pygame

# Use these imports and code if this will be a subdirectory

import TicTacToe.drawFunctions as drawFunctions
import TicTacToe.section as section

import TicTacToe.calculations as calculations

from TicTacToe.positionInfo import PositionInfo

"""
# Use these imports and code if running the game individually

import drawFunctions
import section

import calculations

from positionInfo import PositionInfo
  
"""

tieStatus = "Tie"

    
class Game:
    def __init__(self, player1, player2, screenSize):
        """
        _players stores the two player classes
        _spacer is the space separating sections
        _currentIdentifier is the grey box that is drawn over the current box to be placed in
        _allSections stores all of the sections.
        _allSectionOwners stores who owns which section. If is not owned, will be 0
        _positionInfo stores general position info about the board
        
        miniSpacer is the space separating the boxes within an individual section
        """
        self._players = (player1, player2)
        
        imageSize = section.Section.notPressedImage.get_rect()
    
        self._spacer = 20
        miniSpacer = 15
        
        # Want to make it so the box will be centred
        xStart = (screenSize[0] - (imageSize.width * 9 + self._spacer * 2 + miniSpacer * 6)) / 2
        yStart = (screenSize[1] - (imageSize.height * 9 + self._spacer * 2 + miniSpacer * 6)) / 2
        
        
        self.CreateSections(15, miniSpacer, xStart, yStart)
    
        self._currentIdentifier = pygame.Surface((self._positionInfo.startPosX[1] - self._positionInfo.startPosX[0] - self._spacer, self._positionInfo.startPosY[1] - self._positionInfo.startPosY[0] - self._spacer))
    
        self._currentIdentifier.set_alpha(128)
        self._currentIdentifier.fill((0, 0, 0))
        
        
        
        
        
    def CreateSections(self, linesExtraLength, miniSpacer, xStart, yStart):
        """
        Will set up all of the classes sections, and the corresponding positionInfo
        """
        # This information will be added to self later in this function, just reduces typing
        allSections = []
        allSectionOwners = []
        
        positionInfo = PositionInfo(xStart, yStart)
        
        for y in range(3):
            for x in range(3):
                allSections.append(section.Section((positionInfo.startPosX[x],  positionInfo.startPosY[y]), miniSpacer))
                
                
                tempRect = allSections[-1].GetBottomRight()
                
                # This sets up the information for later boxes, so the position doesn't need to be calculated each time.
                    # Is also used later for drawing the overlay
                positionInfo.startPosX[x + 1] = tempRect[0] + self._spacer
                positionInfo.startPosY[y + 1] = tempRect[1] + self._spacer
                
                positionInfo.lineSideStartX[x] = tempRect[0]
                positionInfo.lineSideStartY[y] = tempRect[1]
                
                allSectionOwners.append(0)
                
        
        positionInfo.lineStartX = positionInfo.startPosX[0] - linesExtraLength
        positionInfo.lineStartY = positionInfo.startPosY[0] - linesExtraLength
        
        
        # The startPos[3] is the start pos immediately after the final box
        positionInfo.lineLengthX = positionInfo.startPosX[3] - positionInfo.startPosX[0] + linesExtraLength * 2 - self._spacer
        positionInfo.lineLengthY = positionInfo.startPosY[3] - positionInfo.startPosY[0] + linesExtraLength * 2 - self._spacer
        
        
        positionInfo.lineSideStartX.pop()
        positionInfo.lineSideStartY.pop()
        
        
        self._allSections = allSections
        self._allSectionOwners = allSectionOwners
        self._positionInfo = positionInfo
        
        
        
        
        
    def Run(self, screen, screenSize):
        """
        Will leave the screen drawn before returning.
        
        If the user wanted to exit, will return None, otherwise will return the id of the winner
        """
        currentPlayer = 0
        
        currentSection = 4
        
        self.DrawBasic(screen, screenSize)
        self.DrawInfo(screen, screenSize, self._players[currentPlayer], currentSection)
        pygame.display.flip()
        
        while True:
            # Checking to see if any section can be placed in
            if self.GameIsTie():
                return tieStatus
            
            chosen = self._players[currentPlayer].ChoosePosition(self._allSections, self._allSectionOwners, currentSection, self._players[1 - currentPlayer].id)
            
            # The user wanted to exit (so no need to redraw)
            if chosen == None:
                return None
            
            
            changedSection = chosen[0]
            boxChanged = chosen[1]
            
            newStatus = self._allSections[changedSection].AssignBoxToPlayer(boxChanged, self._players[currentPlayer])
            
            # The new section relates to the box that was changed
            currentSection = boxChanged
            
            
            # Update allSectionOwners (may remain 0). Does not use the old currentSection, because the player may have been able to place anywhere
            self._allSectionOwners[changedSection] = newStatus
            
            self.DrawBasic(screen, screenSize)
            
            winner = calculations.CheckIfWin(self._allSectionOwners)
            
            if (winner != None):
                # Draw the winning line
                startBoxNum = winner[0]
                endBoxNum = winner[1]
                
                startPos = self._allSections[startBoxNum].GetCenter()
               
                endPos = self._allSections[endBoxNum].GetCenter()
                
                pygame.draw.line(screen, (0, 255, 0), startPos, endPos, 15)
                
                # winner is the player who just played, so return them
                return self._players[currentPlayer].name
                        
            # Update the information for the next run
            currentPlayer = 1 - currentPlayer
            
            self.DrawInfo(screen, screenSize, self._players[currentPlayer], currentSection)
            pygame.display.flip()
                
                
                
    def GameIsTie(self):
        """
        Will check to see if it is still possible for a player to make a move
        """
        for section in self._allSections:
            if section.CanBeClickedIn():
                return False
        
        return True
        
        
        
        
        
    def DrawBasic(self, screen, screenSize):
        """
        Will clear the screen and draw the sections, but will not draw the player, or the currentIdentifier
        """
        screen.fill((0, 0, 0))
        drawFunctions.DrawBoxesAndLinesToScreen(screen, self._allSections, self._positionInfo, self._spacer)
    
    
    
    
    def DrawInfo(self, screen, screenSize, thePlayer, currentSection):
        """
        Will draw all of the info related to the game, such as the player and the currentIdentifier
        """
        drawFunctions.DrawCurrentPlayer(screen, thePlayer)
        
        if self._allSections[currentSection].CanBeClickedIn():
            screen.blit(self._currentIdentifier, (self._positionInfo.startPosX[currentSection %3], self._positionInfo.startPosY[currentSection//3]))