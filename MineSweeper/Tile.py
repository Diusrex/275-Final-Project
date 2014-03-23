import pygame
from pygame.locals import *

class Tile:
    """
    A tile in minesweeper, which has either
    a mine or a number. The number should be
    the number of mines adjacent to it, or if
    it is a mine, should be -1
    """

    # These constants are for use outside the tile
    # They should be used for spacing for drawing
    # The images for hidden.png, tile.png, mind.png
    # should also be of these dimensions
    # 
    # These are intended as constants, so should not
    # be changed
    WIDTH = 10
    HEIGHT = 10

    pygame.init()

    # images for tiles
    hiddenImage = pygame.image.load("hidden.png")
    shownImage = pygame.image.load("shown.png")
    mineImage = pygame.image.load("mine.png")
    flagImage = pygame.image.load("flag.png")

    # The font for numbers in tiles
    font = pygame.font.SysFont("monospace", HEIGHT)

    def __init__(self, number):
        """
        Creates a tile with the specified number
        if this tile is a mine, the number should
        be -1
        All tiles begin hidden
        """
        self.number = number
        self.hidden = True
        self.text = Tile.font.render(str(self.number), 1, (255, 255, 0))
        self.flag = False

    def draw(self, screen, x, y):
        """
        draws the tile, if it's hidden it
        will not draw this contents within
        """
        if self.hidden:
            screen.blit(Tile.hiddenImage, (x, y))
            if self.flag:
                screen.blit(Tile.flagImage, (x, y))
        else:
            screen.blit(Tile.shownImage, (x, y))
            if self.isMine():
                screen.blit(Tile.mineImage, (x, y))
            else:
                screen.blit(self.text, (x, y))

    def isMine(self):
        """
        returns true if this tile is a mine
        returns false if this tile is not a mine
        """
        if self.number == -1:
            return True

        return False

    def show(self):
        """
        makes the tile uncovered, if there is no flag on it
        """
        if not self.flag:
            self.hidden = False

    def toggleFlag(self):
        """
        Toggles the flag on the tile
        """
        self.flag = not self.flag

    def isFlagged(self):
        return self.flag
        
    def increaseNumber(self):
        """
        Increases the number
        Intended to be used if a mine
        is placed beside the tile
        """
        if not self.isMine():
            self.number += 1
            self.text = Tile.font.render(str(self.number), 1, (0, 0, 0))
