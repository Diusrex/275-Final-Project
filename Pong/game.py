import pygame
from pygame.locals import *
import pygame.time
import math

import ball

from player import Player

class Scores():
    def __init__(self):
        self.leftPlayerScore = 0
        
        self.rightPlayerScore = 0
        
    def HitLeftSide(self):
        self.rightPlayerScore += 1
    
    def HitRightSide(self):
        self.leftPlayerScore += 1
        
        
def RunGame(screen, size):    
    """
    If there was a winner, will leave the screen drawn and return the score info
    
    If the user wanted to exit, then will return None
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
    
    while score.leftPlayerScore < 7 and score.rightPlayerScore < 7:
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
        
        # These use fabs because it is possile that the ball hit the wall behind the paddle, then the paddle, and the ball should not bounce back against the wall
        if pygame.sprite.collide_rect(players[0], theBall):
            theBall.speed[0] = math.fabs(theBall.speed[0])
        if pygame.sprite.collide_rect(players[1], theBall):
            theBall.speed[0] = - math.fabs(theBall.speed[0])
        
        DrawScore(screen, score, size)
        
        pygame.display.flip()
    
    
    return score
    
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