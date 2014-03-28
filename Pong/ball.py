import pygame

class Ball(pygame.sprite.Sprite):
    standardImage = pygame.Surface((15, 15))
    
    def __init__(self, position, movement, impactHandler):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = Ball.standardImage
        self.image.fill((255, 255, 255))
        
        self.rect = self.image.get_rect()
        self.rect.center = position
        
        self.speed = movement
        
        self.impactHandler = impactHandler
        
        
        
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