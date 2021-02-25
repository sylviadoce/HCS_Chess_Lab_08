from Piece import *
from BishopKingQueen_Sahil import *
from Subclasses2 import *
from graphics import *

win = GraphWin("title",500,500)
win.setCoords(-5,-5,10,10)

#queen = Queen(Point(3,2),win,"black","queen")
#queen.imageUpdate().draw(win)
king = King(Point(3.5,0.5),"black","king")
kingImage = king.imageUpdate()
kingImage.draw(win)
king2 = King(Point(3.5,7.5),"white","king")
(king2.imageUpdate()).draw(win)
bishop = Bishop(Point(2.5,2.5),"white","bishop")
bishopImage = bishop.imageUpdate()
bishopImage.draw(win)

enemyPieces = [king]
sameTeam = [king2,bishop]

spots = bishop.getPossibleMoves(king2,king,[bishop],enemyPieces,bishop.calcListDirections(),10,"y")

