# HCS Lab 08 - Chess
# Name: Sahil Agrawal
#
# This module creates the Button class.

from graphics import *

class Button:

    """A button is a labeled rectangle in a window. It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method returns true if the button is active and p is inside it."""

    def __init__(self,win,center,width,height,label):
        """creates a rectangular button, eg:
        qb=Button(myWin,centerPoint, width, height, 'Quit')"""
        self.center = center
        w,h=width/2.0,height/2.0
        x,y=center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1=Point(self.xmin, self.ymin)
        p2=Point(self.xmax, self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label=Text(center,label)
        self.label.draw(win)
        self.deactivate()

        self.click = False

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active=True
        
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active=False

    def getLabel(self):
        """Returns the label of the button."""
        return self.label.getText()
        
    def clicked(self,pt):
        """Returns true if pt (click) is inside."""
        if (self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax):
            self.click = True
            return True
        else:
            return False

    def checkClicked(self) -> bool:
        """Returns the boolean value of click."""
        return self.click

    def setClicked(self) -> bool:
        """Sets the click status to True."""
        self.click = True
        return self.click

    def resetClicked(self) -> bool:
        """Sets the click status to False."""
        self.click = False
        return self.click

    def setLabel(self,newText):
        """Sets the text of the button"""
        self.label.setText()

    def undraw(self):
        """Undraws the button from the window."""
        self.rect.undraw()
        self.label.undraw()

    def getX(self):
        """Returns the x value."""
        return self.center.getX()
    
    def getY(self):
        """Returns the y value."""
        return self.center.getY()
