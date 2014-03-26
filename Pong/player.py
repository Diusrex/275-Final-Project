import pygame

class Player(pygame.sprite.Sprite):
    standardImage = pygame.image.load("basicPaddle.png")
    
    # Is up, not moving, down
    speed = (-10, 0, 10)
    
    def __init__(self, name, position, upKey, downKey):
        pygame.sprite.Sprite.__init__(self)
        
        self.upKey = upKey
        self.downKey = downKey
        
        self.image = Player.standardImage
        
        self.rect = self.image.get_rect()
        
        self.rect.center = position
        
        self.speed = 0
        
    def HandleKeyPress(self, keyId):
        if self.upKey == keyId:
            self.speed = Player.speed[0]
            print("Changed Speed")
            
        elif self.downKey == keyId:
            self.speed = Player.speed[2]
            print("Changed Speed")
            
    def HandleKeyRelease(self, keyId):
        if self.upKey == keyId:
            self.speed = Player.speed[1]
            
        elif self.downKey == keyId:
            self.speed = Player.speed[1]
            
    def update(self, timePassed):            
        self.rect.move_ip(0, self.speed * timePassed / 50)
        
    