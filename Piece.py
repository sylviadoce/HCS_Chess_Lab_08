#Author: Sahil Agrawal

class Piece:
    def __init__(self,location,win,color,pieceType):
        #pieceType --> rook,bishop, pawn, etc.
        #Another way to implement this?
        self.eaten = False
        self.location = location
        self.color = color
        self.pieceType = pieceType
        self.imageUpdate(location)
        

    #make a list
    
        

    def getPossibleMoves(self,myKing,myTeam,enemyTeam):
        #create a list of all possible coordinates the piece can move
        self.spots = self.calcPossibleSquares(myTeam,enemyTeam)
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
            self.imageUpdate(location)
            self.eatPiece(enemyPieces)
            return True,enemyPieces,self.image
        else:
            return False,enemyPieces,self.image


'''main'''
valid,enemyPieces,image = piece.movePiece
image.draw(win)
'''----'''





    #This will find the possible spots for all pieces. (except for diagonal pawn capture)
    #Ex: king's parameters would be: [[1,1],[1,0]....], 1, enemyTeam
        #knight: [[1,2],[2,1],etc.],1,enemyTeam
    #First filter
    def possibleSpots(self,listDir,numSpaces,enemyTeam):
        self.spots = []
        for direction in listDir:
            x,y = self.location.getX(),self.location.getY()
            for i in numSpaces
                x += direction[0]
                y += direction[1]
                if onAPiece: break
                for piece in enemyTeam:
                    if piece.getLocation() == Point(x,y):
                        if pieceType != "pawn":
                            self.spots.append(Point(x,y))
                        onAPiece = True
                        break
                for piece in sameTeam:
                    if piece.getLocation() == Point(x,y):
                        onAPiece = True
                        break
                        
                
        

        
    def eatPiece(self,enemyPieces):
        for piece in enemyPieces:
            if piece.getLocation() == self.getLocation():
                piece.isEaten()

    #use this for updating message box 
    def getPieceType(self):
        return self.pieceType 
#These functions are not called in main
'""""""'
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
        self.image = Image(location,color+pieceType+".png")
        return self.image
'"""""""'

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
                if (self.currentLocation = self.location) and (myKing.getPosition() in possibleSpots):
                    #This checks if the the king is in check without moving any of the pieces.
                    spot.remove(self.spots) #find correct notation
        self.location = self.currentLocation            
                    
            #check that if the piece's location is at one of these spots, does myKing become in check?

    

