import pygame
import os

# Use this import if running from base menu
import Tetris.drawFunctions as drawFunctions


"""
# Use this import if running game individually
import drawFunctions
"""

maxNumScores = 10
maxNameSize = 10


# For the highscores, there may be spaces in the name. Everything other than the last item (which will be the score) in a line will be interpreted as part of the name

def LoadHighScores(fileName):
    """
    Will load up to maxNumScores highScores. 
    
    Even if there are less than this number, or if the file does not exist, will return a list of tuples with size maxNumScores
        If an entry is just a filler, its will be ["", 0]
    """
    highScores = [("", 0) for x in range(maxNumScores)]
    
    # Ensure that the file exists before doing anything with it
    if os.path.isfile(fileName):
        with open(fileName, 'r') as theFile:
            pos = 0
            
            for line in theFile:
                if pos >= maxNumScores:
                    break
                
                line = line.strip().split()
                
                if len(line) > 1:
                    highScores[pos] = (' '.join(line[0:-1]), int(line[-1]))
                    
                    pos += 1
    
    return highScores

    
    
    
    
def UpdateHighScores(screen, screenSize, score, highScores, fileName):
    """
    Will determine if the player earned a new high score. If they did, will prompt them to input their name (using GetHighScoreInput).
        Will then shift all of the scores after the changed score up one
    """
    different = False
    for pos in range(len(highScores)):
        if highScores[pos][1] < score:
            different = True
            name = GetHighScoreInput(screen, screenSize, score, pos)
            
            for newPos in range(len(highScores) - 1, pos, -1):
                highScores[newPos] = highScores[newPos - 1]
            
            highScores[pos] = (name, score)
            
            different = True
            
            break
    
    if different:
        with open(fileName, 'w') as theFile:
        
            for score in highScores:
                # Has hit the end of the high scores, no need to write anything else
                if score[0] == "":
                    break
                theFile.write("%s %d\n" % (score[0], score[1]))
        
       



       
def GetHighScoreInput(screen, screenSize, score, pos):
    """
    Will allow the user to enter their name (which has a size limited by maxNameSize to make the scores print better
    
    Note: This function does not allow the user to quit.
    """
    redraw = True
    finished = False
    
    # Because position for output is not 0 indexed (makes it easier to output)
    pos = pos + 1
    
    name = ""
    
    while not finished:
        ev = pygame.event.get()
            
        for event in ev:
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_RETURN:
                    if name != "":
                        finished = True
                
                elif event.key == pygame.K_BACKSPACE:
                    if name != "":
                        name = name[:-1]
                        redraw = True
                
                
                # Make some assumptions about all being valid
                elif event.key <= 127 and event.key != pygame.K_TAB:
                    if len(name) < maxNameSize:
                        name += pygame.key.name(event.key)
                        redraw = True
        
        if redraw:
            screen.fill((0, 0, 0))
            posY = 0
            myfont = pygame.font.SysFont("monospace", 30)
            
            posY = drawFunctions.WriteText(screen, screenSize, myfont, "Congratulations!", posY, True)
            
            posY = drawFunctions.WriteText(screen, screenSize, myfont, "Your score got you into ranking %d!" % pos, posY, True)
                    
            posY = drawFunctions.WriteText(screen, screenSize, myfont, "What is your name? (Press enter to finish)", posY, True)
            
            posY = drawFunctions.WriteText(screen, screenSize, myfont, "There is a limit of %d characters in your name." % maxNameSize, posY, True)
            
            posY = drawFunctions.WriteText(screen, screenSize, myfont, name, posY, True)
            
            pygame.display.flip()
            
    return name
    
    
    
    
    
def ShowScoreScreen(screen, screenSize, score, highScores):
    """
    Will display all of the top scores, after they have been updated with the most recent score, and the users score.
    Note: Will not allow the user to quit.
    """
    
    # clear all of the events
    ev = pygame.event.get()
    
    screen.fill((0, 0, 0))
    
    myfont = pygame.font.SysFont("monospace", 30)
    
    posY = 20
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Congratulations, you earned a score of " + str(score), posY, True)
    
    if score == 0:
        posY = drawFunctions.WriteText(screen, screenSize, myfont, "I'm sure you'll do better next time", posY, True)
    
    posY += 20
    
    myfont = pygame.font.SysFont("monospace", 15)
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Press enter/return to go to the main menu", posY, True)
    
    drawFunctions.DisplayHighScores(screen, screenSize, posY + 15, highScores, 15)
    
    pygame.display.flip()
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return