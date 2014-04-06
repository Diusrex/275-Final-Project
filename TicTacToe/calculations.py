
def CheckIfWin(owners):
    """
    This function will work for both checking for winner among sections, and winner among boxes.
    
    owners should be a 1d array of size 9, which stores at each position who owns the box/section
    
    
    if there is a winner will return:
        (start, end) where start and end are the box #s that were on the start and end of the win
        Don't check in more detail because the player who just played is the only one who could win
        
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
    
def SectionCanBePlaced(boxes):
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
            
def CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, startBox, boxIncrease):
    """
    Will be used by calculatePlacedScore
    
    Will calculate the number of blocked and number of created lines over the given increase, and return them
    """
    
    temp = NumberInRow(boxesOwners, id, startBox, boxIncrease) + countIncrease
    
    if temp == 3:
        threeInRow = True
    
    if temp == 2:
        twoLine = True
    
    temp = NumberInRow(boxesOwners, otherId, startBox, boxIncrease)
    
    if temp == 2:
        blocksTwoLine = True
     
    return threeInRow, twoLine, blocksTwoLine
    

winGameScore = 1000
winSectionScore = 20

makeTwoLineScore = 5
blockTwoLineScore = 3

placedMiddleScore = 0
placedCornerScore = 0


def CalculateBoxScore(sectionOwners, sectionPos, boxesOwners, boxPos, id, otherId, multiplier, aboveScore):
    """
    This will calculate the score based on the following:
        1) If it wins this section score will be:
            1000 if wins the game (to completely render the other scores unneccesary
            8 otherwise
        
        2) If it creates a 2 line, will be a score of:
            4
            
        3) If it blocks an enemy 2 line, will be a score of:
            3
        
        4) Middle will be a score of 2, corners will 1, and rest will be 0
    
    The numbers could probably use some fiddling
    """
    # idIncrease represents whether or not the id has already been added to the box
    if boxesOwners[boxPos] != id:
        countIncrease = 1
    else:
        countIncrease = 0
        
    threeInRow = False
    twoLine = False
    blocksTwoLine = False
    
    score = 0
    

    if boxPos == 0:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 3)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 4)
        
        score += placedCornerScore
    
    
    elif boxPos == 1:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 1, 3)
    
    elif boxPos == 2:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 3)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 2)
        
        score += placedCornerScore
        
    elif boxPos == 3:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 3, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 3)

        
    elif boxPos == 4:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 3, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 1, 3)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 4)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 2)
        
        score += placedMiddleScore
        
    elif boxPos == 5:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 3, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 3)
        
    elif boxPos == 6:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 6, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 3)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 2)
        
        score += placedCornerScore
    
    elif boxPos == 7:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 6, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 1, 3)
    
    elif boxPos == 8:
        # All of the lines from this guy
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 6, 1)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 2, 3)
        threeInRow, twoLine, blocksTwoLine = CalculateAllWanted(boxesOwners, countIncrease, threeInRow, twoLine, blocksTwoLine, id, otherId, 0, 4)
        
        score += placedCornerScore
    
    
    
    # The only benefit to playing, is when this section is not owned, otherwise there is no point
    if sectionOwners[sectionPos] == 0:
        output = ""
        if threeInRow:
            sectionOwners[sectionPos] = id
            wins = CheckIfWin(sectionOwners)
            sectionOwners[sectionPos] = 0
            
            output += "Three in a row,"
            if wins:
                score += winGameScore
            else:
                score += winSectionScore
        
        if twoLine:
            output += "Two in a row,"
            score += makeTwoLineScore
            
        if blocksTwoLine:
            output += "Block"
            score += blockTwoLineScore
        
        #print(output)
    else:
        score = 0   
    
    return score * multiplier + aboveScore
    
    
    
def CalculateSectionScore(allSectionOwners, sectionPosition, multiplier, aboveScore):
    score = 0
    
    if allSectionOwners[sectionPosition] != 0:
        score -= 4
    
    # If cannot win off of this section, should also decrease
    # If can deny enemy with this section, should increase
    
    return score * multiplier + aboveScore