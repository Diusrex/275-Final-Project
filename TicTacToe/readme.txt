The game consists of a large Tic Tac Toe board which will consist of 9 mini Tic Tac Toe boards. The mini Tic Tac Toe boards will be referred to as 'sections', while the spots inside of a mini Tic Tac Toe board will be called a box.
    This naming is also used within the code

The Game:
    (There is also a description with pictures inside of the game itself)
    
    The first player starts playing in the center section.
    When a player plays in a box, the other player will then play in the section in the same position as that box
        ex: If I were to play in the top left box inside of a section (the specific section doesn't matter), the other player would then play within the top left section
    
    If it is impossible for a player to play within a section due to it being full, then that player can play in any of the sections.
    
    To win a section, you must be the first one to get three boxes in a row, like in normal Tic Tac Toe. Winning a section is pernament, the other player cannot win it back.
    
    To win the game, you must get three sections in a row, like in normal Tic Tac Toe.
    
AI descripion:
    The ai is based on minimax. This means that, when choosing its next move, it assumes that the other player will minimize the score of this ai, and it will attempt to maximize its score. When determining score, any score the other player may accrue is negative (because their score will hurt this bots score), and any score this player may gain is positive.
        My solution varies from minimax though, because as it recurses down the moves, the score from nodes (boxes and sections) that were traversed from above will be added to the score of the current node. This means that when a node returns its score (due to reaching maxDepth), that score will not be altered (although it may be ignored due to there being better scores for the nearest section).
    
    There are two configurations for the AI: max and semirandom (often refered to as best). The only difference is when all of the scores for future moves have been calculated, and the AI has to choose from among its currently possible moves (one of which it will return as its move), the max AI (which has setBest best be true), will pick the move with the higest score. A semirandom ai will pick from among the positive values, randomly with the ones with a higher score being more likely (as described in the comments for the function SemiRandomPicker).
        The default ai uses SemiRandomPicker.
    
    
    The reason why the maxDepth (which determines how many moves the player will look forward) is relatively low, is because the first depth checks upto 9 positions, the second checks up to 81 distinct positions, and the third checks up to 729 distinct positions. These are distinct becuase what was played before these spots were chosen will be different. So the complexity is roughly 9^maxDepth.
        However, over time, the maxDepth is increased because there will simply not be that many possible moves, because the 
    
    The ai will look 3 to 6 moves ahead, depending on how far into the game it is. However, becuase the scoring method could use improvements, the ai is beatable
    
    The ai will recursively determine the score for each initial starting box, with the following pattern:
        For each box that may be played in box, will call CalculateBoxScore. This fucntion will calculate the score of that box within the section that it is in, such as if it will block an opponents two in a row, if it will win the section for this player, etc.
        
        Then, if the recursion depth has not been reached, CalculateBoxScore will call CalculateSectionScore on the section that this box will cause the next player to play in, and will change the player.
        
        CalculateSectionScore will calculate the score the section it is in using calculations.CalculateSectionScore, and will then call CalculateBoxScore on all boxes that may be placed in. It will then determine which of the boxes is the best to play in for the player who would be able to plays (if it aligns best or worst with their goal) and will return the best score for that player.
        
        All of these functions will use the above score to influence their score, and will return the final score of their branch

    I have included a file call Results.txt in this directory that lists some of my results against the AI.
    
    If you wish to have two AI's play each other, within main.RunGame, there is a commented out line for creating playerOne as an AIPlayer. Just need to uncomment that line, and run the game in single player mode. Without changing either line, the first player will be the 'best' type ai, and the second player will be of the 'semirandom; type.
    
AI Improvements:
    One of the biggest improvements that could likely be used on the ai is improving the values of numbers used within calculations.CalculateBoxScore and calculations.CalculateSectionScore:
        These scores are relatively arbitrary, and by adjusting them the ai would likely perform better.
        By altering the scores, and the multiplyer, it is possible to create bots with different characteristics, like making some very aggressive, and making others very defensive etc.
    
    Adding more diverse checks withing calculations.CalculateBoxScore and calculations.CalculateSectionScore.
        This is because while the checks are very useful, I am sure that there are more checks that could be performed that would increase the strength of the ai
    
    Making so that different ai's can use different CalculateBoxScore functions.
        Could mostly be accomplished by changing scores
    
    Using Alpha–beta pruning instead of minimax.
        This would increase the number of moves able to look ahead by 1 or 2, which will have an impact on how well the ai does.
    
    Having different difficulties.
        This could be accomplished by changing the absoluteMaxDepth, altering boxScoring and sectionScoring, or running altered versions of calculations.CalculateBoxScore and calculations.CalculateSectionScore
    
    
The reason why I had the tic tac toe boxes be stored as a single 1d list, rather than a 2d list, was for ease of use.
    It is quite simple to convert back and forth between using 1d coordinate and 2d coordinate inside of the list (below) but it is easier to iterate through all of the items.
    
    Makes it far simpler for functions like CanBeClickedIn within boxContainer, and makes the code for the ai easier to write.
    
    Also decreases the complexity of the code by making it so there is no need to pass around tuples/lists contining the x and y pos, but instead use a single int.
    
    The conversions are:
        x = pos % 3, y = pos // 3
            when going from 1d to 2d
        
        pos = y * 3 + x 
            when going from 2d to 1d