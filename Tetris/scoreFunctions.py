import pygame
import os
import drawFunctions

maxNumScores = 10
maxNameSize = 10

def LoadHighScores(fileName):
    """
    Will load up to maxNumScores highScores. 
    
    Even if there are less than this number, or if the file does not exist, will return a list of tuples with size maxNumScores
        If an entry is just a filler, its [0] will be ""
    """
    highScores = [("", 0) for x in range(maxNumScores)]
    
    

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
    redraw = True
    finished = False
    
    # Because position for output is not 0 indexed
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
    Will overwrite the screen createdy by the game
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
    
    posY = drawFunctions.WriteText(screen, screenSize, myfont, "Press any button to return to the main menu", posY, True)
    
    drawFunctions.DisplayHighScores(screen, screenSize, posY + 15, highScores, 15)
    
    # EDIT: Display all older high scores, and add option to add own high score?
    
    pygame.display.flip()
    
    
    
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                return