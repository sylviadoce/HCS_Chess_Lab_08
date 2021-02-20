from Piece import *

# Subclasses Pawn, Rook, Knight

class Pawn(Piece):
    """Subclass of the Piece Class for pawns."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible pawn moves: lists of what to add
            to the pawn's x,y location."""
        numSpaces = 1
        # Includes the special eating diagonals and two-y beginning move
        listDir = [[1,1],[-1,1],[0,1],[0,2]]

        return listDir, numSpaces

class Rook(Piece):
    """Subclass of the Piece Class for rooks."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the rook's x,y location."""
        numSpaces = 7
        listDir = [[0,1],[1,0],[0,-1],[-1,0]]
##        listDir = []
##        for i in range(8):
##            if i != 0:
##                listDir.append([0,i])
##                listDir.append([i,0])

        return listDir, numSpaces
    

class Knight(Piece):
    """Subclass of the Piece Class for knights."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the rook's x,y location."""
        numSpaces = 1
        listDir = [[1,2],[-1,2],[1,-2],[-1,-2],
                   [2,1],[-2,1],[2,-1],[-2,-1]]

        return listDir, numSpaces

class Queen(Piece):
    """Subclass of the Piece Class for rooks."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the queen's x,y location."""
        numSpaces = 7
        listDir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
##        listDir = []
##        for i in range(8):
##            if i != 7:
##                listDir.append([i,i+1])
##                listDir.append([i+1,i])
##                listDir.append([i,-(i+1)])
##                listDir.append([-(i+1),i])
##            if i != 6 and i != 7:
##                listDir.append([i,i+2])
##                listDir.append([i+2,i])
##                listDir.append([i,-(i+2)])
##                listDir.append([-(i+2),i])
##            if i != 5 and i != 6 and i != 7:
##                listDir.append([i,i+3])
##                listDir.append([i+3,i])
##                listDir.append([i,-(i+3)])
##                listDir.append([-(i+3),i])
##            if i != 4 and i != 5 and i != 6 and i != 7:
##                listDir.append([i,i+4])
##                listDir.append([i+4,i])
##                listDir.append([i,-(i+4)])
##                listDir.append([-(i+4),i])
##            if i != 3 and i != 4 and i != 5 and i != 6 and i != 7:
##                listDir.append([i,i+5])
##                listDir.append([i+5,i])
##                listDir.append([i,-(i+5)])
##                listDir.append([-(i+5),i])
##            if (i != 2 and i != 3 and i != 4 and i != 5 and i != 6
##                and i != 7):
##                listDir.append([i,i+6])
##                listDir.append([i+6,i])
##                listDir.append([i,-(i+6)])
##                listDir.append([-(i+6),i])
##            if (i != 1 and i != 2 and i != 3 and i != 4 and i != 5
##                and i != 6 and i != 7):
##                listDir.append([i,i+7])
##                listDir.append([i+7,i])
##                listDir.append([i,-(i+7)])
##                listDir.append([-(i+7),i])
##            if i != 0:
##                listDir.append([i,i])
##                listDir.append([-i,-i])

        return listDir, numSpaces


##class Piece:
##    def __init__(self,color,position: list):
##        # Gives the piece's team (white or black)
##        self.color = color
##        # Gives the piece's board position
##        self.position = position
##        # Sets the piece's status to not dead
##        self.eaten = eaten
##
##    def eatPiece(self,target):
##        # piece's position is target's old position
##
##    def movePiece(self) -> list:
##        return self.position
##
##    def getPosition(self) -> list:
##        return self.position
##
##    def getNextPosition(self,move) -> list:
##        return self.position
##
##    def checkValidMove(self) -> bool:
##        return #some way to check if space is occupied
##
##    def isEaten(self) -> bool:
##        # Returns true is self.eaten is True
##        return self.eaten
