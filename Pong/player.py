import pygame

class Player(pygame.sprite.Sprite):
    standardImage = pygame.Surface((15, 60))
    
    # Is up, not moving, down
    speed = (-30, 0, 30)
    
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
        if self.upKey == keyId:
            self.speed = Player.speed[0]
            
        elif self.downKey == keyId:
            self.speed = Player.speed[2]
            
    def HandleKeyRelease(self, keyId):
        if self.upKey == keyId:
            self.speed = Player.speed[1]
            
        elif self.downKey == keyId:
            self.speed = Player.speed[1]
            
    def update(self, timePassed, screenSize):            
        self.rect.move_ip(0, self.speed * timePassed)
        
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= screenSize[1]:
            self.rect.bottom = screenSize[1]
    