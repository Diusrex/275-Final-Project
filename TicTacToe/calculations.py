
# Should improve the code of this, there are only 8 different win conditions
def CheckIfWin(allBoxOwners):
    """
    allBoxOwners should be a 1d array of size 9, which stores at each position who owns the current box
    should also be in the format [y * 3 + x], but that isn't completely necessary
    
    will return:
        (0) if no one won
        (playerId, (start, end)) where start and end are the box #s that were on the start and end of the win
    """
    
    winner = 0
    # Horizontal
    if allBoxOwners[0] == allBoxOwners[1] and allBoxOwners[1] == allBoxOwners[2] and allBoxOwners[0] != 0:
        return (allBoxOwners[0], (0, 2))
        
    if allBoxOwners[3] == allBoxOwners[4] and allBoxOwners[4] == allBoxOwners[5] and allBoxOwners[3] != 0:
        return (allBoxOwners[3], (3, 5))
        
    if allBoxOwners[6] == allBoxOwners[7] and allBoxOwners[7] == allBoxOwners[8] and allBoxOwners[6] != 0:
        return (allBoxOwners[6], (6, 8))
    
    # Vertical
    if allBoxOwners[0] == allBoxOwners[3] and allBoxOwners[3] == allBoxOwners[6] and allBoxOwners[0] != 0:
        return (allBoxOwners[0], (0, 6))
    
    if allBoxOwners[1] == allBoxOwners[4] and allBoxOwners[4] == allBoxOwners[7] and allBoxOwners[1] != 0:
        return (allBoxOwners[1], (1, 7))
        
    if allBoxOwners[2] == allBoxOwners[5] and allBoxOwners[5] == allBoxOwners[8] and allBoxOwners[2] != 0:
        return (allBoxOwners[2], (2, 8))
    
    # Diagonal
    if allBoxOwners[0] == allBoxOwners[4] and allBoxOwners[4] == allBoxOwners[8] and allBoxOwners[0] != 0:
        return (allBoxOwners[0], (0, 8))
        
    if allBoxOwners[2] == allBoxOwners[4] and allBoxOwners[4] == allBoxOwners[6] and allBoxOwners[2] != 0:
        return (allBoxOwners[2], (2, 6))
    
    return (0,)
    """
    for dimension in range(3):
        id = allBoxOwners[dimension * 3]
        
        same = True
        
        # Horizontal
        for x in range(1, 3):
            if allBoxOwners[dimension * 3 + x] != id:
                same = False
        
        if same and id != 0:
            return (id, (dimension * 3, dimension * 3 + 2))
            
        # Vertical
        id = allBoxOwners[dimension]
        same = True
        for y in range(1, 3):
            if allBoxOwners[y * 3 + dimension] != id:
                same = False
    
        if same and id != 0:
            return (id, (dimension, 2 * 3 + dimension))
    
    topLeftId = allBoxOwners[0]
    topRightId = allBoxOwners[2]
    
    topLeftSame = True
    topRightSame = True
    
    for spot in range(1, 3):
        if (allBoxOwners[spot * 4] != topLeftId):
            topLeftSame = False
        
        if (allBoxOwners[2 + spot * 2] != topRightId):
            topRightSame = False
     
    if topLeftSame and topLeftId != 0:
        return (topLeftId, (0, 8))
    
    if topRightSame and topRightId != 0:
        return (topRightId, (2, 6))
    
    # Need to return a tuple
    return (0,)
    """
    
def GetSpotsToWin(owner, playerId):
    pass