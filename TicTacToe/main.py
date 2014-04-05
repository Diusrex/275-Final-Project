import pygame


# Use these imports when running the main menu
import TicTacToe.menu as menu
import TicTacToe.game as game
import TicTacToe.tutorial as tutorial

import TicTacToe.drawFunctions as drawFunctions

import TicTacToe.player as player

"""
# Use these imports when running the game individually
import menu
import game
import tutorial

import drawFunctions

import player
"""


# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3
    # This is for this game only

    
def Main(screen, screenSize):
    wantsToExit = False
    tryingToExit = False
    
    while not tryingToExit:
        decision = menu.RunMenu(screen, screenSize)
        
        if decision == menu.tutorialText:
            tutorial.RunTutorial(screen, screenSize)
        
        elif decision == menu.twoPlayerText or decision == menu.onePlayerText:
            winner = RunGame(screen, screenSize, decision)
            
            if winner == None:
                tryingToExit = True
                
            elif winner == game.tieStatus:
                ShowTieScreen(screen, screenSize)
                
            else:
                ShowWinScreen(screen, screenSize, winner)
            
        else:
            tryingToExit = True

def RunGame(screen, screenSize, decision):
    playerOne = player.HumanPlayer("Player one", 1, pygame.image.load('Assets/xPressed.png'))
    
    if decision == menu.twoPlayerText:
        playerTwo = player.HumanPlayer("Player two", 2, pygame.image.load('Assets/oPressed.png'))
        
    else:
        return None
    
    theGame = game.Game(playerOne, playerTwo, screenSize)
    
    return theGame.Run(screen, screenSize)
                
                
def ShowWinScreen(screen, screenSize, winner):
    """
    screen should already have the background set up
    """
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 30
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Congratulations " + winner + " you have won!", posY, True)
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return

                
                
def ShowTieScreen(screen, screenSize):
    """
    screen should already have the background set up
    """
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 30
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Well that is unfortunate, no one may play, and thus the game is a tie.", posY, True)
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return
                
                
if __name__ == "__main__":
    pygame.init()
    screenSize = (1024, 650)
    screen = pygame.display.set_mode(screenSize)
    main(screen, screenSize)
    
    