# HCS Lab 04
# Name: Sahil Agrawal
#
# This module creates the Button class.

from graphics import *

class Button:

    """A button is a labeled rectangle in a window. It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method returns true if the button is active and p is inside it."""

    #creating a button object parameters
    def __init__(self,win,center,width,height,label):
        """creates a rectangular button, eg:
        qb=Button(myWin,centerPoint, width, height, 'Quit')"""

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

    #activate a button
    def activate(self):
        """sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active=True
        
    #deactivate the button
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active=False
    #accessor - returns the text of self.label
    def getLabel(self):
        """Returns true if button active and p is inside"""
        return self.label.getText()
        
    #registers if the button was clicked
    def clicked(self,pt):
        """Returns true if button active and pt is inside"""
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    #sets the text of self.label
    def setLabel(self,newText):
        """Sets the text of the button"""
        self.label.setText()

    def undraw(self):
        """undraws the button from the window"""
        self.rect.undraw()
        self.label.undraw()