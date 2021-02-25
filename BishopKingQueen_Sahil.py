#Author: Sahil Agrawal

from Piece import Piece

class King(Piece):

    '''
    def calcPossibleSquares(self):
        #this is the possible coordinates for the piece
        self.possibleSpots = []
        #possible Square objects to go to
        self.possibleSquares = []

        #find all the spots one space away from the king
        for x in [self.x-1,self.x,self.x+1]:
            for y in [self.y-1,self.y,self.y+1]
                self.possibleSpots.append((x,y))

        #remove the king's current position
        for pt in self.possibleSpots:
            if pt[0] == self.x and pt[1] == self.y:
                pt.remove()

        #find where unoccupied squares are, and if someone is occupying it, find out which team they are on
        #highlight the squares that are unoccupied
        for sq in allSquares:
            for piece in teamPieces:
                if sq.getLocation() == piece.getLocation():
                    #pieces are being occupied by a a team member, you can remove this from list

        #Find which squares the enemy pieces are on
        for sq in allSquares:
            for piece in enemyPieces:
                #same as above
    '''

    
    def calcListDirections(self):
        numSpaces = 1
        listDir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        return listDir,1

    def getNumSpaces(self):
        return 1

#for moving it, we need to check if the square the user clicked in was in list self.possibleSquares
#if it isn't, then we need to figure out if the user clicked on 

class Bishop(Piece):



    def calcListDirections(self):
        numSpaces = 10
        listDir = [[1,1],[1,-1],[-1,1],[-1,-1]]

        return listDir,10

    def getNumSpaces(self):
        return 10
        
    

    
