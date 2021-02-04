from Button import *

class Square():
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
        #self.label=Text(center,label)
        #self.label.draw(win)
        #self.deactivate()

#convert coordinates from standard to 0-7


    def activate(self):
        self.rect.setFill("red")
        
