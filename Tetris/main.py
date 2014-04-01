import pygame
import random
import game

import block
from coordinate import Coordinate

def main(screen, size):
    wantsToExit = False
    
    theGame = game.Game(size, 30)
    
    while not wantsToExit:
        run_game(screen, theGame)
        
        # They wanted to exit while in game
        if playerOutput == None:
            return
            
        
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
                    valid = True
                    wantsToExit = True

                    
                    
def run_game(screen, theGame):    
    """
    
    """
    theGame.SetUpNewGame()
    theGame.RunUntilLoss(screen)
    
    



if __name__ == "__main__":
    random.seed()
    
    pygame.init()
    size = (1024, 650)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    