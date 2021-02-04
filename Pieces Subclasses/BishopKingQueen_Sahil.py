


class King(Class):

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

        #removes spots that are off the board
        self.removeOffBoardSpots()
        
        #Any other filters before returning?


    def removeOffBoardSpots(self):
        


class Bishop(Class):



    def calcPossibleSquares(self):
       
        
    

    
