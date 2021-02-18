# Sylvia Chin
#
# Chess Games module that runs the game - class??
#
from Piece import *
from BoardGUI import *

def __init__(self):
    self.board_gui = BoardGUI()

    # Create a list of two lists storing all pieces
    self.pieces = [[],[]]

def createPawns(self) -> list:
    """Creates all white, black pawns in their standard locations."""
    # Stores a list of two lists, pawns in each color (white first)
    pawns = [[],[]]
    
    # Initialize the white (bottom-left) pawn coordinates (a2), create
    x,y = 0.5,1.5
    for i in range(8):
        pawns[0] += Pawn(Point(x,y),self.win,"white","pawn")
        x += 1

    # Initialize the black (top-left) pawn coordinates (a7), create
    x,y = 0.5,6.5
    for i in range(8):
        pawns[1] += Pawn(Point(x,y),self.win,"black","pawn")

    return pawns
    
def createBishops(self) -> list:
    """Creates all white, black bishops in their standard locations."""
    # Stores a list of two lists, bishops in each color (white first)
    bishops = [[],[]]

    # Initialize the white bishop coordinates (c1 and f1), create
    bishops[0] += Bishop(Point(2.5,0.5),self.win,"white","bishop")
    bishops[0] += Bishop(Point(5.5,0.5),self.win,"white","bishop")

    # Initialize the black bishop coordinates (c8 and f8), create
    bishops[1] += Bishop(Point(2.5,7.5),self.win,"black","bishop")
    bishops[1] += Bishop(Point(5.5,7.5),self.win,"black","bishop")

    return bishops

def createKnights(self) -> list:
    """Creates all white, black knights in their standard locations."""
    # Stores a list of two lists, knights in each color (white first)
    knights = [[],[]]

    # Initialize the white knight coordinates (b1 and g1), create
    knights[0] += Knight(Point(1.5,0.5),self.win,"white","knight")
    knights[0] += Knight(Point(6.5,0.5),self.win,"white","knight")

    # Initialize the black knight coordinates (b8 and g8), create
    knights[1] += Knight(Point(1.5,7.5),self.win,"black","knight")
    knights[1] += Knight(Point(6.5,7.5),self.win,"black","knight")

    return knights

def createRooks(self) -> list:
    """Creates all white, black rooks in their standard locations."""
    # Stores a list of two lists, rooks in each color (white first)
    rooks = [[],[]]

    # Initialize the white rook coordinates (a1 and h1), create
    rooks[0] += Rook(Point(0.5,0.5),self.win,"white","rook")
    rooks[0] += Rook(Point(7.5,0.5),self.win,"white","rook")

    # Initialize the black rook coordinates (a8 and h8), create
    rooks[1] += Rook(Point(0.5,7.5),self.win,"black","rook")
    rooks[1] += Rook(Point(7.5,7.5),self.win,"black","rook")

    return rooks

def createQueens(self) -> list:
    """Creates all white, black queens in their standard locations."""
    # Stores a list of two lists, queens in each color (white first)
    queens = [[],[]]

    # Initialize the white queen coordinates (d1), create
    queens[0] += Queen(Point(3.5,0.5),self.win,"white","queen")

    # Initialize the black queen coordinates (d8), create
    queens[1] += Queen(Point(3.5,7.5),self.win,"black","queen")

    return queens

def createKings(self) -> list:
    """Creates all white, black kings in their standard locations."""
    # Stores a list of two lists, kings in each color (white first)
    kings = [[],[]]

    # Initialize the white king coordinates (e1), create
    kings[0] += King(Point(4.5,0.5),self.win,"white","king")

    # Initialize the black king coordinates (e8), create
    kings[1] += King(Point(4.5,7.5),self.win,"black","king")

    return kings

def createPieces(self) -> list:
    # Create all pieces from their subclass
    pawns = self.board_gui.createPawns()
    bishops = self.board_gui.createBishops()
    knights = self.board_gui.createKnights()
    rooks = self.board_gui.createRooks()
    queens = self.board_gui.createQueens()
    kings = self.board_gui.createKings()

    # First item contains white pieces, second contains black pieces
    for color in range(2):
        for piece in [pawns,bishops,knights,rooks,queens,kings]:
            self.pieces[color] += piece[color]

    return self.pieces
