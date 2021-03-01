#Author: Sahil Agrawal
from graphics import *

class Piece:
    #works
    def __init__(self,location,color,pieceType,ID):
        #pieceType --> rook,bishop, pawn, etc.
        #Another way to implement this?
        self.eaten = False
        self.location = location
        self.color = color
        self.pieceType = pieceType
        self.imageUpdate()
        self.ID = ID
        self.firstPawnMove = True #this will be used in getPossibleMoves
        self.check = False
        self.checkmate = False
        self.actualLocation = self.location
        self.oppCheck = False
        self.oppCheckMate = False
        

    def getPossibleMoves(self,myKing,enemyKing,myTeam,enemyTeam,avoidCheck):
        #create a list of all possible coordinates the piece can move
        listDir,numSpaces = self.calcListDirections()
        self.possibleSpots(listDir,numSpaces,enemyTeam,myTeam)
        #remove spots that are off the board
        #removes spot that will put their own king in check
        #print(self.pieceType)
        if avoidCheck != "nocheck":
            self.avoidOwnCheck(myKing,enemyKing,myTeam,enemyTeam)
##            print("spots after avoidCheck",self.spots,self.pieceType)
            #print(self.pieceType,self.color,"Piece being moved")
        #if avoidCheck == "y":self.calcCheckMate(myKing,enemyKing,myTeam,enemyTeam)
        self.myKing = myKing
        self.enemyKing = enemyKing
        self.myTeam = myTeam
        self.enemyTeam = enemyTeam
        #print(self.spots,"First")
        #self.delCornerSpots()
        #self.removeOffBoardSpots()
        #print(self.spots,"second\n")
        return self.spots

    
    #call this after the user clicks on a square.
        #This will check if it is a valid move, and if it is it
        #will return True and will move the pieces accordingly.
    def movePiece(self,xy,enemyPieces):
        self.location = Point(xy[0],xy[1])
##        print(self.pieceType,"moved to",self.location)
        self.actualLocation = self.location
        #print(self.location)
        #self.imageUpdate()
        self.eatPiece(enemyPieces)
        if self.pieceType == "pawn":
            self.firstPawnMove = False
        enemyPieces[0].getPossibleMoves(self.enemyKing,self.myKing,self.enemyTeam,self.myTeam,"y")
##        print(enemyPieces[0].getCheck(),"check")
        if enemyPieces[0].getCheck():
            self.setOppCheck("t")
            enemyPieces[0].calcCheckMate(self.enemyKing,self.myKing,self.enemyTeam,self.myTeam)
            if enemyPieces[0].getCheckMate():
                self.setOppCheckMate("t")
        else:
            self.setOppCheck("f")
##        print(self.getOppCheck(),"oppCheck")
##        print(self.getOppCheckMate(),"oppCheckmate")
        return enemyPieces
        

    #This will find the possible spots for all pieces. (except for diagonal pawn capture)
    #Ex: king's parameters would be: [[1,1],[1,0]....], 1, enemyTeam
        #knight: [[1,2],[2,1],etc.],1,enemyTeam
#knight: 2,1],[1,2]
    #First filter
    def possibleSpots(self,listDir,numSpaces,enemyTeam,sameTeam):
##        if self.color == "white" and self.pieceType == "queen":
##            print(self.pieceType)
        self.spots = []
        validPawnMove = True #Use this to check if the pawn can go 2 spaces ahead - is there a piece in front of it?
        if self.firstPawnMove == False:
            listDir.remove(listDir[3])
        #For every direction, go i in numSpaces until you hit an enemy Piece or same team.
        for direction in listDir:
            #print(direction,self.pieceType)
            x,y = self.location.getX(),self.location.getY()
            onAPiece = False
            if self.pieceType == "pawn":
                if validPawnMove==False: break
            for i in range(1,(int(numSpaces)+1)):
                x += direction[0]
                y = direction[1] + y
                #print(68)
                if onAPiece or x<0 or y<0 or x>8 or y>8:
                    #print("x",x,"y",y,self.pieceType,self.color)
                    #print("onAPiece",onAPiece)
                    break
                #elif x <0 or y<0 or x>0 or y>0: break
                #if on enemyTeam, this is the last possible square to go in this direction
                #If it is pawn, then we check which direction it is going in
##                if self.color == "white" and self.pieceType == "queen":
##                    print(x,y)
                for piece in enemyTeam:
                    if x == piece.getLocation().getX() and y == piece.getLocation().getY():
##                        print(75)
                        if self.pieceType == "pawn":
                            absDir = [abs(direction[0]),abs(direction[1])]
                            if absDir == [1,1]:
##                                print("here1")
                                self.spots.append(Point(x,y))
                            elif absDir == [0,1]:
                                validPawnMove = False
                                #This is used to prevent checking direction [0,2]
                        else:
##                            print("here2")
                            self.spots.append(Point(x,y))

                        onAPiece = True
                for piece in sameTeam:
                    if x == piece.getLocation().getX() and y == piece.getLocation().getY():
                        onAPiece = True

                        
                if onAPiece == False:
                    #print(90)
                    if self.pieceType == "pawn":
                        if direction[0] == 0:
                            #print("here3",self.pieceType)
                            self.spots.append(Point(x,y))
                    else: self.spots.append(Point(x,y))    
                        
    def eatPiece(self,enemyPieces):
        for piece in enemyPieces:
            x,y = self.getLocationXY()
            #print(self.getLocationXY())
            enemyx,enemyy = piece.getLocationXY()
            #print("enemy",piece.getLocationXY())
            if x == enemyx and y == enemyy:
##                print(piece.getPieceType(),piece.checkColor(),"has been eaten")
##                print(piece.checkColor(),piece.getLocation(),"enemy")
##                print(self.color,self.location)
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
        self.location = Point(200,200)
        self.eaten = True




    #def removeOffBoardSpots(self):
    #    lstIndex = []
    #    if len(self.spots) != 0:
    #       for i in range(len(self.spots)-1):
     #           pt = self.spots[i]
    #            if (pt.getX()>0) or (pt.getY()>0) or (pt.getX()<7) or (pt.getY()<7):
    #                lstIndex.append(i)
    #        spots = self.spots
   #         self.spots = []
    #        for index in lstIndex:
    #            self.spots.append(spots[index])
                
  
    #works
    def imageUpdate(self):
        if self.eaten:
            self.location = Point(200,200)
        #(self.image).move(self.location.getX(),self.location.getY())
        self.image = Image(self.location,self.color+self.pieceType+".png")
        return self.image

##Checking logic##        
    #for pieces - allows them to only make moves that prevent the king from going into check
    #for king - prevents him from going to squares that put himself in check.
    def avoidOwnCheck(self, myKing,enemyKing,myTeam,enemyTeam):
        for p in myTeam:
            p.setCheck("f")
        kingX, kingY = myKing.getLocationXY()
        removeSpots = []
        #myTeam.append(self) #How to make a list append the object that it is in?
        currentLocation = self.location
        #this is used for checking for check
        self.spots.append(currentLocation)
        for spot in self.spots:
##            print("avoidCheck",self.spots)
            self.location = spot
            for piece in enemyTeam:
                listDir,numSpaces = piece.calcListDirections()
                #print(piece.checkColor())
                enemyX,enemyY = piece.getLocationXY()
                #if the piece can capture an enemy piece such that it will no longer be in check, then pretend to eliminate the piece
                #if the king still is under check, then the move is invalid. otherwise, it is valid. 
                if enemyX == spot.getX() and enemyY == spot.getY():
##                    print(190)
                    piece.setLocation(Point(200,200))
                x1,y1 = piece.getLocationXY()
##                if x1 == 200:
##                    print(piece.getPieceType(),piece.checkColor(),"simulating eaten")
                possibleEnemyMoves = piece.getPossibleMoves(enemyKing,myKing,enemyTeam,myTeam,"nocheck")
                for pos in possibleEnemyMoves:
                    #print(kingX,",",kingY,"king")
                    #print(pos.getX(),",",pos.getY(),"pos")
                    #print("spot",spot)
                    #if a piece can attack the king when the sameTeam piece is moved, then not allowed
                    if (kingX == pos.getX() and kingY == pos.getY()) and (self.pieceType!="king"):
##                        print("Piece",164)
                        #if the location is the currentLocation, then the king is under check since the king is being
                        #attacked even though no one on sameTeam has moved
                        if currentLocation == spot:
                            for p in myTeam:
                                p.setCheck("t")
##                                print("king is under check")                             
                        else: removeSpots.append(spot) #find correct notation
                    elif self.pieceType == "king":
                        x,y = spot.getX(),spot.getY()
                        if x == pos.getX() and y == pos.getY():
##                            print("x",x,"y",y)
##                            print(pos.getX(),pos.getY())
                            if spot not in removeSpots:
                                if currentLocation != spot:
                                    removeSpots.append(spot)
                                if currentLocation == spot:
                                    for p in myTeam:
                                        p.setCheck("t")
##                                        print("king is under check")
                                        
                piece.resetLocation()        
                            
        removeSpots.append(currentLocation)
##        print(self.pieceType,removeSpots,self.spots)
        for spot in removeSpots:
            if spot in self.spots:
                self.spots.remove(spot)
        self.location = currentLocation            
                    
            #check that if the piece's location is at one of these spots, ds myKing become in check?

    
    #def getKingCheck(self,enemyKing,enemyPieces,sameTeam):
    #    numChecksReturned = 0
    #    if self.pieceType == "king"
    #        for piece in enemyPieces:
    #            spots = []
    #            spots = piece.getPossibleMoves(enemyKing,myKing,enemyTeam,myTeam,piece.calcListDirections(),piece.getNumSpaces())
    #            for pt in spots:
    #                if pt == self.location:
    #                    numChecksReturned +=1
    #                    
    #        if numChecksReturned>0:
    #            return True
    #        else: return False
                    


    def calcCheckMate(self,myKing,enemyKing,myTeam,enemyTeam):
        if self.spots == []:
##            print(261)
            for p in myTeam:
                spots = p.getPossibleMoves(myKing,enemyKing,myTeam,enemyTeam,"c")
                if spots == []:
                    noMoves = True
                else:
                    noMoves = False
                    break
            if noMoves == True:
                for piece in myTeam:
                    #print("inCheckmate")
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
