import pygame
import math
import random

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
    
    def ChoosePosition(self, allSectionContainers, allSectionOwners, currentSection, otherId):
        """
        This is a virtual function.
        
        If the player choose a box, then will return the position of that box. 
        
        Otherwise the user wants to quit, and will return None.
        
        When calling, do not copy the boxesInformation, that can be done later if this classes wants to do so
        
        If the program is to quit, will return none
        
        Otherwise, will return a tuple containing:
            0: The section that was altered
            1: The box changed
            
        """
        raise NotImplementedError
        
class HumanPlayer(Player):
    def __init__(self, name, id, image):
        super().__init__(name, id, image)
        
    def ChoosePosition(self, allSections, allSectionOwners, currentSectionNum, otherId):
        """
        Will just wait until the user presses on a valid position
        """
        while True:
            ev = pygame.event.get()
            
            for event in ev:
                # Means user wanted to press button here
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    
                    # If it was a valid press, input will be a tuple containing (boxStatus, boxPressedIn)
                    if (allSections[currentSectionNum].CanBeClickedIn()):
                        boxChanged = allSections[currentSectionNum].HandleClicked(pos)
                        
                        if boxChanged != None:
                            return (currentSectionNum, boxChanged)
                        
                    # It is possible that it is impossible to place in current box, in which case any box is valid
                    else:
                        for sectionPos in range(9):
                            boxChanged = allSections[sectionPos].HandleClicked(pos)
                            if boxChanged != None:
                                return (sectionPos, boxChanged)
                    
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                
                elif event.type == pygame.QUIT:
                    return None