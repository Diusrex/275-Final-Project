The Game:
    (There is also a description with pictures inside of the game itself)
    The game consists of a large Tic Tac Toe board which will consist of 9 mini Tic Tac Toe boards. The mini Tic Tac Toe boards will be referred to as 'sections', while the spots inside of a mini Tic Tac Toe board will be called a box.
    
    The first player starts playing in the center section.
    When a player plays in a box, the other player will then play in the section in the same position as that box
        ex: If I were to play in the top left box inside of a section (the specific section doesn't matter), the other player would then play within the top left section
    
    If it is impossible for a player to play within a section due to it being full, then that player can play in any of the sections.
    
    To win a section, you must be the first one to get three boxes in a row, like in normal Tic Tac Toe. Winning a section is pernament, the other player cannot win it back.
    
    To win the game, you must get three sections in a row, like in normal Tic Tac Toe.
    
Basic Program flow:



The reason why I had the tic tac toe boxes be stored as a single 1d list, rather than a 2d list, was for ease of use.
    It is quite simple to convert back and forth between using 1d coordinate and 2d coordinate inside of the list (below) but it is easier to iterate through all of the items.
    
    Makes it far simpler for functions like CanBeClickedIn within boxContainer, and makes the code for the ai easier to write.
    
    Also decreases the complexity of the code by making it so there is no need to pass around tuples/lists contining the x and y pos, but instead use a single int.
    
    The conversions are:
        x = pos % 3, y = pos // 3
            when going from 1d to 2d
        
        pos = y * 3 + x 
            when going from 2d to 1d