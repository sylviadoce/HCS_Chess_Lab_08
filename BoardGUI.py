# This is the Board GUI that manages all things interface.
#
# Import the superclass Button subclass Square class
##from Square import Square
from Button import *
from graphics import *

class BoardGUI:
    def __init__(self):
        self.win = GraphWin("Chess",900,600)
        self.quit_button = Button(self.win,Point(160,420),
                                  100,40,"Quit")
        self.message_label = Text(Point(160,160),"Instructions")
        self.message_label.setSize(15)
        self.message_label.draw(self.win)
        self.message_box = Rectangle(Point(50,320),
                                     Point(270,180)).draw(self.win)
        self.message = Text(Point(160,250),"It is white's move.")
        self.message.setSize(18)
        self.message.draw(self.win)
        
        self.squares = [Square()]
        for sq in self.squares:
            sq.draw(self.win)
                        

###### END OF CLASS ######
def main():
    board = BoardGUI()

#TO-DOs:

#QUESTIONS:
