
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
    
def WillWin(owners, positionToCheck, playerId):
    pass
    
def CanWin(owners, playerId):
    pass