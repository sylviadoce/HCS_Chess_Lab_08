

#move method outline:

user clicks on a square
#find which square was clicked
for sq in allsq:
    if sq.checkClicked(pt) == True:
        #find out who is occupying the square
        for piece in EnemyPieces:
            if piece.getLocation() == sq.getLocation():
                BoardGUI.setMessage("Wrong color")
                #display a message that they selected wrong color
        for piece in sameTeam:
            if piece.getLocation() == sq.getLocation():
                #this is valid
                #identify who is the king using getPieceType
                piece.getPossibleMoves(myKing,myTeam,enemyTeam)
                pt = win.getMouse()
                valid,enemyTeam,pieceImage = piece.movePiece(pt,enemyTeam)
                while valid == False:
                    valid,enemyTeam,sameTeam = piece.movePiece(pt,enemyTeam)
                for p in enemyTeam:
                    if p.getEaten():
                        p.remove(enemyTeam)
                        #remove eaten pieces from the list
