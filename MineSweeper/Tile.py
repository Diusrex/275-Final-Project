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

    # images for tiles
    hiddenImage = pygame.image.load("hidden.png")
    shownImage = pygame.image.load("shown.png")
    mineImage = pygame.image.load("mine.png")

    # The font for numbers in tiles
    font = pygame.font.SysFont("monospace", HEIGHT)

    def __init__(number):
        """
        Creates a tile with the specified number
        if this tile is a mine, the number should
        be -1
        All tiles begin hidden
        """
        self.number = number
        self.hidden = True

    def draw(screen, x, y):
        """
        draws the tile, if it's hidden it
        will not draw this contents within
        """
        if self.hidden == True:
            screen.blit(hiddenImage, (x, y))
        else:
            screen.blit(shownImage, (x, y))
            if self.isMine():
                screen.blit(mine, (x, y))
            else:
                text = font.render(self.number, 1, (255, 255, 0))
                screen.blit(text, (x, y))

    def isMine():
        """
        returns true if this tile is a mine
        returns false if this tile is not a mine
        """
        if self.number == -1:
            return True

        return False

    def show():
        """
        makes the tile uncovered
        """
        self.hidden = False

    def increaseNumber():
        """
        Increases the number
        Intended to be used if a mine
        is placed beside the tile
        """
        if not isMine():
            self.number += 1
