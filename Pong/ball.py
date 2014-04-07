import pygame
import math
import random

class Ball(pygame.sprite.Sprite):
    standardSize = 15
    
    def __init__(self, position, movement, impactHandler):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((Ball.standardSize, Ball.standardSize))
        
        # This makes it so that only the white circle, radius Ball.standardSize // 2, is drawn while rest is ignored
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (Ball.standardSize // 2, Ball.standardSize // 2), Ball.standardSize // 2)
        
        self.rect = self.image.get_rect()
        self.rect.center = position
        
        self.speed = movement
        
        self.impactHandler = impactHandler
        
        
        
        
    def RandomlyIncreaseSpeed(self):
        """
        Will increase the speed of this ball.
        This function is very arbitrary with the numbers it uses, but it seems to work
        """
        # Should not increase beyond this point (yes it is arbitrary)
        if self.speed[0] ** 2 + self.speed[1] ** 2 > 100000:
            return
            
        # These are to make it so that the increases can be added to speed without danger of decreasing speed
        xMultiplyer = self.speed[0] / math.fabs(self.speed[0])
        yMultiplyer = self.speed[1] / math.fabs(self.speed[1])
        
        xIncrease = random.randint(0, 4) * xMultiplyer
        yIncrease = random.randint(0, 4) * yMultiplyer
        
        self.speed[0] += xIncrease
        self.speed[1] += yIncrease
        
        
        
        
        
    def update(self, timePassed, screenSize):
        """
        Time passed will be tenths of a second
        """
        self.rect.move_ip(self.speed[0] * timePassed, self.speed[1] * timePassed)
        
        if (self.rect.top < 0):
            self.rect.top = 0
            self.speed[1] *= -1
        
        elif self.rect.bottom > screenSize[1]:
            self.rect.bottom = screenSize[1]
            self.speed[1] *= -1
        
        if self.rect.left <= 0:
            # Alert that has scored
            self.impactHandler.HitLeftSide()
            self.rect.left = 0
            self.speed[0] *= -1
            
        elif self.rect.right > screenSize[0]:
            # Aler that has scored
            self.impactHandler.HitRightSide()
            self.rect.right = screenSize[0]
            self.speed[0] *= -1