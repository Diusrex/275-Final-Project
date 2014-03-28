import pygame
from pygame.locals import *
import pygame.time
import math

import ball

from player import Player
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

                    
class Scores():
    def __init__(self):
        self.leftPlayerScore = 0
        
        self.rightPlayerScore = 0
        
    def HitLeftSide(self):
        self.rightPlayerScore += 1
    
    def HitRightSide(self):
        self.leftPlayerScore += 1
        
def run_game(screen, size):    
    """
    If there was a winner, will draw the game before returning
    
    """
    
    
    players = [Player("Player 1", (12, size[1] / 2), K_w, K_s),
               Player("Player 2", (size[0] - 15, size[1] / 2), K_UP, K_DOWN)]
    
    
    allSprites = pygame.sprite.Group()
    allSprites.add(players[0])
    allSprites.add(players[1])
    
    score = Scores()
    theBall = ball.Ball((250, 250), [40, 40], score)
    
    allSprites.add(theBall)
    # add paddle
    
    clock = pygame.time.Clock()
    
    while True:
        ev = pygame.event.get()
        
        # proceed events
        for event in ev:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                
                for player in players:
                    player.HandleKeyPress(event.key)
                
            elif event.type == KEYUP:
                for player in players:
                    player.HandleKeyRelease(event.key)
            
            elif event.type == QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        time = clock.tick()
        
        allSprites.update(time / 100, size)
        
        allSprites.draw(screen)
        
        if pygame.sprite.collide_rect(players[0], theBall):
            theBall.speed[0] = math.fabs(theBall.speed[0])
        if pygame.sprite.collide_rect(players[1], theBall):
            theBall.speed[0] = - math.fabs(theBall.speed[0])
        
        DrawScore(screen, score, size)
        
        pygame.display.flip()

def DrawScore(screen, score, screenSize):
    myfont = pygame.font.SysFont("monospace", 200)
        
    firstScore = myfont.render(str(score.leftPlayerScore), 200, (255,255,255))
        
        
    secondScore = myfont.render(str(score.rightPlayerScore), 200, (255,255,255))
    
    middle = screenSize[0] / 2
    spacer = 15
    
    firstPos = middle - spacer - myfont.size(str(score.leftPlayerScore))[0]
    secondPos = middle + spacer
    
    screen.blit(firstScore, (firstPos, 0))
    screen.blit(secondScore, (secondPos, 0))
    
    
if __name__ == "__main__":
    pygame.init()
    size = (1024, 768)
    screen = pygame.display.set_mode(size)
    main(screen, size)
    
    