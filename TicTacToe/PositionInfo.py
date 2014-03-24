class PositionInfo:
    """
    This class's sole purpose is to store position information easily, rather than have it be scattered among 4 or 5 different lists
    
    """
    
    def __init__(self, startX, startY):
        self.startPosX = [startX, -1, -1, -1]
        self.startPosY = [startY, -1, -1, -1]
        
        # The third value in these is just for ease, will be removed
        self.lineSideStartX = [-1, -1, -1]
        self.lineSideStartY = [-1, -1, -1]
        
        self.lineStartX = -1
        self.lineStartY = -1
        
        self.lineLengthX = -1
        self.lineLengthY = -1