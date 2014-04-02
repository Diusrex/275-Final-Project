import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, centerPosition, size, text, renderedText, textSize):
        """
        center position will be the centre of where the button will be
        both center and size should be tuples
        
        renderedText is the text rendered by pygame.font.SysFont, text is the text that renderedText was created from
        """
        
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        
        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))
        
        textStartX = (size[0] - textSize[0]) / 2
        textStartY = (size[1] - textSize[1]) / 2
        
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
        