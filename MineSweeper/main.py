import pygame
from pygame.locals import *

# Whenever storing 2d data in a 1d array, stores as y * 3 + x
    # So x = pos % 3, y = pos // 3

    
def main(screen, size):
    wantsToExit = False
    
    while not wantsToExit:
        playerOutput = run_game(screen, size)
        
        # They wanted to exit while in game
        if playerOutput == None:
            return
            
        
        myfont = pygame.font.SysFont("monospace", 15)
        
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

                    
                    
def run_game(screen, size):    
    """
    If there was a winner, will draw the game before returning
    
    """
    
    players = [Player.Player("Player 1", 1, pygame.image.load('xPressed.png')),
               Player.Player("Player 2", 2, pygame.image.load('oPressed.png'))]
    
    
    imageSize = BoxContainer.BoxContainer.notPressedImage.get_rect()
    
    spacer = 20
    miniSpacer = 15
    
    # Want to make it so the box will be centred
    xStart = (size[0] - (imageSize.width * 9 + spacer * 2 + miniSpacer * 6)) / 2
    yStart = (size[1] - (imageSize.height * 9 + spacer * 2 + miniSpacer * 6)) / 2
    
    
    allBoxContainers, allBoxOwners, positionInfo = CreateBoxes(15, spacer, miniSpacer, xStart, yStart)
    
    
    # Will be the size of one box
    currentIdentifier = pygame.Surface((positionInfo.startPosX[1] - positionInfo.startPosX[0] - spacer, positionInfo.startPosY[1] - positionInfo.startPosY[0] - spacer))
    
    currentIdentifier.set_alpha(128)
    currentIdentifier.fill((0, 0, 0))
    
    currentPlayer = 0
    
    currentBox = 4
    
    
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
     
if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    
