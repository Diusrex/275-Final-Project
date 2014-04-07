import pygame

# This file is the same throughout the program, reason there are multiple copies is to make is the games can, relatively easily, be ran individually

class Button(pygame.sprite.Sprite):
    def __init__(self, centerPosition, buttonSize, text, renderedText, textSize):
        """
        centerPosition will be the centre of where the button will be
        both center and size should be tuples
        
        renderedText is the text created from using pygame.font.SysFont, text is the string that renderedText was created from
        """
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        
        self.image = pygame.Surface(buttonSize)
        self.image.fill((255, 0, 0))
        
        textStartX = (buttonSize[0] - textSize[0]) / 2
        textStartY = (buttonSize[1] - textSize[1]) / 2
        
        self.image.blit(renderedText, (textStartX, textStartY))
        
        self.rect = self.image.get_rect()
        self.rect.center = centerPosition
    
    
    
    
    def HandleMousePress(self, mousePos):
        """
        Will check to see if this button was pressed. If it was, will return the text that was pressed on.
        
        Otherwise, will return None
        """
        
        if self.rect.collidepoint(mousePos):
            return self.text
        
        return None
        