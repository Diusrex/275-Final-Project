class Coordinate:
    """
    Access using .x or .y.
    Replaces using a list or tuple to store coordinates to increase readability of the code.
        Don't use this in other games because they need to work using rect, while this game's drawing is based off of grid location and some math.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def Copy(self):
        return Coordinate(self.x, self.y)
        
        
    def __str__(self):
        return "Coordinate: " + str(self.x) +' ' + str(self.y)