

#move method outline:

sq = self.board_gui.allClicks()
#did the user click the quit button?
if sq.getType() == "QUIT":
    quitClicked = True
else:
    quitClicked = False

#execute all of this only if quitbutton not clicked
if quitClicked = False:    
    #find out who is occupying the square
    #Is it the enemy team?
    for piece in EnemyPieces:
        #we are finding out who is the king (will be useful later on)
        if piece.getPieceType() == "king":
            enemyKing = piece
        if piece.getLocation() == sq.getLocation():
            #If it is, then they selected the wrong color
            BoardGUI.setMessage("Wrong color")
            break
    #Are they a piece on the correct team?
    for piece in sameTeam:
        #identify who is the king using getPieceType
        if piece.getPieceType() == "king":
            myKing = piece
        if piece.getLocation() == sq.getLocation():
            #this is valid
            piece.getPossibleMoves(myKing,enemyKing,myTeam,enemyTeam,piece.calcListDirections(),piece.getNumSpaces(),"y")
            #activate the correct squares

            #get mouse input
            sq = self.board_gui.allClicks()
            if sq.getType() == 
            valid,enemyTeam,pieceImage = piece.movePiece(sq.getLocation(),enemyTeam)
            #input validation - what did the user click? An activated square, another piece, etc.
            while valid == False:
                valid,enemyTeam,sameTeam = piece.movePiece(pt,enemyTeam)
            #After the piece moved, check if a piece on the enemyTeam was eaten. If so, then remove it from the list of enemy pieces.
            noneCaptured = True
            for p in enemyTeam:
                if p.getEaten():
                    noneCaptured = False
                    p.remove(enemyTeam)
                    #message showing capture
                    #remove eaten pieces from the list
            if noneCaptured:
                #check if the king is in check
                check = enemyKing.getKingCheck(myKing,sameTeam,enemyTeam)
                #if the enemy king is in check, check for checkmate
                if check:
                    for piece in enemyTeam:
                        possibleMovesUnderCheck = piece.getPossibleMoves(enemyKing,myKing,enemyTeam,myTeam,piece.calcListDirections(),piece.getNumSpaces())
                        if possibleMovesUnderCheck == []:
                            checkmate = True
                        else:
                            checkmate = False
                    if checkmate = True:
                        #This is checkmate
                    else:
                        #It is just a check
                else:
                    #This was just a normal move
        else:
            self.board_gui.setMessage("No Piece on this square")

