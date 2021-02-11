# Subclasses Pawn, Rook, Knight

class Piece:
    def __init__(self,color,position: list):
        # Gives the piece's team (white or black)
        self.color = color
        # Gives the piece's board position
        self.position = position
        # Sets the piece's status to not dead
        self.eaten = eaten

    def eatPiece(self,target):
        # piece's position is target's old position

    def movePiece(self) -> list:
        return self.position

    def getPosition(self) -> list:
        return self.position

    def getNextPosition(self,move) -> list:
        return self.position

    def checkValidMove(self) -> bool:
        return #some way to check if space is occupied

    def isEaten(self) -> bool:
        # Returns true is self.eaten is True
        return self.eaten

class Pawn(Piece):
    """Subclass of the Piece Class for pawns."""

    def calcPossibleSquares(self):
        # Stores open squares in which to move 
        self.possibleSquares = []

        

    def movePiece(self) -> list:
        # Pawns can normally only move one square forward
        return self.position[1] += 1

class Rook(Piece):
    """Subclass of the Piece Class for rooks."""
    # Same init as superclass

class Knight(Piece):
    """Subclass of piece class for knights."""
    # Same init as superclass
