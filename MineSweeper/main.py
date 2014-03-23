import pygame
from pygame.locals import *
import Tile from Tile.py

# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3

    
def main(screen, size):
    wantsToExit = False
    
    while not wantsToExit:
        playerOutput = runGame(screen, size)
        
        # They wanted to exit while in game
        if playerOutput == None:
            return
        
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

                    
                    
def runGame(screen, size):    
    """
    If there was a winner, will draw the game before returning
    
    """
    # create the minesweeper board
    board = createBoard(10, 10)

    redraw = True
    
    while True:
        ev = pygame.event.get()
        
        # proceed events
        for event in ev:
            # Means user wanted to press button here
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            
            elif event.type == QUIT:
                return
                
        if redraw:
            screen.fill((0, 0, 0))
            pygame.display.flip()
            redraw = False
     
def createBoard(width, height, numMines):
    """
    Creates a board with a set width and height of tiles
    as well as a specific number of mines
    """
    # creates a 2D list for the board
    board = [[Tile(0) for y in range(height)] for x in range(width)]

    # creates a list to store coordinates that are not mines
    noMines = []
    for x in board:
        for y in board[x]:
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
        for x in (-1, 1):
            for y in (-1, 1):
                try:
                    board[mine[0]+x][mine[1]+y].increaseNumber()
                except IndexError: # if the index is out of bounds, ignore it
                    pass

    return board

if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    
