import pygame
import random
import copy

# Use this import if this will be a subdirectory
import TicTacToe.calculations as calculations

"""
# Use this import if running the game individually

import calculations
  
"""

class BasePlayer:
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
    
    
    
    
    def ChoosePosition(self, allSectionContainers, allSectionOwners, sectionPositon, otherId):
        """
        This is a virtual function (which is why it will raise the below error
        
        If the player choose a box, then will return the position of that box. 
        
        Otherwise the user wants to quit, and will return None.
        
        When calling, do not copy the boxesInformation, the passed information will not be altered
        
        If the program is to quit, will return none
        
        Otherwise, will return a tuple containing:
            0: The section that was altered
            1: The box changed
        """
        raise NotImplementedError
        
        
        
        
        
        
class HumanPlayer(BasePlayer):
    def __init__(self, name, id, image):
        super().__init__(name, id, image)

        
    def ChoosePosition(self, allSections, allSectionOwners, sectionPositon, otherId):
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
                    if (allSections[sectionPositon].CanBeClickedIn()):
                        boxChanged = allSections[sectionPositon].HandleClicked(pos)
                        
                        if boxChanged != None:
                            return (sectionPositon, boxChanged)
                        
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

                    
                    
                    
                    
                    
                    
def SemiRandomPicker(possibleItems):
    """
    This function will pick one item and return it. The items will be a tuple in the pattern (section, box, score), so will be compare using [2].
    
    If there is at least one positive item, will pick randomly, with items that have a higher score being more likely to be picked.
    Otherwise, will pick randomly from all of the items with the highest score.

    """
    totalScore = 0
    
    for item in possibleItems:
        if item[2] > 0:
            totalScore += item[2]
    
    if totalScore > 0:
        randomNumber = random.randint(0, totalScore - 1)
        
        for item in possibleItems:
            if item[2] > 0:
                randomNumber -= item[2]
                if randomNumber <= 0:
                    return item
                    
    # All were non-positive
    highest = [possibleItems[0]]
    
    for item in possibleItems:
        # The second check is to avoid giving greater precedence to the first item
        if item[2] == highest[0][2] and item != highest[0]:
            highest.append(item)
        
        elif item[2] > highest[0][2]:
            highest = [item]
        
    return random.choice(highest)
    
    
    
    
    
    
class AIPlayerMiniMax(BasePlayer):
    """
    This player will use a varient of the MiniMax method
    
    A more complete description can be found in the readme in this directory.
    """
    def __init__(self, name, id, image,  currentMaxDepth, absoluteMaxDepth, boxScoring, sectionScoring, takeBest):
        """
        maxDepth is how deep this player will check
        overtime, the maxDepth will slowly increase, based on the count and increaseThreshold
        """
        super().__init__(name, id, image)
        self.maxDepth = currentMaxDepth
        self.absoluteMaxDepth = absoluteMaxDepth
        self.takeBest = takeBest
        self.count = 0
        self.increaseThreshold = 12
        self.boxScoring = boxScoring
        self.sectionScoring = sectionScoring
    
    
    
    
    
    def ChoosePosition(self, allSections, allSectionOwners, sectionPosition, otherId):
        """
        This player will calculate the score recursively using the function AIPlayerMiniMax.CalculateScore and calculations.CalculateBoxScore
        
        Will return a tuple containing:
            0: The section that was altered
            2: The box changed
        """
        self.count += 1
        if self.count >= self.increaseThreshold and self.maxDepth < self.absoluteMaxDepth:
            self.count = 0
            self.maxDepth += 1
        
        
        
        # Makes it easy to know who is going
        currentPlayer = 0
        ids = (self.id, otherId)
        
        # This means could create a bot more focused upon denying the oppenent, and one that is more aggresive
        multipliers = (1, -1)
        
        # These are related to how I want the highest score, and my opp wants the lowest score
            # The reason why these do not use SemiRandomPicker is because that would introduce too much variation, and could skew the choosing by a large amount
        decisionSelectors = (max, min)
        
        
        # Use this rather than allSections because it will be alot easier to simply copy a list, rather than copy a section
        allSectionBoxOwners = []
        for section in allSections:
            allSectionBoxOwners.append(section.GetOwnedBy())
        
        allPossiblePositions = calculations.GetAllCanBePlacedIn(allSectionBoxOwners[sectionPosition])
        
        
        # placementOptions is a list of tuples in form (section, box, score)
        placementOptions = []
        
        # The reason why this does not use CalculateSectionScore is because CalculateSectionScore only gives the best score, not the best position
        # Means the player can play in any spot, so will go through all sections and add their placable positions to placementOptions
        if allPossiblePositions == []:
            for sectionNum in range(9):
                allPossiblePositions = calculations.GetAllCanBePlacedIn(allSectionBoxOwners[sectionNum])
                
                for position in allPossiblePositions:
                    
                    score = self.CalculateBoxScore(allSectionOwners, allSectionBoxOwners, sectionNum, position, currentPlayer, ids, multipliers, decisionSelectors, 0, 0)
                    
                    
                    placementOptions.append((sectionNum, position, score))
                    
        # Means the player can only play in the current section (sectionPosition)
        else:
            for position in allPossiblePositions:
                score = self.CalculateBoxScore(allSectionOwners, allSectionBoxOwners, sectionPosition, position, currentPlayer, ids, multipliers, decisionSelectors, 0, 0)
                
                
                placementOptions.append((sectionPosition, position, score))
        
        
        # The choosing method for here can be changed
        if self.takeBest:
            choice = max(placementOptions, key=lambda item:item[2])
        else:
            choice = SemiRandomPicker(placementOptions)
        
        # Rest of program doesn't care about the score
        return choice[:2]
    
    
    
    
    
    def CalculateBoxScore(self, allSectionOwners, allSectionBoxOwners, sectionPosition, boxPosition, currentPlayer, ids, multipliers, decisionSelectors, aboveScore, depth):
        """
        Will use calculations.CalculateBoxScore, which is focused upon the position of the box within a square (including blocking the opponent and creating lines)
        
        After calculating it's own score, will then check to see if it should end (due to a player winning, or depth being reached).

        If it shouldn't end, will sreverse the currentPlayer, and call CalculateSectionScore on the section that would be moved to from selecting this box. 
        """
        score = calculations.CalculateBoxScore(allSectionOwners, sectionPosition, allSectionBoxOwners[sectionPosition], boxPosition, ids[currentPlayer], ids[1
 - currentPlayer], multipliers[currentPlayer], aboveScore, self.boxScoring)
        
        # Just to print out some information, shouldn't be enabled with an absoluteMaxDepth above 1, maybe 2
        #print("Section %d box %d, score of %d (above of %d) and multiplier of %d" % (sectionPosition, boxPosition, score, aboveScore, multipliers[currentPlayer]))
        
        if depth >= self.maxDepth:
            return score
        
        # Need to copy this list, otherwise will effect the caller, which would be very very bad
        allSectionBoxOwners = copy.deepcopy(allSectionBoxOwners)
        
        allSectionBoxOwners[sectionPosition][boxPosition] = ids[currentPlayer]
        
        # Copy allSectionBoxOwners, and set this section to ids[currentPlayer]
        if allSectionBoxOwners[sectionPosition] == 0:
            winner = calculations.CheckIfWin(allSectionBoxOwners[sectionPosition])
            
            if winner:
                # Unlike allSectionBoxOwners, this does not need to be deep copied, due to only being a 1d list
                allSectionOwners = allSectionOwners[:]
                allSectionOwners[sectionPosition] = ids[currentPlayer]
                
                # Check if won (because if did, then no need to check further)
                if calculations.CheckIfWin(allSectionOwners):
                    return score
                    
        # The other player will be able to use the score of the section, not the player that played into this box
        currentPlayer = 1 - currentPlayer
        
        # The boxPosition is the new sectionPosition
        return self.CalculateSectionScore(allSectionOwners, allSectionBoxOwners, boxPosition, currentPlayer, ids, multipliers, decisionSelectors, score, depth + 1)
    
    
        
        
        
    def CalculateSectionScore(self, allSectionOwners, allSectionBoxOwners, sectionPosition, currentPlayer, ids, multipliers, decisionSelectors, aboveScore, depth):
        """
        Will use calculations.CalculateSectionScore, which is focused upon the usefulness of a section, based upon the game itself.
        
        Also, will then calculate the score of each of its possible boxes, and use the one most favourable to the currentPlayer.
        
        If the sectionPosition cannot be played in, will instead return the score of the most favourable of all of the sections, by calling CalculateSectionScore on all sections that may be placed in
        """
        scores = []
        
        if calculations.SectionCanBePlaced(allSectionBoxOwners[sectionPosition]):
            sectionScore = calculations.CalculateSectionScore(allSectionOwners, sectionPosition, allSectionBoxOwners[sectionPosition], ids[currentPlayer], ids[1 - currentPlayer], multipliers[currentPlayer], aboveScore, self.sectionScoring)

            allPossibleBoxes = calculations.GetAllCanBePlacedIn(allSectionBoxOwners[sectionPosition])
            

            for box in allPossibleBoxes:
                scores.append(self.CalculateBoxScore(allSectionOwners, allSectionBoxOwners, sectionPosition, box, currentPlayer, ids, multipliers, decisionSelectors, sectionScore, depth))
            
             
        else:
            # Can be placed anywhere
            for section in range(9):
                # Need to make sure that they may be placed in before, otherwise would create an infinite loop
                if calculations.SectionCanBePlaced(allSectionBoxOwners[section]):
                    scores.append(self.CalculateSectionScore(allSectionOwners, allSectionBoxOwners, section, currentPlayer, ids, multipliers, decisionSelectors, aboveScore, depth))
        
        # Means it was a tie
        if len(scores) == 0:
            return 0
            
        # Want to select the best possible score
        return decisionSelectors[currentPlayer](scores)
