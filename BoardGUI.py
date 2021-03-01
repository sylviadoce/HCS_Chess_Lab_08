# Sylvia Chin
#
# This is the Board GUI that manages all things interface, including all
# board squares, piece images, messages, and quit capabilities. Uses the
# graphics, Button, and Piece classes, and subclass Square.
#
from graphics import *
from Button import *
from Square import *

class BoardGUI:
    def __init__(self,color):
        """Initializes the game's graphics, including a variable to
            track the current team's color, the window, the message
            label/box/text, the quit button, and all board squares."""
        # Track what color team's turn it is
        self.color = color
        
        # Create a graphics window called "Chess", 900x600
        self.win = GraphWin("Chess",900,600)
        # Set coordinates so each square move is 1 - bottom left square's
        #   center is (0.5,0.5)
        self.win.setCoords(-8,-2,10,10)

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
        # Create all 64 chess board squares each 1x1, append to squares
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

    def getWin(self):
        """Returns the graphics window instance variable."""
        return self.win

    def getSquares(self) -> list:
        """Returns the list of all board squares."""
        return self.squares

    def locationCoordToLabel(self,location) -> str:
        """Converts a piece's coordinate to its alphabetized and
            numeric label."""
        loc_label = ""
        coord = 0.5
        # Associate the y/x coordinate with its respective letter/number
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
        """Updates the color to reflect whichever team's turn it is."""   
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

        return self.color

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
        """Closes the graphics window."""
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
