import pygame
from pygame.locals import *
import pygame.time
import math

import random

# These are the imports for when running from base menu
import Pong.drawFunctions as drawFunctions
import Pong.ball as ball

from Pong.player import Player

"""
# Use these imports when just want to run this game
import drawFunctions
import ball

from player import Player
"""

class Scores():
    """
    Stores all of the scores. An instance will be passed to the ball class so it can easily update the score.
    
    Ball should treat the members of this class as private
    """
    def __init__(self):
        self.leftPlayerScore = 0
        
        self.rightPlayerScore = 0
        
        
    def HitLeftSide(self):
        self.rightPlayerScore += 1
    
    
    def HitRightSide(self):
        self.leftPlayerScore += 1
        
        
        
        
def RunGame(screen, screenSize):    
    """
    If there was a winner, will leave the screen drawn and return the score info
    
    If the user wanted to exit, then will return None
    """
    
    # Setting up the game
    
    # These are store inside of the allSprites as well, but are needed to be accessible for program logic
    players = [Player("Player 1", (12, screenSize[1] / 2), K_w, K_s),
               Player("Player 2", (screenSize[0] - 15, screenSize[1] / 2), K_UP, K_DOWN)]
    
    allSprites = pygame.sprite.Group()
    allSprites.add(players[0])
    allSprites.add(players[1])
    
    score = Scores()
    
    # Want the overall speed to be the same, but want the angle to be random. It can also start going in any direction
    xSpeed = random.randint(70, 90)
    xNegative = random.randint(0, 1)
    if xNegative == 1:
        xSpeed *= -1
        
    ySpeed = math.sqrt(12800 - xSpeed ** 2)
    yNegative = random.randint(0, 1)
    if yNegative == 1:
        ySpeed *= -1
    
    # Spawn the ball in the middle of the screen
    theBall = ball.Ball((screenSize[0] // 2, screenSize[1] // 2), [xSpeed, ySpeed], score)
    
    allSprites.add(theBall)    
    
    clock = pygame.time.Clock()
    
    # Run the game until one user has a score of 7, in which case they will win
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
        
        # Need to update all of the sprites based on the time passed, then redraw them
        time = clock.tick()
        
        allSprites.update(time / 100, screenSize)
        
        allSprites.draw(screen)
        
        
        # These use fabs because it is possible that the ball hit the wall behind the paddle, then the paddle, and since the ball should not bounce back against the wall, cannot simply multiply the speed by -1
        if pygame.sprite.collide_rect(players[0], theBall):
            theBall.speed[0] = math.fabs(theBall.speed[0])
            theBall.RandomlyIncreaseSpeed()
            
        if pygame.sprite.collide_rect(players[1], theBall):
            theBall.speed[0] = - math.fabs(theBall.speed[0])
            theBall.RandomlyIncreaseSpeed()
            
        drawFunctions.DrawScore(screen, score, screenSize)
        
        pygame.display.flip()
    
    
    return score
    
