# Subclasses Pawn, Rook, Knight

# I don't think we can write what each piece needs to do before
# establishing the coordinates system in the GUI. Also, we need
# to come up with a way of knowing when pieces are clicked on to
# move — whether that be making each graphic a button or
# something. She also wants one author per module, so we should
# split off. I'm fine doing either I guess.

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
    # Same init as superclass
    # Define the pawn's moves
    def movePiece(self) -> list:
        # Pawns can normally only move one square forward
        return self.position[1] += 1

class Rook(Piece):
    """Subclass of the Piece Class for rooks."""
    # Same init as superclass

class Knight(Piece):
    """Subclass of piece class for knights."""
    # Same init as superclass
