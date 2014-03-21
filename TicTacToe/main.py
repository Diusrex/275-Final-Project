import pygame
from pygame.locals import *
import BoxContainer
import Player

# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3

# Note: Images must be squares

def main(screen):
    
    wantsToExit = False
    
    while not wantsToExit:
        playerOutput = run_game(screen)
        
        print("Completed")
        
        screen.fill((0, 0, 0))
        
        myfont = pygame.font.SysFont("monospace", 15)
        
        label = myfont.render("Congratulations " + playerOutput + ", you won the game!", 50, (255,255,0))
        
        screen.blit(label, (0, 200))
        
        label = myfont.render("To play another game press enter. To exit press escape", 50, (255,255,0))
        screen.blit(label, (0, 500))
        
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
                        
def run_game(screen):
    
    
    players = [Player.Player("Player 1", 1, pygame.image.load('xPressed.png')),
               Player.Player("Player 2", 2, pygame.image.load('oPressed.png'))]
    
    
    spacer = 20
    allBoxContainers, allBoxOwners, boxStartPoses, lineSideStart, lineOtherSideEnd = CreateBoxes(spacer)
    
    # Will be the size of one box
    currentIdentifier = pygame.Surface((lineSideStart[0] - boxStartPoses[0], lineSideStart[0] - boxStartPoses[0]))
    
    allBoxOwners = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    
    currentIdentifier.set_alpha(128)
    currentIdentifier.fill((0, 0, 0))
    
    currentPlayer = 0
    
    currentBox = 4
    
    while True:
        ev = pygame.event.get()

        # proceed events
        for event in ev:
            # Means user wanted to press button here
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = allBoxContainers[currentBox].HandleClicked(pos, players[currentPlayer])
                
                if (x != None):
                    allBoxOwners[currentBox] = x[0]
                    
                    winner = CheckIfWin(allBoxOwners)
                    
                    if (winner != 0):
                        for player in players:
                            if player.id == winner:
                                return player.name
                        
                    currentPlayer = 1 - currentPlayer
                    
                    currentBox = x[1]
                    
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                
        screen.fill((0, 0, 0))
        
        for drawBox in allBoxContainers:
            drawBox.Draw(screen)
        
        DrawLines(screen, lineSideStart, lineOtherSideEnd, spacer)
        
        screen.blit(currentIdentifier, (boxStartPoses[currentBox %3], boxStartPoses[currentBox//3]))
        
        pygame.display.flip()

        
def CreateBoxes(spacer):
    allBoxContainers = []
    allBoxOwners = []
    
    startPoses = [0, 0, 0, 0]
    
    lineSideStart = [0, 0, 0]
    
    for y in range(3):
        for x in range(3):
            allBoxContainers.append(BoxContainer.BoxContainer((startPoses[x], startPoses[y]), 15))
            tempRect = allBoxContainers[-1].GetBottomRight()
            
            
            startPoses[x + 1] = tempRect[0] + spacer
            lineSideStart[x] = tempRect[0]
            
            allBoxOwners.append(0)
            
    # Will be the size of one box
    currentIdentifier = pygame.Surface((lineSideStart[0] - startPoses[0], lineSideStart[0] - startPoses[0]))
    
    lineSideStart.pop()
    
    lineOtherSideEnd = [startPoses[0], startPoses[3] - spacer]
    
    return allBoxContainers, allBoxOwners, startPoses, lineSideStart, lineOtherSideEnd

def CheckIfWin(allBoxOwners):
    for dimension in range(3):
        id = allBoxOwners[dimension * 3]
        
        same = True
        
        # Horizontal
        for x in range(1, 3):
            if allBoxOwners[dimension * 3 + x] != id:
                same = False
        
        if same and id != 0:
            return id
            
        # Vertical
        id = allBoxOwners[dimension]
        same = True
        for y in range(1, 3):
            if allBoxOwners[y * 3 + dimension] != id:
                same = False
    
        if same and id != 0:
            return id
    
    topLeftId = allBoxOwners[0]
    topRightId = allBoxOwners[2]
    
    topLeftSame = True
    topRightSame = True
    
    for spot in range(1, 3):
        if (allBoxOwners[spot * 4] != topLeftId):
            topLeftSame = False
        
        if (allBoxOwners[2 + spot * 2] != topRightId):
            topRightSame = False
     
    if topLeftSame and topLeftId != 0:
        return topLeftId
    
    if topRightSame and topRightId != 0:
        return topRightId
    
    return 0
    
    
def DrawLines(screen, lineSideStart, lineOtherSideEnd, spacer):
    for start in lineSideStart:
        pygame.draw.line(screen, (255, 0, 0), (start + spacer / 2, lineOtherSideEnd[0]), (start + spacer / 2, lineOtherSideEnd[1]), spacer)
        pygame.draw.line(screen, (255, 0, 0), (lineOtherSideEnd[0], start + spacer / 2), (lineOtherSideEnd[1], start + spacer / 2), spacer)

    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    main(screen)
    
    