#Author: Sahil Agrawal

class Piece:
    def __init__(self,location):
        self.eaten = False
        self.location = location

    def getPossibleMoves(self,myTeam,enemyTeam):
        self.spots = self.calcPossibleSquares(myTeam,enemyTeam)
        self.spots = self.avoidOwnCheck(myTeam, enemyTeam)
        return self.spots
        
    def movePiece(self,pt):
        valid = self.checkValidMove(
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

    #remove a spot from self.spots if moving there puts our own king in check.
    #to do: confirm that this is required by assignment
    def avoidOwnCheck(self, myKing, enemyTeam):
        kingX, kingY = myKing.getPosition()
        for spot in self.spots:
            #check that if the piece's location is at one of these spots, does myKing become in check?
            if myKingCheck:
                self.spots.remove(spot)
