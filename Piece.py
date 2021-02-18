#Author: Sahil Agrawal
from graphics import *

class Piece:
    def __init__(self,location,win,color,pieceType):
        #pieceType --> rook,bishop, pawn, etc.
        #Another way to implement this?
        self.eaten = False
        self.location = location
        self.color = color
        self.pieceType = pieceType
        self.imageUpdate(location)

    def getPossibleMoves(self,myKing,myTeam,enemyTeam,listDir,numSpaces):
        #create a list of all possible coordinates the piece can move
        self.possibleSpots(listDir,numSpaces,enemyTeam,myTeam)
        #self.spots = self.calcPossibleSquares(myTeam,enemyTeam)
        #remove spots that are off the board
        self.spots = self.removeOffBoardSpots()
        #removes spot that will put their own king in check
        self.spots = self.avoidOwnCheck(myKing,myTeam,enemyTeam)
        return self.spots

    
    #call this after the user clicks on a square.
        #This will check if it is a valid move, and if it is it
        #will return True and will move the pieces accordingly.
    def movePiece(self,pt,enemyPieces):
        valid = self.checkValidMove(pt)
        if valid:
            self.location = Point(x,y)
            self.imageUpdate(self.location)
            self.eatPiece(enemyPieces)
            return True,enemyPieces,self.image
        else:
            return False,enemyPieces,self.image


    #This will find the possible spots for all pieces. (except for diagonal pawn capture)
    #Ex: king's parameters would be: [[1,1],[1,0]....], 1, enemyTeam
        #knight: [[1,2],[2,1],etc.],1,enemyTeam
#knight: 2,1],[1,2]
    #First filter
    def possibleSpots(self,listDir,numSpaces,enemyTeam,sameTeam):
        self.spots = []
        validPawnMove = True #Use this to check if the pawn can go 2 spaces ahead
        #For every direction, go i in numSpaces until you hit an enemy Piece or same team.
        for direction in listDir:
            x,y = self.location.getX(),self.location.getY()
            if pieceType == "pawn":
                if validPawnMove==False: break
            for i in numSpaces:
                x += direction[0]
                y += direction[1]
                if onAPiece: break
                #if on enemyTeam, this is the last possible square to go in this direction
                #If it is pawn, then we check which direction it is going in
                for piece in enemyTeam:
                    if piece.getLocation() == Point(x,y):
                        if pieceType != "pawn":
                            self.spots.append(Point(x,y))
                        elif pieceType == "pawn":
                            if direction == [1,1] or direction == [-1,1]:
                                self.spots.append(Point(x,y))
                            elif direction == [0,1]:
                                validPawnMove = False
                        onAPiece = True
                for piece in sameTeam:
                    if piece.getLocation() == Point(x,y):
                        onAPiece = True
                        
                        
                        
    def eatPiece(self,enemyPieces):
        for piece in enemyPieces:
            if piece.getLocation() == self.getLocation():
                piece.isEaten()

    #use this for updating message box 
    def getPieceType(self):
        return self.pieceType 
#These functions are not called in main
    #checks if user input is valid (don't call this)
    def checkValidMove(self,userInput):
        if userInput in self.spots:
            return True
        else:
            return False

    def isEaten(self):
        self.eaten = True

    def removeOffBoardSpots(self):
        for pt in self.possibleSpots:
            if pt[0] >7 or pt[0] <1 or pt[1] >7 or pt[1] <1:
                pt.remove

    def imageUpdate(self,location):
        if self.eaten:
            location = Point(200,200)
        self.image = Image(location,self.color+self.pieceType+".png")
        return self.image

#Checking logic        
    #to do: confirm that this is required by assignment
    #for pieces - allows them to only make moves that prevent the king from going into check
    #for king - prevents him from going to squares that put himself in check.
    def avoidOwnCheck(self, myKing,myTeam,enemyTeam):
        kingX, kingY = myKing.getPosition()
        myTeam.append(self) #How to make a list append the object that it is in?
        self.currentLocation = self.location
        for spot in self.spots:
            self.location = spot
            for piece in enemyTeam:
                possibleSpots = piece.getPossibleMoves(enemyTeam,myTeam)
                if (self.currentLocation == self.location) and (myKing.getPosition() in possibleSpots):
                    #This checks if the the king is in check without moving any of the pieces.
                    spot.remove(self.spots) #find correct notation
        self.location = self.currentLocation            
                    
            #check that if the piece's location is at one of these spots, does myKing become in check?

    

'"""""" accessors """""'
def getEatean(self):
    return self.eaten

def checkColor(self):
    return self.color

def getLocation(self):
    return self.location


