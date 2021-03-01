# Sahil
# HCS Lab 08 - Chess
#
# This is the Square subclass of superclass Button that represents each
#   square of the chess board.
#
from Button import *
from graphics import *

class Square(Button):
    def __init__(self,win,center,width,height):
        """Initializes the square with instance variables including
            dimension, point, window, color, and active."""
        w,h=width/2.0,height/2.0
        x,y=center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        self.p1=Point(self.xmin, self.ymin)
        self.p2=Point(self.xmax, self.ymax)
        self.rect=Rectangle(self.p1,self.p2)
        self.win = win
        # Alternate between white and grey squares
        if (center.getX()+center.getY())%2 == 0:
            self.color = "white"
        else:
            self.color = "gray"
        self.rect.setFill(self.color)
        self.rect.draw(win)
        self.center = center
        self.active = False
        self.occupied = False

    def activate(self):
        """Activates the square visually and sets boolean to True."""
        self.rect.setFill("red")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Deactivates the square visually and sets boolean to False."""
        self.rect.setFill(self.color)
        self.rect.setWidth(1)
        self.active = False

    def setOccupied(self):
        """Returns the boolean status of occupied."""
        self.occupied = True

    def resetOccupiedSquare(self):
        """Resets the square's occupied status, creates a rectangle
            ro cover up the old piece."""
        self.occupied = False
        self.rect=Rectangle(self.p1,self.p2)
        self.rect.setFill(self.color)
        self.rect.draw(self.win)

    def getLocation(self):
        """Returns two values, x and y."""
        return self.center.getX(),self.center.getY()

    def checkActive(self):
        """Returns the active boolean for squares."""
        return self.active

    def getType(self):
        """Returns the type of the square."""
        return self.type

    def getColor(self):
        """Returns the color of the square."""
        return self.color
