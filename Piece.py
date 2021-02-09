#Author: Sahil Agrawal

class Piece:
    def __init__(self,location):
        self.eaten = False
        self.location = location

    def getPossibleMoves(self,myKing,myTeam,enemyTeam):
        self.spots = self.calcPossibleSquares(myTeam,enemyTeam)
        self.spots = self.removeOffBoardSpots()
        self.spots = self.avoidOwnCheck(myKing,myTeam, enemyTeam)
        return self.spots
        
    def movePiece(self,pt):
        valid = self.checkValidMove(pt)
        if valid:
            self.location = Point(x,y)
            return True
        else:
            return False
        
    def eatPiece(self,enemyPieces):
        for piece in enemyPieces:
            if piece.getLocation() == self.getLocation():
                piece.isEaten()

    def checkValidMove(self,userInput):
        if userInput in self.spots:
            return True
        else:
            return False

    def isEaten(self):
        self.eaten = True
        
    #to do: confirm that this is required by assignment
    #for pieces - allows them to only make moves that prevent the king from going into check
    #for king - prevents him from going to squares that put himself in check.
    def avoidOwnCheck(self, myKing,myTeam,enemyTeam):
        kingX, kingY = myKing.getPosition()
        myTeam.append(self) #How to make a list append the object that it is in?
        for spot in self.spots:
            self.currentLocation = self.location
            self.location = spot
            for piece in enemyTeam:
                possibleSpots = piece.getPossibleMoves(enemyTeam,myTeam)
                if myKing.getPosition() in possibleSpots:
                    spot.remove(self.spots) #find correct notation
                    
            #check that if the piece's location is at one of these spots, does myKing become in check?

    def removeOffBoardSpots(self):
            for pt in self.possibleSpots:
                if pt[0] >7 or pt[0] <1 or pt[1] >7 or pt[1] <1:
                    pt.remove
    
