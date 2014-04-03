# EDIT: Will probably want

def CheckIfWin(allBoxOwners):
    """
    allBoxOwners should be a 1d array of size 9, which stores at each position who owns the current box
    should also be in the format [y * 3 + x], but that isn't completely necessary
    
    will return:
        (0) if no one won
        (playerId, (start, end)) where start and end are the box #s that were on the start and end of the win
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