# This is the Board GUI that manages all things interface.
#
# Import the superclass Button subclass Square class
##from Square import Square
from Button import *
from Square import *
from graphics import *

class BoardGUI:
    def __init__(self):
        # Create a graphics window called "Chess", 900x600
        self.win = GraphWin("Chess",900,600)
        # Set coordinates so the board's corner is (0,0)
        self.win.setCoords(-400,-80,500,520)

        # Create a message label, box, and text
        self.message_label = Text(Point(-240,450),"Messages")
        self.message_label.setSize(15)
        self.message_label.draw(self.win)
        self.message_box = Rectangle(Point(-350,300),
                                     Point(-130,430)).draw(self.win)
        self.message = Text(Point(-240,365),"It is white's move.")
        self.message.setSize(18)
        self.message.draw(self.win)

        # Create a quit button from the Button Class
        self.quit_button = Button(self.win,Point(-240,0),
                                  100,40,"Quit")

        # Marks the origin (0,0), DELETE LATER
        self.origin = Text(Point(0,0),"ORIGIN")
        self.origin.draw(self.win)

        # List to store all squares
        self.squares = []
        # Create all 64 chess board squares each 50x50, append to squares
        x,y = 25,25
        for row in range(8):
            for column in range(8):
                y_center = Point(x,y)
                square = Square(self.win,y_center,50,50)
                self.squares.append(square)
                y += 51
            y -= 51*8
            x += 51

        # Create the alphabetic and numeric board labels
        board_label = [["a","b","c","d","e","f","g","h"],[1,2,3,4,5,6,7,8]]
        x,y = 25,425
        for alph in board_label[0]:
            point = Point(x,y)
            Text(point,alph).draw(self.win)
            x += 51
        x,y = 425,25
        for num in board_label[1]:
            point = Point(x,y)
            Text(point,num).draw(self.win)
            y += 51

###### END OF CLASS ######
def main():
    board = BoardGUI()

#TO-DOs:

#QUESTIONS:
