# This is the Board GUI that manages all things interface.
#
# Import the superclass Button subclass Square class
from Button import *
from Square import *
from graphics import *

class BoardGUI:
    def __init__(self):
        # Create a graphics window called "Chess", 900x600
        self.win = GraphWin("Chess",900,600)
        # Set coordinates so each square move is 1
        self.win.setCoords(-8,-2,10,10)
        
        # Marks the origin (0,0), DELETE LATER
        self.origin = Text(Point(0,0),"ORIGIN")
        self.origin.draw(self.win)

        # Create a message label, box, and text
        self.message_label = Text(Point(-5,9),"Messages")
        self.message_label.setSize(15)
        self.message_label.draw(self.win)
        self.message_box = Rectangle(Point(-7.25,5.5),
                                     Point(-2.75,8.5)).draw(self.win)
        self.message = Text(Point(-5,7),"It is white's move.")
        self.message.setSize(18)
        self.message.draw(self.win)     

        # Create a quit button from the Button Class
        self.quit_button = Button(self.win,Point(-5,0),
                                  2,0.8,"Quit")

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
        board_label = [["a","b","c","d","e","f","g","h"],[1,2,3,4,5,6,7,8]]
        x,y = 0.5,8.5
        for alph in board_label[0]:
            point = Point(x,y)
            Text(point,alph).draw(self.win)
            x += 1
        x,y = 8.5,0.5
        for num in board_label[1]:
            point = Point(x,y)
            Text(point,num).draw(self.win)
            y += 1

###### END OF CLASS ######
def main():
    board = BoardGUI()

#TO-DOs:

#QUESTIONS:
