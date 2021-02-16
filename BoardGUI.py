# Sylvia Chin
#
# This is the Board GUI that manages all things interface, including all
# board square, piece image, message, and quit capabilities.
#
# Import the superclass Button subclass Square class
from graphics import *
from Button import *
from Square import *
from Piece import *

class BoardGUI:
    def __init__(self):
##        # Access the Piece Class variables
##        self.piece = Piece()
        
        # Create a graphics window called "Chess", 900x600
        self.win = GraphWin("Chess",900,600)
        # Set coordinates so each square move is 1
        self.win.setCoords(-8,-2,10,10)
        
        # Marks the origin (0,0), DELETE LATER
        self.origin = Text(Point(0,0),"ORIGIN")
        self.origin.draw(self.win)

        # Create a message label, box, and text
        self.message_label = Text(Point(-5,9),"MESSAGES")
        self.message_label.setSize(14)
        self.message_label.draw(self.win)
        self.message_box = Rectangle(Point(-7.25,5.5),
                                     Point(-2.75,8.5)).draw(self.win)
        self.message = Text(Point(-5,7),"It is white's move.")
        self.message.setSize(18)
        self.message.draw(self.win)     

        # Create and activate a quit button from the Button Class
        self.quit_button = Button(self.win,Point(-5,0),
                                  2,0.8,"QUIT")
        self.quit_button.activate()

        # List to store all squares
        self.squares = []
        # Create all 64 chess board squares each 50x50, append to squares
        x,y = 0.5,0.5
        for row in range(8):
            for column in range(8):
                y_center = Point(x,y)
                square = Square(self.win,y_center,1,1)
                self.squares.append(square)
                y += 1
            y -= 8
            x += 1

        # Create the alphabetic and numeric board labels
        self.board_label = [["a","b","c","d","e","f","g","h"],
                            [1,2,3,4,5,6,7,8]]
        x,y = 0.5,8.5
        for alph in self.board_label[0]:
            point = Point(x,y)
            Text(point,alph).draw(self.win)
            x += 1
        x,y = 8.5,0.5
        for num in self.board_label[1]:
            point = Point(x,y)
            Text(point,num).draw(self.win)
            y += 1

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
        """Return a list of two lists of created objects: white pieces and
            black pieces (white is 0, black is 1)."""

        # Create all pieces from their subclass
        pawns = self.createPawns()
        bishops = self.createBishops()
        knights = self.createKnights()
        rooks = self.createRooks()
        queens = self.createQueens()
        kings = self.createKings()

        # Create a list of two lists storing all pieces
        # First item contains white pieces, second contains black pieces
        pieces = [[],[]]
        for color in range(2):
            for piece in [pawns,bishops,knights,rooks,queens,kings]:
                pieces[color] += piece[color]

##        # Draw all pieces in the graphics window
##        for color in range(2):
##            for piece in pieces[color]:
##                piece.draw(self.win)

        return pieces

    def locationCoordToLabel(self) -> str:
        """Converts a piece's coordinate to its alphabetized and
            numeric label."""
        
        loc_label = ""
        coord = 0.5
        # Associate the y/x coordinate with its respective letter/number
        for y in range(8):
            if self.piece[1][1] == coord:
                loc_label += str(self.board_label[0][y])
                break
            coord += 1
        coord = 0.5
        for x in range(8):
            if self.piece[1][0] == coord:
                loc_label += str(self.board_label[1][x])
                break
            coord += 1

        return loc_label


###### END OF CLASS ######
def main():
    board = BoardGUI()

#TO-DOs:

#QUESTIONS:
