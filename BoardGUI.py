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
    def __init__(self,color):
##        # Access the Piece Class variables
##        self.piece = Piece()

        # Track what color team's turn it is
        self.color = color
        
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

    def locationCoordToLabel(self,location) -> str:
        """Converts a piece's coordinate to its alphabetized and
            numeric label."""
        
        loc_label = ""
        coord = 0.5
        # Associate the y/x coordinate with its respective letter/number
        print(location)
        for x in range(8):
            if location[0] == coord:
                loc_label += str(self.board_label[0][x])
                break
            coord += 1
        coord = 0.5
        for y in range(8):
            #print(location.getY())
            if location[1] == coord:
                loc_label += str(self.board_label[1][y])
                break
            coord += 1

        return loc_label

    def checkTurnColor(self):
        """Returns the color of whichever team's turn it is."""
        return self.color

    def updateTurn(self):
        """Updates the color and message to reflect whichever team's
            turn it is."""
        
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

        self.message.setText("It is " + self.color + "'s move.")

    def updateMessage(self,update):
        """Sets the message to update."""
        self.message.setText(update)

    def checkBoardStatus(self) -> int:
        """Returns the number of active board squares."""
        active = 0
        for sq in self.squares:
            if sq.active == True:
                active += 1

        return active

    def drawPiece(self,piece):
        """Draws the piece in the graphics window."""
        #pieceImg = Image(piece.getLocation(),piece.checkColor()+piece.getPieceType()+".png")
        piece.imageUpdate().draw(self.win)


    def undrawPiece(self,piece):
        """Undraws the piece in the graphics window."""

        self.drawPiece(piece).undraw(self.win)

    def getActiveSquares(self) -> list:
        """Returns a list of all the activated squares."""

        active_sqs = []
        for sq in self.squares:
            if sq.checkActive():
                active_sqs.append(sq)

        return active_sqs      

    def closeGame(self):
        self.win.close()

    def allClicks(self):
        """Handles all mouse clicks and carries out its respective
            action and/or message update. Returns the clicked item."""
        # Detect user mouse clicks
        pt = self.win.getMouse()
        
        # If the quit button is clicked, close the window
        if self.quit_button.clicked(pt):
            quit()
            
        # Check if a board square is clicked
        for sq in self.squares:
            # Identify the clicked square
            if sq.clicked(pt):
                return sq,"square"

        return "quit","quit"
                
##                # If another square is activated, check valid move
##                if self.checkBoardStatus != 0:
##                    # this needs to move the piece
##                    # if capturing a piece, the other piece is undrawn
##                    # Change the turn color (after successful move)
##                    self.updateTurnColor()
##                    return "move sq"
##                else:
##                    return "wrong sq"
                
## PUT IN CHESSGAME
##                # Check if the clicked square is occupied by a piece
##                for piece in pieces:
##                    for p in piece:
##                        if sq.getLocation() == p.getLocation():
##                            if p.checkColor() == self.color:
##                                # activate the possible squares
##                                # deactivate all other squares
##                                return "good sq"
##                            else:
##                                return "wrong sq"
##                        else:
##                            self.message.setText(
##                                "Please click on a",self.color,"piece")
##                            return "wrong sq"

    

###### END OF CLASS ######
def main():
    board = BoardGUI("white")
    board.allClicks()

#TO-DOs:
#   1. Keep track of which color team's turn it is
#   2. Figure out what piece color is on the square
#   3. Squares should only be able to be clicked if active

#QUESTIONS:
#   1. Is this truly encapsulated if I need Square and Piece to make it work?
        # Purely use the piece through a method, not instance
#   2. What's the best way to track which team's turn it is?
