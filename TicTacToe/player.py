import pygame

class Player:
    def __init__(self, name, id, image):
        """
        id must not be 0, if it is then the program will fail miserably
        
        Image should be the image associated with this player
        """
        if id == 0:
            raise ValueError('The id CANNOT be 0')
            
        self.name = name
        self.image = image
        self.id = id
    
    def ChoosePosition(self, allSectionContainers, allSectionOwners, currentSection):
        """
        This is a virtual function.
        
        If the player choose a box, then will return the position of that box. 
        
        Otherwise the user wants to quit, and will return None.
        
        When calling, do not copy the boxesInformation, that can be done later if this classes wants to do so
        """
        raise NotImplementedError
        
class HumanPlayer(Player):
    def __init__(self, name, id, image):
        super().__init__(name, id, image)
        
    def ChoosePosition(self, allSectionContainers, allSectionOwners, currentSection):
        """
        Will just wait until the user presses on a valid position
        """
        while True:
            ev = pygame.event.get()
            
            for event in ev:
                # Means user wanted to press button here
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    
                    # if it was a valid press, input will be a tuple containing (boxStatus, boxPressedIn)
                    if (allSectionContainers[currentSection].CanBeClickedIn()):
                        input = allSectionContainers[currentSection].HandleClicked(pos, self)
                    
                    # It is possible that it is impossible to place in current box, in which case any box is valid
                    else:
                        for section in allSectionContainers:
                            temp = section.HandleClicked(pos, self)
                            if temp != None:
                                input = temp
                    
                    
                    if input != None:
                        return input
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                
                elif event.type == pygame.QUIT:
                    return None