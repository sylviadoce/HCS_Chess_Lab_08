<<<<<<< Updated upstream
from Button import *
from graphics import *

class Square(Button):
    #Works
    def __init__(self,win,center,width,height):
        w,h=width/2.0,height/2.0
        x,y=center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1=Point(self.xmin, self.ymin)
        p2=Point(self.xmax, self.ymax)
        self.rect=Rectangle(p1,p2)
        if (center.getX()+center.getY())%2 == 0:
            self.color = "gray"
        else:
            self.color = "white"
        self.rect.setFill(self.color)
        self.rect.draw(win)
        self.center = center
        self.active = False
        self.occupied = False
        #self.label=Text(center,label)
        #self.label.draw(win)
        #self.deactivate()

#convert coordinates from standard to 0-7

    #Use this after the correct squares have been calculated
    #Will set the square to show the correct image
        #Works
    def activate(self):
        self.rect.setFill("red")
        self.rect.setWidth(2)
        self.active = True

    #call this after the move has ended, and when calculating the squares
        #Works
    def deactivate(self):
        self.rect.setFill(self.color)
        self.rect.setWidth(1)
        self.active = False

    #Still needs work
    def clicked(self,pt):
        if (self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax):
            if self.active == True and self.occupied == False:
                return ("valid move")
                #valid move
            elif self.active == False and self.occupied == True:
                return ("There is a piece on this square")
                
                #TODO: find out who is occupying the square
                
                #If an enemy piece in the range of the piece, then it is valid
                #Else, not valid
            else:
                return("3")
                #This shouldn't happen, but we can use this for testing
                
        

    #If a piece is on the square
    def setOccupied(self):
        self.occupied = True

    #If a piece is not on the square
        #Not sure if this is needed yet - 
    def resetOccupiedSquare(self):
        #Call this after a piece has moved off of the square it was occupying
        self.occupied = False
        self.rect.setFill(self.color)
        

    def getLocation(self):
        #how de handle the coordinate grid?
        #We can convert everything to 0-7
        return self.center.getX(),self.center.getY()


      

def main():
    win=GraphWin("Hi",800,600)
    sq = Square(win,Point(50,50),20,20)
    sq.activate()
    c = sq.clicked(Point(50,50))
    print(c)
    '''
    sq.deactivate()
    pt=win.getMouse()
    
    point = Point(50,50)
    sq.clicked(pt)
    '''

main()


=======
from Button import *
from graphics import *

class Square(Button):
    #Works
    def __init__(self,win,center,width,height):
        w,h=width/2.0,height/2.0
        x,y=center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1=Point(self.xmin, self.ymin)
        p2=Point(self.xmax, self.ymax)
        self.rect=Rectangle(p1,p2)
        if (center.getX()+center.getY())%2 == 0:
            self.color = "gray"
        else:
            self.color = "white"
        self.rect.setFill(self.color)
        self.rect.draw(win)
        self.center = center
        #self.label=Text(center,label)
        #self.label.draw(win)
        #self.deactivate()

#convert coordinates from standard to 0-7

    #Use this after the correct squares have been calculated
    #Will set the square to show the correct image
        #Works
    def activate(self):
        self.rect.setFill("red")
        self.rect.setWidth(2)
        self.active = True

    #call this after the move has ended, and when calculating the squares
        #Works
    def deactivate(self):
        self.rect.setFill(self.color)
        self.rect.setWidth(1)
        self.active = False

    #Still needs work
    def clicked(self,pt):
        if (self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax):
            if self.active == True and self.occupied == False:
                print("valid move")
                #valid move
            elif self.active == False and self.occupied == True:
                print("There is a piece on this square")
                #find out who is occupying the square
                #If an enemy piece in the range of the piece, then it is valid
                #Else, not valid
            else:
                print("3")
                #This shouldn't happen, but we can use this for testing
                
        

    #If a piece is on the square
    def occupied(self):
        self.occupied = True

    #If a piece is not on the square
        #Not sure if this is needed yet - 
    def resetOccupiedSquare(self):
        #Call this after a piece has moved off of the square it was occupying
        self.occupied = False
        self.rect.setFill(self.color)
        

    def getLocation(self):
        #how de handle the coordinate grid?
        #We can convert everything to 0-7
        return self.center.getX(),self.center.getY()


      
##
##def main():
##    win=GraphWin("Hi",800,600)
##    sq = Square(win,Point(50,50),20,20)
##    pt = win.getMouse()
##    sq.activate()
##    pt = win.getMouse()
##    '''
##    sq.deactivate()
##    pt=win.getMouse()
##    
##    point = Point(50,50)
##    sq.clicked(pt)
##    '''
##    sq.resetOccupiedSquare()
##
##main()


>>>>>>> Stashed changes
