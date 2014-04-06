class BoxScoring:
    """
    May treat all variables as being public. This is simply a container for all of the score types.
    
    The name of each variable corresponds to when it would be added to the score in calculations.CalculateBoxScore.
    """
    
    def __init__(self, winGameScore, winSectionScore, makeTwoLineScore, blockTwoLineScore, placedMiddleScore, placedCornerScore, placedOtherScore):
        self.winGameScore = winGameScore
        self.winSectionScore = winSectionScore

        self.makeTwoLineScore = makeTwoLineScore
        self.blockTwoLineScore = blockTwoLineScore

        self.placedMiddleScore = placedMiddleScore
        self.placedCornerScore = placedCornerScore
        self.placedOtherScore = placedOtherScore

        
        
# Simply the standard design for scoring
defaultBoxScoring = BoxScoring(1000, 20, 5, 3, 0, 0, 0)




class SectionScoring:
    """
    May treat all variables as being public. This is simply a container for all of the score types.
    
    The name of each variable corresponds to when it would be added to the score in calculations.CalculateBoxScore.
    """
    
    def __init__(self, unableToEffectGameScore, mayWinImmediately, makeTwoLineScore, blockTwoLineScore, ownMiddleScore, ownCornerScore, ownOtherScore):
        self.unableToEffectGameScore = unableToEffectGameScore
        self.mayWinImmediately = mayWinImmediately
        self.makeTwoLineScore = makeTwoLineScore
        self.blockTwoLineScore = blockTwoLineScore
        self.ownMiddleScore = ownMiddleScore
        self.ownCornerScore = ownCornerScore
        self.ownOtherScore = ownOtherScore
    
    
    
defaultSectionScoring = SectionScoring(-5, 20, 7, 4, 0, 0, 0)