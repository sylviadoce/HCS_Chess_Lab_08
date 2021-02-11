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
        # Access the Piece Class variables
        self.piece = Piece()
        
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

    def createPieces(self) -> list:
        # This should return a list of lists each [piece, coord, color]

    def createPawns(self):
        # Create all white, black pawns in their standard locations
        # Use the Piece class to draw an image for the image param
        
    def createBishops(self):
        # Create all white, black bishops in their standard locations

    def createKnights(self):
        # Create all white, black knights in their standard locations

    def createRooks(self):
        # Create all white, black rooks in their standard locations

    def createQueens(self):
        # Create the white, black queen in her standard location

    def createKings(self):
        # Create the white, black king in his standard location

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
