import pygame

import random

# Use this include if running from base menu
from Tetris.coordinate import Coordinate


"""
# Use this include if running this game individually
from coordinate import Coordinate
"""

class Block:
    """
    This will be the current falling block. Once a block has fallen, that block should be stored in the grid instead.
    
    All coordinates are based on the grid, which is based on the size of each block
    """
    
    # Note: The 0, 0 position should be within one block of the top of the object
    
    shapes = ([Coordinate(0, 1), Coordinate(0, 0), Coordinate(0, -1), Coordinate(0, -2)], # straight line
              [Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, -1), Coordinate(1, -1)], # box
              [Coordinate(0, 0), Coordinate(1, 0), Coordinate(-1, -1), Coordinate(0, -1)], # 's'
              [Coordinate(-1, 0), Coordinate(0, 0), Coordinate(0, -1), Coordinate(1, -1)], # 'z'
              [Coordinate(0, 0), Coordinate(1, 0), Coordinate(-1, 0), Coordinate(-1, 1)], # 'J'
              [Coordinate(0, 0), Coordinate(-1, 0), Coordinate(1, 0), Coordinate(1, 1)], # 'J'
              [Coordinate(-1, 0), Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, -1)]) #'T'
              
    # Only the box at [1] is not able to be rotated      
    ableToRotate = (True, False, True, True, True, True, True)
    
    # Colors: White, red, blue, green, yellow, cyan
    colors = ((255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255))
    
    def __init__(self, position, blockSize):
        """
        Will generate itself using one of the shape options, and one of the color options
        """
        self.position = position.Copy()
        self.blockSize = blockSize
        
        shapeToUsed = random.randrange(len(Block.shapes))
        
        # To ensure that the shape of this object does not effect the original shape
        self.shape = []
        for block in Block.shapes[shapeToUsed]:
            self.shape.append(block.Copy())
        self.rotatable = Block.ableToRotate[shapeToUsed]
        
        
        self.image = pygame.Surface((blockSize, blockSize))
        self.image.fill(random.choice(Block.colors))
        
    def SetPosition(self, newPos):
        self.position = newPos.Copy()
    
    def MoveHorizontal(self, grid, move):
        """
        Will check to see if the block can be moved the requested number of units horizontally. If it can will return True, otherwise will return False
        """
        xPos = self.position.x
        yPos = self.position.y
        
        for block in self.shape:
            # Means would go out of bounds
            if xPos + block.x + move < 0 or xPos + block.x + move >= len(grid):
                return False
            # Means there is a block where it will be moving to
            elif grid[xPos + block.x + move][yPos + block.y]:
                return False
        self.position.x += move
        return True
        
    def RotateClockwise(self, grid):
        """
        How rotation will be handled:
        1. Will rotate in the direction wanted around the centre position
        2. Will then horizontally to ensure that this object doesn't interfere with any other objects.
        3. If the second step was not possible, then will not rotate
        
        EDIT: For now, will not use step 2
        """
        # Some shapes should not rotate
        if not self.rotatable:
            return
            
        tempShape = [Coordinate(block.y, block.x * -1) for block in self.shape]
        
   
        for block in tempShape:
            # Would be rotated out of the grid
            if (self.position.y + block.y < 0 or self.position.y + block.y >= len(grid[0])) or (self.position.x + block.x < 0 or self.position.x + block.x >= len(grid)):
                return 
            
            
            # There is a block there, so nothing should be changed
            elif grid[self.position.x + block.x][self.position.y + block.y]:
                return
        
        self.shape = tempShape
        
    def Update(self, grid):
        """
        This should only be called every time the block is to descend one step
        
        The block cannot go below 1, because then it will be beyond the screen
        Will return true if it was able to move down
        """
        xPos = self.position.x
        yPos = self.position.y
        
        for block in self.shape:
            if yPos + block.y - 1 < 1:
                return False
                
            # Means there is a block where it will be moving to
            elif grid[xPos + block.x][yPos + block.y - 1]:
                return False
        
        self.position.y -= 1
        return True
        
    def Draw(self, screen, bottomPos, horizontalOffset):    
        """
        Remember that the bottomPos will be screenSize[1], because the top of the screen is (0, 0)
        """
        xPos = self.position.x
        yPos = self.position.y
        for block in self.shape:
            screen.blit(self.image, [horizontalOffset + self.blockSize * (xPos + block.x), bottomPos - self.blockSize * (yPos + block.y)])
        
        
        
    def SaveInGrid(self, grid):
        """
        This means that the Block has collided with an object, and will now become part of the grid
        """
        
        
        for block in self.shape:
            grid[self.position.x + block.x][self.position.y + block.y] = self.image
        