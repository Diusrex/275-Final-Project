
class Coordinate:
    """
    Access using .x or .y.
    Replaces using a list or tuple to store coordinates (which I don't like)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Copy(self):
        return Coordinate(self.x, self.y)
        
    def __str__(self):
        return "Coordinate: " + str(self.x) +' ' + str(self.y)