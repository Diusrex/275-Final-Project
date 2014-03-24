"""
import pygame
from pygame.locals import *
from tile import Tile
import random
"""

import pygame
from pygame.locals import *
from MineSweeper.tile import Tile
import random

# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3

    
def Main(screen, size):
    wantsToExit = False
    
    font = pygame.font.SysFont("monospace", 12, bold = True)
    
    while not wantsToExit:
        gameResult = runGame(screen, size)
        
        # They wanted to exit while in game
        if gameResult == None:
            return
        if gameResult == 1:
            label = font.render("Congratulations, you won the game!", 50, (0, 0, 0))
        elif gameResult == 0:
            label = font.render("You bit the bullet", 50, (0, 0, 0))
        
        screen.blit(label, (0, 0))
        
        label = font.render("To play another game press enter.", 50, (0,0,0))
        screen.blit(label, (0, font.size("hi")[1] + 5))
        label = font.render("To exit press escape.", 50, (0,0,0))
        screen.blit(label, (0, font.size("hi")[1] * 2 + 5))
        
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

                    
                    
def runGame(screen, size):    
    """
    If there was a winner, will draw the game before returning
    
    """
    # sets up the screen width and height in tiles
    WIDTH = 30
    HEIGHT = 30

    pygame.display.set_mode((WIDTH * Tile.WIDTH, HEIGHT * Tile.HEIGHT))

    NUM_MINES = 100

    # create the minesweeper board
    board = createBoard(WIDTH, HEIGHT, NUM_MINES)

    redraw = True
    gameResult = None
    
    while True:
        ev = pygame.event.get()
        
        # proceed events
        for event in ev:
            # Means user wanted to press button here
            if event.type == pygame.MOUSEBUTTONUP:
                # event.button == 1 is left click
                # evnet.button == 3 is right click
                pos = pygame.mouse.get_pos()
                tilePos = (pos[0] // 10, pos[1] // 10)
                
                # left button reveals the tile
                if event.button == 1:
                    redraw = True
                    clickedMine = reveal(board, tilePos[0], tilePos[1])
                    
                    if clickedMine:
                        gameResult = 0
                    elif cleared(board):
                        gameResult = 1

                # right button flags the tile
                if event.button == 3:
                    redraw = True
                    try:
                        board[tilePos[0]][tilePos[1]].toggleFlag()
                    except IndexError:
                        pass
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            
            elif event.type == QUIT:
                return
                
        if redraw:
            screen.fill((0, 0, 0))
            drawBoard(screen, board, 0, 0)
            pygame.display.flip()
            redraw = False

        # gameResult should be 1 for victory, 0 for defeat
        if gameResult is not None:
            return gameResult
     
def createBoard(width, height, numMines):
    """
    Creates a board with a set width and height of tiles
    as well as a specific number of mines
    """
    # creates a 2D list for the board
    # creates a list to store coordinates that are not mines
    noMines = []
    board = []
    for x in range(width):
        board.append([])
        for y in range(height):
            board[x].append(Tile(0))
            noMines.append((x, y))

    # makes sure numMines is not too big
    if numMines > width * height:
        numMines = width * height

    # randomly chooses coordinates to make mines, that are not mines
    # already
    # tiles beside the mines have their number incremented by 1
    while numMines > 0:
        mine = random.choice(noMines)

        noMines.remove(mine)
        board[mine[0]][mine[1]] = Tile(-1)
        numMines -= 1
        # look at the adjacent tiles, and increment them
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                try:
                    if mine[0]+x >= 0 and mine[1]+y >= 0:
                        board[mine[0]+x][mine[1]+y].increaseNumber()
                except IndexError: # if the index is out of bounds, ignore it
                    pass

    return board

def drawBoard(screen, board, x, y):
    """
    Given a 2D list of Tiles, draws them
    starting from (x,y)
    """
    for xi in range(len(board)):
        for yi in range(len(board[x])):
            board[xi][yi].draw(screen, x + (xi * Tile.WIDTH), y + (yi * Tile.HEIGHT))
            
def reveal(board, x, y):
    """
    Reveals a tile
    If the tile is a 0, reveal all adjacent tiles

    Returns whether the tile was a mine (T or F)
    """
    try:
        if x < 0 or y < 0:
            return False

        tile = board[x][y]
        revealAdjacent = False

        # if this tile is hidden, and enough adjacent tiles are flagged
        # reveal all non flagged adjacent tiles
        if not tile.hidden:
            numMines = tile.number
            for xi in (-1, 0, 1):
                for yi in (-1, 0, 1):
                    if x + xi < 0 or y + yi < 0 or x + xi >= len(board) or y + yi >= len(board):
                        continue
                    if (xi, yi) != (0, 0) and board[x+xi][y+yi].isFlagged():
                        numMines -= 1
            if numMines == 0:
                revealAdjacent = True

        if not tile.isFlagged():
            tile.show()
            if tile.isMine():
                return True
        
        if tile.number == 0:
            revealAdjacent = True

        # reveals adjacent tiles
        # this should never return true, so there
        # is no need to check
        if revealAdjacent:
            for xi in (-1, 0, 1):
                for yi in (-1, 0, 1):
                    if (xi, yi) != (0, 0) and board[x+xi][y+yi].hidden:
                        reveal(board, x + xi, y + yi)
    except IndexError:
        pass

    return False

def cleared(board):
    """
    Returns true if all but the mine tiles have been
    revealed
    """
    for column in board:
        for tile in column:
            if not tile.isMine() and tile.hidden == True:
                return False

    return True

if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    
