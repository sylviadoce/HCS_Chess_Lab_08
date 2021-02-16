# Sylvia Chin
#
# Chess Games module that runs the game - class??
#
from Piece import *
from BoardGUI import *

def __init__(self):
    self.board_gui = BoardGUI()

def createPieces(self) -> list:
    # Create all pieces from their subclass
    pawns = self.board_gui.createPawns()
    bishops = self.board_gui.createBishops()
    knights = self.board_gui.createKnights()
    rooks = self.board_gui.createRooks()
    queens = self.board_gui.createQueens()
    kings = self.board_gui.createKings()

    # Create a list of two lists storing all pieces
    # First item contains white pieces, second contains black pieces
    pieces = [[],[]]
    for color in range(2):
        for piece in [pawns,bishops,knights,rooks,queens,kings]:
            pieces[color] += piece[color]

    return pieces
