def CheckIfWin(owners):
    """
    This function will work for both checking for winner among sections, and winner among boxes.
    
    owners should be a 1d array of size 9, which stores at each position who owns the box/section
    
    if there is a winner will return:
        (start, end) where start and end are the #s that were on the start and end of the win
    
    This must be called every time something is changed, because this function does not check to see who won, just if there was a winner
        
    otherwise, will return None
    """
    # Far easier to hardcode all of the checks, and more readable
    
    # Horizontal
    if owners[0] == owners[1] and owners[1] == owners[2] and owners[0] != 0:
        return (0, 2)
        
    if owners[3] == owners[4] and owners[4] == owners[5] and owners[3] != 0:
        return (3, 5)
        
    if owners[6] == owners[7] and owners[7] == owners[8] and owners[6] != 0:
        return (6, 8)
    
    # Vertical
    if owners[0] == owners[3] and owners[3] == owners[6] and owners[0] != 0:
        return (0, 6)
    
    if owners[1] == owners[4] and owners[4] == owners[7] and owners[1] != 0:
        return (1, 7)
        
    if owners[2] == owners[5] and owners[5] == owners[8] and owners[2] != 0:
        return (2, 8)
    
    # Diagonal
    if owners[0] == owners[4] and owners[4] == owners[8] and owners[0] != 0:
        return (0, 8)
        
    if owners[2] == owners[4] and owners[4] == owners[6] and owners[2] != 0:
        return (2, 6)
    
    return None
    
    
    
    
    
def SectionCanBePlacedIn(boxes):
    """
    Is pretty basic, probably not needed to be a function
    """
    return (0 in boxes)


    
    
    
def GetAllCanBePlacedIn(boxes):
    """
    The reason why this function does not belong to section is because the sections are not used within the AiPlayer function recursively, due to too high copy costs
    """
    toReturn = []
    for pos in range(9):
        if boxes[pos] == 0:
            toReturn.append(pos)
    
    return toReturn

    
    
    
    
def NumberInRow(boxesOwners, id, startBox, boxIncrease):
    """
    Will return the number of boxes in this row that the same as the id. Should not include added box.
    
    If there is a box that is of a different id, then will return 0, because there is no use for the others
    """
    number = 0
    
    for spot in range(3):
        if boxesOwners[startBox + spot * boxIncrease] == id:
            number += 1
        elif boxesOwners[startBox + spot * boxIncrease] != 0:
            return 0
            
    return number

    
    
    
    
class OccuranceInfo:
    """
    Will store information about how many there are in a row, and how many a pos will block
    
    ThreeInRow is not a count because it doesn't matter
    """
    def __init__(self):
        self.threeInRow = False
        self.twoLineCount = 0
        self.blocksTwoLineCount = 0

        
        
        
        
def CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, startBox, boxIncrease):
    """
    Will be used by calculatePlacedScore
    
    Will calculate the number of blocked and number of created lines over the given increase, and store the information in occuranceInfo
    """
    
    temp = NumberInRow(boxesOwners, id, startBox, boxIncrease) + countIncrease
    
    if temp == 3:
        occuranceInfo.threeInRow = True
    
    if temp == 2:
        occuranceInfo.twoLineCount += 1
    
    temp = NumberInRow(boxesOwners, otherId, startBox, boxIncrease)
    
    if temp == 2:
        occuranceInfo.blocksTwoLineCount += 1
    




def CalculateBoxScore(sectionOwners, sectionPos, boxesOwners, boxPos, id, otherId, multiplier, aboveScore, boxScoring):
    """
    This will calculate the score based on the following (if the section has not be won yet):
        1) If it wins this section score will be:
            boxScoring.winGameScore if wins the game (to completely render the other scores unneccesary
            boxScoring.winSectionScore otherwise
        
        2) If it creates a 2 line, will be a score of:
            boxScoring.makeTwoLineScore per line created
            
        3) If it blocks an enemy 2 line, will be a score of:
            boxScoring.blockTwoLineScore per line blocked
        
        4) Middle will be a score of boxScoring.placedMiddleScore, corners will be boxScoring.placedCornerScore, and rest will be boxScoring.placedOtherScore
    Will also add the aboveScore to this new score
    """
    # idIncrease represents whether or not the id has already been added to the box
    if boxesOwners[boxPos] != id:
        countIncrease = 1
    else:
        countIncrease = 0
    
    occuranceInfo = OccuranceInfo()
    
    score = 0
    
    # Only time that setting up rows and such matters
    if sectionOwners[sectionPos] == 0:
        # This is for determining how important the current boxPos is within the section, based on if there are any three in a rows and such
            # I really wish python had switch statements...
        # increase of 1 is horizontal, increase of 3 is vertical, increase of 2 or 4 a different diagonals
        if boxPos == 0:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            score += boxScoring.placedCornerScore
        
        
        elif boxPos == 1:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            score += boxScoring.placedOtherScore
        
        elif boxPos == 2:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += boxScoring.placedCornerScore
            
        elif boxPos == 3:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            score += boxScoring.placedOtherScore

            
        elif boxPos == 4:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += boxScoring.placedMiddleScore
            
        elif boxPos == 5:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            score += boxScoring.placedOtherScore
            
        elif boxPos == 6:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += boxScoring.placedCornerScore
        
        elif boxPos == 7:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            score += boxScoring.placedOtherScore
        
        elif boxPos == 8:
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            CalculateAllWanted(boxesOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            score += boxScoring.placedCornerScore

        if occuranceInfo.threeInRow:
            sectionOwners[sectionPos] = id
            wins = CheckIfWin(sectionOwners)
            sectionOwners[sectionPos] = 0
            

            if wins:
                score += boxScoring.winGameScore
            else:
                score += boxScoring.winSectionScore
        
        
        score += boxScoring.makeTwoLineScore * occuranceInfo.twoLineCount
            

        score += boxScoring.blockTwoLineScore * occuranceInfo.blocksTwoLineCount   
    
    return score * multiplier + aboveScore
    
    
    
    


def CanBeWon(owners, otherId):
    """
    Will calculate if there is at least one line that does not contain other's id.
    """
    # Horizontal
    if owners[0] != otherId and owners[1] != otherId and owners[2] != otherId:
        return True
        
    if owners[3] != otherId and owners[4] != otherId and owners[5] != otherId:
        return True
        
    if owners[6] != otherId and owners[7] != otherId and owners[8] != otherId:
        return True
    
    # Vertical
    if owners[0] != otherId and owners[3] != otherId and owners[6] != otherId:
        return True
    
    if owners[1] != otherId and owners[4] != otherId and owners[7] != otherId:
        return True
        
    if owners[2] != otherId and owners[5] != otherId and owners[8] != otherId:
        return True
    
    # Diagonal
    if owners[0] != otherId and owners[4] != otherId and owners[8] != otherId:
        return True
        
    if owners[2] != otherId and owners[4] != otherId and owners[6] != otherId:
        return True
        
    # All contain at least 1
    return False
    
    
    
    
    
def CalculateSectionScore(allSectionOwners, sectionPosition, boxesOwners, id, otherId, multiplier, aboveScore, sectionScoring):
    """
    This will calculate the score based on the following:
        a) If this section has been won, will reduce the score by sectionScoring.unableToEffectGameScore
            Same with if it is not possible to win the section
            
        b) Otherwise:
                
            1) If by winning this section, the player would win the game, will add a score of sectionScoring.mayWinImmediately
            
            2) If, by winning this section, will creates a 2 line of won sections, will be a score of:
                sectionScoring.makeTwoLineScore per line created
                
            3) If, by winning this section, will block a 2 line of opponent won sections, will be a score of:
                sectionScoring.blockTwoLineScore per line blocked
            
            4) Middle section will also add a score sectionScoring.ownMiddleScore, corners will be sectionScoring.ownCornerScore, and rest will be sectionScoring.ownOtherScore
    
    Will also add the aboveScore to this new score
    """
    score = 0
    
    # Don't want to play in a section that is owned by someone else
    if allSectionOwners[sectionPosition] != 0:
        score -= sectionScoring.unableToEffectGameScore
    
    elif not CanBeWon(boxesOwners, otherId):
        score -= sectionScoring.unableToEffectGameScore
    
    else:
        countIncrease = 1
        
        occuranceInfo = OccuranceInfo()
        
        # This is for determining how important the current section is within the game, based on how many allied sections create a line with it, and how many it other sections it can block
            # I really wish python had switch statements...
        # increase of 1 is horizontal, increase of 3 is vertical, increase of 2 or 4 a different diagonals
        if sectionPosition == 0:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            score += sectionScoring.ownCornerScore
        
        
        elif sectionPosition == 1:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            score += sectionScoring.ownOtherScore
        
        
        elif sectionPosition == 2:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += sectionScoring.ownCornerScore
            
            
        elif sectionPosition == 3:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            score += sectionScoring.ownOtherScore

            
        elif sectionPosition == 4:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += sectionScoring.ownMiddleScore
            
            
        elif sectionPosition == 5:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 3, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            score += sectionScoring.ownOtherScore
            
            
        elif sectionPosition == 6:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 3)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 2)
            
            score += sectionScoring.ownCornerScore
        
        
        elif sectionPosition == 7:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 1, 3)
            
            score += sectionScoring.ownOtherScore
        
        
        elif sectionPosition == 8:
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 6, 1)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 2, 3)
            
            CalculateAllWanted(allSectionOwners, countIncrease, occuranceInfo, id, otherId, 0, 4)
            
            score += sectionScoring.ownCornerScore
        
        
        if occuranceInfo.threeInRow:
            score += sectionScoring.mayWinImmediately
        
        score += sectionScoring.makeTwoLineScore * occuranceInfo.twoLineCount
            

        score += sectionScoring.blockTwoLineScore * occuranceInfo.blocksTwoLineCount   
    
    return score * multiplier + aboveScore