#HCS Lab08
#Author: Sahil Agrawal
from graphics import *

class Piece:
    #works
    def __init__(self,location,color,pieceType,ID):
        #pieceType --> rook,bishop, pawn, etc.
        self.eaten = False
        self.location = location
        self.color = color
        self.pieceType = pieceType
        self.imageUpdate()
        self.ID = ID
        self.firstPawnMove = True 
        self.check = False
        self.checkmate = False
        self.actualLocation = self.location
        #oppCheck,oppCheckMate --> check/checkmate for the opposite team
        self.oppCheck = False
        self.oppCheckMate = False
        

    def getPossibleMoves(self,myKing,enemyKing,myTeam,enemyTeam,avoidCheck):
        '''This is the overall method to get the possible moves of a piece'''
        #create a list of all possible coordinates the piece can move
        listDir,numSpaces = self.calcListDirections()
        self.possibleSpots(listDir,numSpaces,enemyTeam,myTeam)
        #"nocheck" is used in avoidOwnCheck when trying to figure out what moves would put the king in check
        if avoidCheck != "nocheck":
            self.avoidOwnCheck(myKing,enemyKing,myTeam,enemyTeam)
        self.myKing = myKing
        self.enemyKing = enemyKing
        self.myTeam = myTeam
        self.enemyTeam = enemyTeam
        return self.spots

    
    #call this after the user clicks on a square.
    def movePiece(self,xy,enemyPieces):
        '''After you know a move is valid, this method will actually move the piece and set check and checkmate status'''
        self.location = Point(xy[0],xy[1])
        self.actualLocation = self.location
        self.eatPiece(enemyPieces)
        #firsPawnMove keeps track of whether or not it is the first pawn move.
        #If it is, then [0,2] is a valid direction. Otherwise, it isn't.
        if self.pieceType == "pawn":
            self.firstPawnMove = False
        #checking for check and checkmate
        enemyPieces[0].getPossibleMoves(self.enemyKing,self.myKing,self.enemyTeam,self.myTeam,"y")
        if enemyPieces[0].getCheck():
            self.setOppCheck("t")
            enemyPieces[0].calcCheckMate(self.enemyKing,self.myKing,self.enemyTeam,self.myTeam)
            if enemyPieces[0].getCheckMate():
                self.setOppCheckMate("t")
        else:
            self.setOppCheck("f")
        return enemyPieces
        

    #This will find the possible spots for all pieces before making sure the piece can't put their own king in check
    #Ex: king's parameters would be: [[1,1],[1,0]....], 1, enemyTeam
        #knight: [[1,2],[2,1],etc.],1,enemyTeam
    def possibleSpots(self,listDir,numSpaces,enemyTeam,sameTeam):
        '''This will find all possible spots before any checking logic'''
        self.spots = []
        validPawnMove = True #Use this to check if the pawn can go 2 spaces ahead - is there a piece in front of it?
        if self.firstPawnMove == False:
            listDir.remove(listDir[3])
        #For every direction, go i in numSpaces until you hit an enemy Piece or same team.
        for direction in listDir:
            x,y = self.location.getX(),self.location.getY()
            onAPiece = False
            if self.pieceType == "pawn":
                if validPawnMove==False: break
            for i in range(1,(int(numSpaces)+1)):
                x += direction[0]
                y = direction[1] + y
                if onAPiece or x<0 or y<0 or x>8 or y>8:
                    break
                #if on enemyTeam, this is the last possible square to go in this direction
                #If it is pawn, then we check which direction it is going in
                for piece in enemyTeam:
                    if x == piece.getLocation().getX() and y == piece.getLocation().getY():
                        if self.pieceType == "pawn":
                            absDir = [abs(direction[0]),abs(direction[1])]
                            if absDir == [1,1]:
                                self.spots.append(Point(x,y))
                            elif absDir == [0,1]:
                                validPawnMove = False
                                #This is used to prevent checking direction [0,2]
                        else:
                            self.spots.append(Point(x,y))

                        onAPiece = True
                for piece in sameTeam:
                    if x == piece.getLocation().getX() and y == piece.getLocation().getY():
                        onAPiece = True

                        
                if onAPiece == False:
                    if self.pieceType == "pawn":
                        if direction[0] == 0:
                            self.spots.append(Point(x,y))
                    else: self.spots.append(Point(x,y))    

                        
    def eatPiece(self,enemyPieces):
        '''This will set pieces to eaten'''
        for piece in enemyPieces:
            x,y = self.getLocationXY()
            enemyx,enemyy = piece.getLocationXY()
            if x == enemyx and y == enemyy:
                piece.isEaten()


    #use this for updating message box 
    def getPieceType(self):
        return self.pieceType

    
    def checkValidMove(self,userInput):
        if userInput in self.spots:
            return True
        else:
            return False

    def isEaten(self):
        '''sets the piece to eaten'''
        self.location = Point(200,200)
        self.eaten = True
                
    def imageUpdate(self):
        '''updates the piece image object. Image is actually drawn in BoardGUI'''
        if self.eaten:
            self.location = Point(200,200)
        self.image = Image(self.location,self.color+self.pieceType+".png")
        return self.image


    #for pieces - allows them to only make moves that prevent the king from going into check
    #for king - prevents him from going to squares that put himself in check.
    def avoidOwnCheck(self, myKing,enemyKing,myTeam,enemyTeam):
        '''Prevents pieces from moving in ways that will put their king in check. It will also check for check.'''
        for p in myTeam:
            p.setCheck("f")
        kingX, kingY = myKing.getLocationXY()
        removeSpots = []
        currentLocation = self.location
        #this is used for checking for check
        self.spots.append(currentLocation)
        for spot in self.spots:
            self.location = spot
            for piece in enemyTeam:
                listDir,numSpaces = piece.calcListDirections()
                enemyX,enemyY = piece.getLocationXY()
                if enemyX == spot.getX() and enemyY == spot.getY():
                    piece.setLocation(Point(200,200))
                x1,y1 = piece.getLocationXY()
                possibleEnemyMoves = piece.getPossibleMoves(enemyKing,myKing,enemyTeam,myTeam,"nocheck")
                for pos in possibleEnemyMoves:
                    #if a piece can attack the king when the sameTeam piece is moved, then not allowed
                    if (kingX == pos.getX() and kingY == pos.getY()) and (self.pieceType!="king"):                      
                        #if the location is the currentLocation, then the king is under check since the king is being
                        #attacked even though no one on sameTeam has moved
                        if currentLocation == spot:
                            for p in myTeam:
                                p.setCheck("t")                  
                        else: removeSpots.append(spot) 
                    elif self.pieceType == "king":
                        #if a king move will put himself in check, then not allowed
                        x,y = spot.getX(),spot.getY()
                        if x == pos.getX() and y == pos.getY():
                            if spot not in removeSpots:
                                if currentLocation != spot:
                                    removeSpots.append(spot)
                                if currentLocation == spot:
                                    for p in myTeam:
                                        p.setCheck("t")
                                        
                piece.resetLocation()        
                            
        removeSpots.append(currentLocation)

        for spot in removeSpots:
            if spot in self.spots:
                self.spots.remove(spot)
        self.location = currentLocation            

    

    def calcCheckMate(self,myKing,enemyKing,myTeam,enemyTeam):
        '''This will find whether or not it is checkmate'''
        if self.spots == []:
            for p in myTeam:
                spots = p.getPossibleMoves(myKing,enemyKing,myTeam,enemyTeam,"c")
                if spots == []:
                    noMoves = True
                else:
                    noMoves = False
                    break
            if noMoves == True:
                for piece in myTeam:
                    piece.setCheckMate()
            

    def setOppCheck(self,oppCheck):
        if oppCheck == "t":
            self.oppCheck = True
        else:
            self.oppCheck = False
        
    def setOppCheckMate(self,oppCheckMate):
        if oppCheckMate == "t":
            self.oppCheckMate = True
        else:
            self.oppCheckMate = False
        
    def getEaten(self):
        return (self.eaten)

    def checkColor(self):
        return self.color

    def getLocation(self):
        return (self.location)

    def setLocation(self,point):
        self.location = point

    def resetLocation(self):
        self.location = self.actualLocation

    def getLocationXY(self):
        return self.location.getX(),self.location.getY()

    def setCheck(self,check):
        if check == "t":
            self.check = True
        else:
            self.check = False

    def getCheck(self):
        return self.check

    def getOppCheck(self):
        return self.oppCheck

    def getOppCheckMate(self):
        return self.oppCheckMate
    
    def checkPieceID(self):
        return self.ID

    def setCheckMate(self):
        self.checkmate = True

    def getCheckMate(self):
        return (self.checkmate)
