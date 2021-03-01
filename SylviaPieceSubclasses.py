# Sylvia Chin
# HCS Lab 08 - Chess
#
# This contains the subclasses of Piece for pieces Pawn, Rook,
#   Knight and Queen.
#
from Piece import *

class Pawn(Piece):
    """Subclass of the Piece Class for pawns."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible pawn moves: lists of what to add
            to the pawn's x,y location."""
        # Pawns move vertically forward; one space
        numSpaces = 1
        # Includes the special eating diagonals and two-y beginning move
        if self.color == "white":
            listDir = [[1,1],[-1,1],[0,1],[0,2]]

        else:
            listDir = [[-1,-1],[1,-1],[0,-1],[0,-2]]

        return listDir, numSpaces

class Rook(Piece):
    """Subclass of the Piece Class for rooks."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the rook's x,y location."""
        # Rooks move horizontally and vertically; board limit
        numSpaces = 7
        listDir = [[0,1],[1,0],[0,-1],[-1,0]]

        return listDir, numSpaces

class Knight(Piece):
    """Subclass of the Piece Class for knights."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the rook's x,y location."""
        # Knights move in an L-shape (over two, over one); board limit
        numSpaces = 1
        listDir = [[1,2],[-1,2],[1,-2],[-1,-2],
                   [2,1],[-2,1],[2,-1],[-2,-1]]

        return listDir, numSpaces

class Queen(Piece):
    """Subclass of the Piece Class for queens."""

    def calcListDirections(self) -> list:
        """Returns a list of all possible rook moves: lists of what to add
            to the queen's x,y location."""
        # Queens move horizontally, vertically and diagonally; board limit
        numSpaces = 7
        listDir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        return listDir, numSpaces
