import pygame
import Calculations

class BoxContainer(pygame.sprite.Sprite):
    """
    Will hold a 3 by 3 grid of boxes. Will not draw lines for itself
    
    self.allSprites/positions are [y * 3 + x]
        x = pos % 3
        y = pos // 3
    
    self.status is the player this is owned by -> 0 means not owned by anyone
    """
    
    notPressedImage = pygame.image.load('blank.png')    
    
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
        
        rect = BoxContainer.notPressedImage.get_rect()
        
        # Goes through creating each box
        for yPos in range(3):
            for xPos in range(3):
                self.allSprites.append(BoxContainer.notPressedImage)
                
                currentRect = rect.move(position[0] + rect.width * xPos + spacing * xPos, position[1] + rect.height * yPos + spacing * yPos)
                self.allPositions.append(currentRect)
                
                self.ownedBy.append(0)
        
    
    def GetBottomRight(self):
        bottomRightRect = self.allPositions[-1]
        return (bottomRightRect[0] + bottomRightRect.width, bottomRightRect[1] + bottomRightRect.height)
        
    def HandleClicked(self, mousePos, player):
        """
        Will handle determining if the player pressed one of the boxes. 
        If the player changed a box, will return a tuple containing:
            0: This entities status
            1: The box to use
            
        Otherwise, will return None
        """
        for pos in range(9):
            if (self.allPositions[pos].collidepoint(mousePos) and (self.ownedBy[pos] == 0)):
                self.allSprites[pos] = player.image
                self.ownedBy[pos] = player.id
                
                # Check to see if the status could have been changed
                if self.status == 0:
                    
                    info = Calculations.CheckIfWin(self.ownedBy)
                    
                    if (info[0] != 0):
                        self.status = info[0]
                        
                        startBox = info[1][0]
                        endBox = info[1][1]
                        
                        self.victoryLineStart = self.allPositions[startBox].center
                        self.victoryLineEnd = self.allPositions[endBox].center
                        
                # The player changed a box
                return (self.status, pos)
      
                
        
        return None
        
    def Draw(self, screen):
        for pos in range(9):
            screen.blit(self.allSprites[pos], self.allPositions[pos])
            
        if (self.victoryLineStart != None):
            pygame.draw.line(screen, (0, 255, 0), self.victoryLineStart, self.victoryLineEnd, 5)