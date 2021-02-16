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
        pawns = []
        
        # Initialize the white (bottom-left) pawn coordinates (a2)
        x,y = 0.5,1.5
        for i in range(8):
            pawns.append(Pawn(Point(x,y),self.win,"white","pawn"))
            x += 1

        # Initialize the black (top-left) pawn coordinates (a7)
        x,y = 0.5,6.5
        for i in range(8):
            pawns.append(Pawn(Point(x,y),self.win,"black","pawn"))

        return pawns
        
    def createBishops(self) -> list:
        # Create all white, black bishops in their standard locations

    def createKnights(self) -> list:
        # Create all white, black knights in their standard locations

    def createRooks(self) -> list:
        # Create all white, black rooks in their standard locations

    def createQueens(self) -> list:
        # Create the white, black queen in her standard location

    def createKings(self) -> list:
        # Create the white, black king in his standard location

    def createPieces(self) -> list:
        # This should return a list of two lists of objects:
        #   white pieces, black pieces (white is 0, black is 1)
        # This should draw each piece in the window

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
