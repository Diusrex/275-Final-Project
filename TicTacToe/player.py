
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