import pygame

# Use this import and code if running from base menu
import TicTacToe.calculations as calculations

"""
# Use this import if running this game individually
import calculations
"""

class Section(pygame.sprite.Sprite):
    """
    Will hold a 3 by 3 grid of boxes. Will not draw lines for itself
    
    self.allSprites/positions are [y * 3 + x]
        x = pos % 3
        y = pos // 3
    
    self.status is the player this is owned by -> 0 means not owned by anyone
    """
    
    notPressedImage = pygame.image.load('Assets/blank.png')    
    
    
    def __init__(self, position, spacing):
        """
        position -> top left position of the box (remember, top left is (0, 0))
        Is to be given its top position, as well as a 3 by 3 list of all inner boxes.
        Size is to be the total size of the area given to this box. Size should not include any spacing required for the outer spacing, and position should incorporate this
        """
        pygame.sprite.Sprite.__init__(self)
        
        self.current = False
        
        
        self.status = 0
        
        self.allSprites = []
        self.allPositions = []
        self.ownedBy = []
        
        # This is for the line to be drawn if there is a winner 
        self.victoryLineStart = None
        self.victoryLineEnd = None
        
        rect = Section.notPressedImage.get_rect()
        
        # Goes through creating each box
        for yPos in range(3):
            for xPos in range(3):
                self.allSprites.append(Section.notPressedImage)
                
                currentRect = rect.move(position[0] + rect.width * xPos + spacing * xPos, position[1] + rect.height * yPos + spacing * yPos)
                self.allPositions.append(currentRect)
                
                self.ownedBy.append(0)
        
        
    
    def GetOwnedBy(self):
        """
        This function is to ONLY be used by the ai. It will make it far easier to use minimax, because the entire Section will not need to be copied.
        
        Will return a copy of the list of which box is owned by who.
        """
        return list(self.ownedBy)
        
        
        
    def GetCenter(self):
        """
        Will return the center position of this section
        """
        middleRect = self.allPositions[4]
        return middleRect.center
        
        
        
        
    def GetBottomRight(self):
        """
        Will return the bottom right position of this section
        """
        bottomRightRect = self.allPositions[-1]
        return (bottomRightRect[0] + bottomRightRect.width, bottomRightRect[1] + bottomRightRect.height)
    
    
    
    
    def CanBeClickedIn(self):
        """
        Will return true if any of any boxes haven't been placed in
        """
        return 0 in self.ownedBy
        
        
        
        
    def HandleClicked(self, mousePos):
        """
        Will handle determining if the player pressed one of the boxes. 
        If the player is able to change a box, will return the pos of that box
            
        Otherwise, will return None
        
        Warning, can return 0, so need to check for if the value isn't None
        """
        for pos in range(9):
            if (self.allPositions[pos].collidepoint(mousePos) and (self.ownedBy[pos] == 0)):
                return pos
        
        return None
    
    
    
    
    def AssignBoxToPlayer(self, boxPos, player):
        """
        Will update the changed box, and if necessary, check to see if this section was won by claiming that box.
            If it was, will set up this section to be able to draw the victoryLine within this section.
        
        Will then return the status (who controls the box) of this section
        """
        self.allSprites[boxPos] = player.image
        self.ownedBy[boxPos] = player.id
        
        # Check to see if the status could have been changed (cant if it isn't 0)
        if self.status == 0:
            
            info = calculations.CheckIfWin(self.ownedBy)
            
            if (info != None):
                # Know that this player was the one who just won this box
                self.status = player.id
                
                startBox = info[0]
                endBox = info[1]
                
                self.victoryLineStart = self.allPositions[startBox].center
                self.victoryLineEnd = self.allPositions[endBox].center
                
        return self.status
             


             
    def Draw(self, screen):
        """
        Will draw all the boxes inside of this Section, and will draw the win line if there is one
        """
        for pos in range(9):
            screen.blit(self.allSprites[pos], self.allPositions[pos])
            
        if (self.victoryLineStart != None):
            pygame.draw.line(screen, (0, 255, 0), self.victoryLineStart, self.victoryLineEnd, 5)
    