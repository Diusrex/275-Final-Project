import pygame
import block
from coordinate import Coordinate

from drawFunctions import WriteText, DisplayHighScores


class Game:
    """
    Will handle all of the game's logic.
    Only part it will not handle is displaying the loss screen
    """
    def __init__(self, screenSize, boxSize):
        """
        Initializes the size of the game. Does not set up any of the game logic though
        """
        self.boxSize = boxSize
        self.totalSize = screenSize
        
        self.leftSize = (200, screenSize[1])
        
        self.middleOffset = 200
        self.middleSize = (screenSize[0] - 400, screenSize[1])
        
        self.rightOffset = screenSize[0] - 200
        
        self.rightSize = (200, screenSize[1])
        
        self.scorePerRow = 100
        # scoreMultiplyer[0] is just for ease of getting the score multiplyer
        self.scoreMultiplyer = [0, 1, 1.2, 1.4, 1.8]
        
        self.timeToShiftStart = 1000
        self.timeToShiftMinimum = 500
        
        
    def SetUpNewGame(self):
        self.lost = False
        self.numberBoxesX = self.middleSize[0] // self.boxSize
        self.numberBoxesY = self.middleSize[1] // self.boxSize
        
        self.score = 0
        
        # Will be the position passed to the block that will be up next, should be near the top right corner
        self.upNextBlockPos = Coordinate(3, self.numberBoxesY - 3)

        # Want it placed at the top of the screen, in the centre of the used area
            # Remember that the spawnPos is immediately decreased by 1
        self.spawnPos = Coordinate(self.numberBoxesX // 2, self.numberBoxesY - 1)
        
        print(self.spawnPos)
        # If there is no block in position, will be None. Otherwise, will be the image corresponding to the block that is in that position
        # Is [x][y]
        self.placedGrid = [[None for y in range(self.numberBoxesY)] for x in range(self.numberBoxesX)]
        
        self.SetUpUsedBlock(block.Block(self.spawnPos, self.boxSize))
        
        self.CreateNewNextBox()
    
    
    
    
    def SetUpUsedBlock(self, newBlock):
        """
        Will create the usedBlock from the given new block. Will also check to see if the used block could be created by call Update() on it, and will return the value of Update.
        
        Will normally be transferred from by upNextBlock
        """
        self.usedBlock = newBlock
        return self.usedBlock.Update(self.placedGrid)
    
    
    
    
    def CreateNewNextBox(self):
        """
        Will create a new Block for upNextBLock, using the spawn pos for it
        """
        self.upNextBlock = block.Block(self.upNextBlockPos, self.boxSize)
        
        
        
        
    def RunUntilLoss(self, screen, highScores):
        """
        Will run the game until the user looses.
        Will return the user's score
        """
        redraw = True
    
        clock = pygame.time.Clock()
        
        timePassed = 0
        self.timeToShift = self.timeToShiftStart
        
        # If the user is pressing shift, then the speed at which blocks descends will increase
        shiftPressed = False
        
        while not self.lost:
            ev = pygame.event.get()
            
            for event in ev:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    
                    elif event.key == pygame.K_LEFT:
                        ableToMove = self.usedBlock.MoveHorizontal(self.placedGrid, -1)
                        if ableToMove:
                            redraw = True
                            
                    elif event.key == pygame.K_RIGHT:
                        ableToMove = self.usedBlock.MoveHorizontal(self.placedGrid, 1)
                        if ableToMove:
                            redraw = True
                            
                    elif event.key == pygame.K_DOWN:
                        # Does this make me a terrible person?
                        while (self.usedBlock.Update(self.placedGrid)):   
                            pass
            
                        self.HandleUsedBlockImpact()
                        
                        redraw = True
                        
                    elif event.key == pygame.K_UP:
                        self.usedBlock.RotateClockwise(self.placedGrid)
                        redraw = True
                    
                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        shiftPressed = True
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        shiftPressed = False
                        
                elif event.type == pygame.QUIT:
                    return
                    
            timePassed += clock.tick()
            
            if timePassed >= timeToShift or (shiftPressed and timePassed >= timeToShift / 4):
                ableToMove = self.usedBlock.Update(self.placedGrid)
                
                if not ableToMove:
                    self.HandleUsedBlockImpact()
                    
                        
                redraw = True        
                timePassed = 0
            
            
            if redraw:
                screen.fill((0, 0, 0))
                
                self.DrawUpNextBox(screen)
                
                
                self.usedBlock.Draw(screen, self.middleSize[1], self.middleOffset)
                
                self.DrawGrid(screen)
                
                self.DrawScores(screen, highScores)
                
                pygame.display.flip()
                
                redraw = False
        
        print("Returning score")
        # Return the score
        return self.score
        
    def HandleUsedBlockImpact(self):
        """
        Will handle all of the logic required to handle the usedBlock impacting the floor
        """
        self.usedBlock.SaveInGrid(self.placedGrid)
        
        self.RemoveCompletedRows()
        
        self.usedBlock = self.upNextBlock
        
        self.usedBlock.SetPosition(self.spawnPos)
        self.upNextBlock = block.Block(self.upNextBlockPos, self.boxSize)
        
        placeable = self.usedBlock.Update(self.placedGrid)
        if not placeable:
            self.lost = True
        
        redraw = True
    
    
    def RemoveCompletedRows(self):
        """
        This will remove all completed rows, and give the user a score, with a score multiplier for combos
        """
        count = 0
        # Go through each of the rows. Easiest to go from top to bottom
        for yPos in range(self.numberBoxesY - 1, 0, -1):
        
            allFilled = True
            for xPos in range(self.numberBoxesX):
                if not self.placedGrid[xPos][yPos]:
                    allFilled = False
                    
            # Can delete this row
            if allFilled:
                count += 1
                for xPos in range(self.numberBoxesX):
                    for tempYPos in range(yPos, self.numberBoxesY - 1):
                        self.placedGrid[xPos][tempYPos] = self.placedGrid[xPos][tempYPos + 1]
                    self.placedGrid[xPos][self.numberBoxesY - 1] = None
        
        if count > 0:
            self.timeToShift -= random.randint(20, 50)
            
            # Shouldn't be less than minimum
            if self.timeToShift < self.timeToShiftMinimum:
                self.timeToShift = self.timeToShiftMinimum
                
        scoreIncrease = count * self.scorePerRow * self.scoreMultiplyer[count]
        self.score += scoreIncrease
    
    def DrawUpNextBox(self, screen):
        """
        Will also draw some infomation for the user
        """
        myfont = pygame.font.SysFont("monospace", 20)
        
        label = myfont.render("Next block:", 50, (255,255,0))
        
        screen.blit(label, (self.rightOffset + 5, 40))
        
        self.upNextBlock.Draw(screen, self.middleSize[1], self.rightOffset)
        
        
    def DrawGrid(self, screen):
        """
        Will draw the grid
        This includes both the boxes in the placedGrid, and the lines separating each box.
        The lines will be gray
        """
        # Draw the boxes
        for boxXPos in range(self.numberBoxesX):
            for boxYPos in range(self.numberBoxesY):
                if self.placedGrid[boxXPos][boxYPos]:
                    screen.blit(self.placedGrid[boxXPos][boxYPos], 
                        [self.middleOffset + self.boxSize * boxXPos, self.totalSize[1] - self.boxSize * boxYPos])
        
        # Draw the lines
        for boxXPos in range(self.numberBoxesX + 1):
            pygame.draw.line(screen, (128, 128, 128), 
                (self.middleOffset + self.boxSize * boxXPos, self.totalSize[1] - self.boxSize * self.numberBoxesY), 
                (self.middleOffset + self.boxSize * boxXPos, self.totalSize[1]))
            
        for boxYPos in range(self.numberBoxesY + 1):
            pygame.draw.line(screen, (128, 128, 128), 
            (self.middleOffset, self.totalSize[1] - self.boxSize * boxYPos), (self.middleOffset + self.boxSize * self.numberBoxesX, self.totalSize[1] - self.boxSize * boxYPos))    
    
    def DrawScores(self, screen, highScores):
        """
        Will draw the score to the right of the screen
        """
        
        myfont = pygame.font.SysFont("monospace", 20)
        
        positionY = WriteText(screen, self.leftSize, myfont, "Current Score:", 20, True)
        
        positionY = WriteText(screen, self.leftSize, myfont, str(self.score), positionY, True)
        
        positionY += 100
        positionY = DisplayHighScores(screen, self.leftSize, positionY, highScores, 20)