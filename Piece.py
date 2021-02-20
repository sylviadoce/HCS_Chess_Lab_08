#Author: Sahil Agrawal
from graphics import *

class Piece:
    #works
    def __init__(self,location,color,pieceType):
        #pieceType --> rook,bishop, pawn, etc.
        #Another way to implement this?
        self.eaten = False
        self.location = location
        self.color = color
        self.pieceType = pieceType
        self.imageUpdate()
        self.firstPawnMove = True #this will be used in getPossibleMoves

    def getPossibleMoves(self,myKing,enemyKing,myTeam,enemyTeam,listDir,numSpaces):
        #create a list of all possible coordinates the piece can move
        self.possibleSpots(listDir,numSpaces,enemyTeam,myTeam)
        #self.spots = self.calcPossibleSquares(myTeam,enemyTeam)
        #remove spots that are off the board
        self.removeOffBoardSpots()
        #removes spot that will put their own king in check
        self.avoidOwnCheck(myKing,enemyKing,myTeam,enemyTeam)
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
            if self.pieceType == "pawn":
                self.firstPawnMove = False
        else:
            return False,enemyPieces,self.image


    #This will find the possible spots for all pieces. (except for diagonal pawn capture)
    #Ex: king's parameters would be: [[1,1],[1,0]....], 1, enemyTeam
        #knight: [[1,2],[2,1],etc.],1,enemyTeam
#knight: 2,1],[1,2]
    #First filter
    def possibleSpots(self,listDir,numSpaces,enemyTeam,sameTeam):
        self.spots = []
        validPawnMove = True #Use this to check if the pawn can go 2 spaces ahead - is there a piece in front of it?
        if self.firstPawnMove == False:
            listDir.remove([0,2])
        onAPiece = False
        #For every direction, go i in numSpaces until you hit an enemy Piece or same team.
        for direction in listDir:
            x,y = self.location.getX(),self.location.getY()
            if self.pieceType == "pawn":
                if validPawnMove==False: break
            for i in range(1,numSpaces+1):
                print(direction[0])
                x = direction[0] + x
                y = direction[1] + y
                if onAPiece: break
                #if on enemyTeam, this is the last possible square to go in this direction
                #If it is pawn, then we check which direction it is going in
                for piece in enemyTeam:
                    if piece.getLocation() == Point(x,y):
                        if self.pieceType == "pawn":
                            if direction == [1,1] or direction == [-1,1]:
                                self.spots.append(Point(x,y))
                            elif direction == [0,1]:
                                validPawnMove = False
                        else:
                            self.spots.append(Point(x,y))
                        onAPiece = True
                for piece in sameTeam:
                    if piece.getLocation() == Point(x,y):
                        onAPiece = True
                        
                if not onAPiece:
                    self.spots.append(Point(x,y))
                        
    def eatPiece(self,enemyPieces):
        for piece in enemyPieces:
            if piece.getLocation() == self.location:
                piece.isEaten()

    #use this for updating message box 
    def getPieceType(self):
        return self.pieceType 
##These functions are not called in main##
    #checks if user input is valid (don't call this)
    def checkValidMove(self,userInput):
        if userInput in self.spots:
            return True
        else:
            return False

    def isEaten(self):
        self.eaten = True

    def removeOffBoardSpots(self):
        for pt in self.spots:
            if pt.getX()<0 or pt.getY()<0 or pt.getX()>7 or pt.getY()>7:
                self.spots.remove(pt)
    #works
    def imageUpdate(self):
        if self.eaten:
            self.location = Point(200,200)
        self.image = Image(self.location,self.color+self.pieceType+".png")
        return self.image

##Checking logic##        
    #for pieces - allows them to only make moves that prevent the king from going into check
    #for king - prevents him from going to squares that put himself in check.
    def avoidOwnCheck(self, myKing,enemyKing,myTeam,enemyTeam):
        kingX, kingY = myKing.getLocation().getX(),myKing.getLocation().getY()
        myTeam.append(self) #How to make a list append the object that it is in?
        self.currentLocation = self.location
        for spot in self.spots:
            self.location = spot
            for piece in enemyTeam:
                listDir,numSpaces = piece.calcListDirections()
                possibleSpots = piece.getPossibleMoves(enemyKing,myTeam,enemyTeam,listDir,numSpaces)
                if (self.currentLocation == self.location) and (myKing.getPosition() in possibleSpots):
                    #This checks if the the king is in check without moving any of the pieces.
                    spot.remove(self.spots) #find correct notation
        self.location = self.currentLocation            
                    
            #check that if the piece's location is at one of these spots, does myKing become in check?

    
    def getKingCheck(self,enemyKing,enemyPieces,sameTeam):
        numChecksReturned = 0
        if self.pieceType == "king":
            for piece in enemyPieces:
                spots = []
                spots = piece.getPossibleMoves(myKing,myTeam,enemyTeam,piece.calcListDirections(),piece.getNumSpaces())
                for pt in spots:
                    if pt == self.location:
                        numChecksReturned +=1
                        
            if numChecksReturned>0:
                return True
            else: return False
                    

    def getEatean(self):
        return self.eaten

    def checkColor(self):
        return self.color

    def getLocation(self):
        return (self.location)


