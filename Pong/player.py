import pygame

class Player(pygame.sprite.Sprite):
    standardImage = pygame.Surface((15, 60))
    
    # Is up, not moving, down. Is the number of pixels per tenth of a second
    speed = (-60, 0, 60)
    
    
    def __init__(self, name, position, upKey, downKey):
        pygame.sprite.Sprite.__init__(self)
        
        self.upKey = upKey
        self.downKey = downKey
        
        self.image = Player.standardImage
        self.image.fill((255, 255, 255))
        
        self.rect = self.image.get_rect()
        
        self.rect.center = position
        
        self.speed = 0
        
        
        
    def HandleKeyPress(self, keyId):
        """
        This wmust be called every time the user presses a button, because the up/down keys could be anything
        """
        if self.upKey == keyId:
            self.speed = Player.speed[0]
            
        elif self.downKey == keyId:
            self.speed = Player.speed[2]
           

           
    def HandleKeyRelease(self, keyId):
        """
        This wmust be called every time the user releases a button, because the up/down keys could be anything
        """
        if self.upKey == keyId:
            self.speed = Player.speed[1]
            
        elif self.downKey == keyId:
            self.speed = Player.speed[1]
          

          
    def update(self, timePassed, screenSize):       
        """
        Should be called everytime the screen will be updated.
        The timePassed parameter should be in tenths of a second, otherwise the paddle will travel far too quickly
        """
        
        self.rect.move_ip(0, self.speed * timePassed)
        
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= screenSize[1]:
            self.rect.bottom = screenSize[1]
    