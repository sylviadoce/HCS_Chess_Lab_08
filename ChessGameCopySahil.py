# Sylvia Chin
#
# Chess Games module that runs the game - class??
#
from Piece import *
from SylviaPieceSubclasses import *
from BishopKingQueen_Sahil import *
from BoardGUI import *

class ChessGame:
    def __init__(self):
        self.board_gui = BoardGUI("white")

        # Create a list of two lists storing all pieces
        self.pieces = [[],[]]

        self.checkmate = False

        # Getting either the white team (0) or black team (1)
        self.teamnum = [0,1]

    def createPawns(self) -> list:
        """Creates all white, black pawns in their standard locations."""
        # Stores a list of two lists, pawns in each color (white first)
        pawns = [[],[]]
        
        # Initialize the white (bottom-left) pawn coordinates (a2), create
        x,y = 0.5,1.5
        for i in range(8):
            pawns[0].append(Pawn(Point(x,y),"white","pawn","wp" + str(i+1)))
            x += 1

        # Initialize the black (top-left) pawn coordinates (a7), create
        x,y = 0.5,6.5
        for i in range(8):
            pawns[1].append(Pawn(Point(x,y),"black","pawn","bp" + str(i+1)))
            x += 1

        return pawns
        
    def createBishops(self) -> list:
        """Creates all white, black bishops in their standard locations."""
        # Stores a list of two lists, bishops in each color (white first)
        bishops = [[],[]]

        # Initialize the white bishop coordinates (c1 and f1), create
        bishops[0].append(Bishop(Point(2.5,0.5),"white","bishop","wb1"))
        bishops[0].append(Bishop(Point(5.5,0.5),"white","bishop","wb2"))

        # Initialize the black bishop coordinates (c8 and f8), create
        bishops[1].append(Bishop(Point(2.5,7.5),"black","bishop","bb1"))
        bishops[1].append(Bishop(Point(5.5,7.5),"black","bishop","bb1"))

        return bishops

    def createKnights(self) -> list:
        """Creates all white, black knights in their standard locations."""
        # Stores a list of two lists, knights in each color (white first)
        knights = [[],[]]

        # Initialize the white knight coordinates (b1 and g1), create
        knights[0].append(Knight(Point(1.5,0.5),"white","knight","wkn1"))
        knights[0].append(Knight(Point(6.5,0.5),"white","knight","wkn2"))

        # Initialize the black knight coordinates (b8 and g8), create
        knights[1].append(Knight(Point(1.5,7.5),"black","knight","bkn1"))
        knights[1].append(Knight(Point(6.5,7.5),"black","knight","bkn2"))

        return knights

    def createRooks(self) -> list:
        """Creates all white, black rooks in their standard locations."""
        # Stores a list of two lists, rooks in each color (white first)
        rooks = [[],[]]

        # Initialize the white rook coordinates (a1 and h1), create
        rooks[0].append(Rook(Point(0.5,0.5),"white","rook","wr1"))
        rooks[0].append(Rook(Point(7.5,0.5),"white","rook","wr1"))

        # Initialize the black rook coordinates (a8 and h8), create
        rooks[1].append(Rook(Point(0.5,7.5),"black","rook","br1"))
        rooks[1].append(Rook(Point(7.5,7.5),"black","rook","br2"))

        return rooks

    def createQueens(self) -> list:
        """Creates all white, black queens in their standard locations."""
        # Stores a list of two lists, queens in each color (white first)
        queens = [[],[]]

        # Initialize the white queen coordinates (d1), create
        queens[0].append(Queen(Point(3.5,0.5),"white","queen","wq1"))

        # Initialize the black queen coordinates (d8), create
        queens[1].append(Queen(Point(3.5,7.5),"black","queen","bq1"))

        return queens

    def createKings(self) -> list:
        """Creates all white, black kings in their standard locations."""
        # Stores a list of two lists, kings in each color (white first)
        kings = [[],[]]

        # Initialize the white king coordinates (e1), create
        kings[0].append(King(Point(4.5,0.5),"white","king","wk1"))

        # Initialize the black king coordinates (e8), create
        kings[1].append(King(Point(4.5,7.5),"black","king","bk1"))

        return kings

    def createPieces(self) -> list:
        # Create all pieces from their subclass
        pawns = self.createPawns()
        bishops = self.createBishops()
        knights = self.createKnights()
        rooks = self.createRooks()
        queens = self.createQueens()
        kings = self.createKings()

        # First item contains white pieces, second contains black pieces
        for color in range(2):
            for piece in [pawns,bishops,knights,rooks,queens,kings]:
                self.pieces[color] += piece[color]

        # Draw each piece to the graphics window
        for piece in self.pieces:
            for p in piece:
                self.board_gui.drawPiece(p)

        self.whitepieces = self.pieces[0]
        self.blackpieces = self.pieces[1]

        return self.pieces

    def pawnToQueen(self,pawn):
        """Replaces a pawn with a queen once at the end of the board."""
        
        colors = ["white","black"]
        
        # Delete the pawn object, undraw the pawn image, and create a new
        #   queen for the player's team color at the same location
        loc = pawn.getLocation()
        for i in range(2):
            if self.color == colors[i]:
                self.pieces[i].remove(pawn)
                self.board_gui.undrawPiece(pawn)
                self.pieces[i].append(Queen(loc,colors[i],"queen"))

    def getEnemyTeam(self):
        if self.board_gui.checkTurnColor() == "white":
            self.enemyPieces = self.pieces[1]
        else:
            self.enemyPieces = self.pieces[0]

        return self.enemyPieces

    def getMyTeam(self):
        if self.board_gui.checkTurnColor() == "white":
            self.sameTeam = self.pieces[0]
        else:
            self.sameTeam = self.pieces[1]

        return self.sameTeam

    def removePiece(self,piece):
        if piece.checkColor() == "white":
            self.pieces[0].remove(piece)

        else:
            self.pieces[1].remove(piece)
            
    def getEnemyKing(self) -> list:
        if self.board_gui.checkTurnColor() == "white":
            for bpiece in self.pieces[1]:
                if bpiece.getPieceType() == "king":
                    enemyKing = bpiece
                    
                    return enemyKing
        else:
            for wpiece in self.pieces[0]:
                if wpiece.getPieceType() == "king":
                    enemyKing = wpiece
                    
                    return enemyKing


    def getMyKing(self) -> list:
        if self.board_gui.checkTurnColor() == "white":
            for wpiece in self.pieces[0]:
                if wpiece.getPieceType() == "king":
                    myKing = wpiece
                    
                    return myKing
        else:
            for bpiece in self.pieces[1]:
                if bpiece.getPieceType() == "king":
                    myKing = bpiece
                    
                    return myKing

##    def afterMoveMessage(self,p,capture:bool,capture_id#HOW TO INCORPORATE?):
##        if checkmate: #DO
##            message = str(p.checkColor()).capitalize(),"moved",
##            p.getPieceType(),"to",
##            self.board_gui.locationCoordToLabel(p.getLocationXY()),
##            "-- Checkmate!" )
##        elif check: #DO
##            message = str(p.checkColor()).capitalize() + " moved "
##            + p.getPieceType() " to " +
##            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
##            "\n (Check) -- It is now \n" +
##            self.board_gui.updateTurn().capitalize() + "'s move.")
##        elif capture: #DO
##            message = str(p.checkColor()).capitalize() + "'s "
##            + p.getPieceType() "captured \n" +
##            self.board_gui.updateTurn().capitalize() + "'s " +
##            capture_id + " at "
##            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
##            "\n -- It is now \n" +
##            self.board_gui.updateTurn().capitalize() + "'s move.")
##        else:
##            message = str(p.checkColor()).capitalize() + " moved "
##            + p.getPieceType() " to " +
##            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
##            "\n -- It is now \n" +
##            self.board_gui.updateTurn().capitalize() + "'s move.")
            

    def main(self):
        """Runs the game, using functions to move the pieces."""

        # Create the pieces
        pieces = self.createPieces()

##        # Set up a list to store the authentic click (choosing a piece)
##        choice = []

        # Loop while the game is not ended (no king in checkmate)
        while not self.checkmate:
            #print("while loop")
            # Set up a list and counter to track clicked squares
            clicked_sqs = []
            clicked_sq = 0

            # Set up a list to store the authentic click (choosing a piece)
            choice = []

            pop_sq = False
            
            click = self.board_gui.allClicks()
            if click[1] == "square":
                # Set the clicked square status to clicked (True)
                click[0].setClicked()

                #print("before this clicked_sqs",clicked_sqs)

                # Check if another square has already been clicked
                for square in self.board_gui.squares:
                    # For first move, bypass conditionals
                    if choice == [] and square.checkClicked():
                        #print("first move")
                        clicked_sq += 1
                        clicked_sqs.append(square)
                        break
                    # Remove any invalid second clicks
                    elif (square.checkClicked() and (square.getLocation()
                        != choice[0].getLocation())):
                        #print("invalid other sq clicked")
                        # Remove the invalid square
                        clicked_sqs.remove(square)
                        # If one of the possible spots
                        if square.checkActive():
                            print("adding here")
                            clicked_sq += 1
                            clicked_sqs.append(square)
                        

                print("after this clicked_sqs",clicked_sqs)

                # If choosing a piece (one square click)
                if clicked_sq == 1:
                    #print("one click")
                    for lstPiece in pieces:
                        for p in lstPiece:
                            #print("loop")
                            pop_sq = False
                            on_piece = False
                            move_on = False
                            #print(p.checkPieceID)
                            #print(click[0].getLocation(),p.getLocationXY())
                            # Check if a piece is on the square
                            if (click[0].getLocation() == p.getLocationXY()):
                                # If wrong team, update message
                                if (p.checkColor() !=
                                    self.board_gui.checkTurnColor()):
                                    print("place1")
                                    self.board_gui.updateMessage(
                                        "Please click on a \n" +
                                        self.board_gui.checkTurnColor() +
                                        " piece!")
                                    pop_sq = True
                                    move_on = True
                                    break
                                # If right team, get possible moves
                                else:
                                    print("over here")
                                    on_piece = True
                                    spots = p.getPossibleMoves(
                                        self.getMyKing(),
                                        self.getEnemyKing(),
                                        self.getMyTeam(),
                                        self.getEnemyTeam(),"y")
                                    selectedPiece = p
                                    #print(p.checkColor,p.getPieceType(),"Piece being moved")
                                    #for piece in [self.getMyKing(),
                                        #self.getEnemyKing()]:
                                        #print(piece.getPieceType(),piece.checkColor())
                                    #for piece in self.getMyTeam():
                                        #print(piece.getPieceType(),piece.checkColor())
                                    #for piece in self.getEnemyTeam():
                                        #print(piece.getPieceType(),piece.checkColor())
                                    #print(spots) 
                                    # Check if the piece has possible spots
                                    if spots != []:
                                        self.board_gui.updateMessage(
                                            "Please select a move \n"
                                            "from the indicated \n"
                                            "options")
                                        on_piece = True
                                        # this is the authentic scenario
                                        # Activate possible spots
                                        for spot in spots:
                                            for sq in self.board_gui.squares:
                                                x,y = spot.getX(),spot.getY()
                                                if x == sq.getLocation()[0] and y == sq.getLocation()[1]:
                                                    sq.activate()
                                        choice.append(p)
                                        move_on = True
                                        break
                                    # If not, update message
                                    else:
                                        self.board_gui.updateMessage(
                                            "That piece does not have \n"
                                            "any legal moves -- \n"
                                            "please pick another piece.")
                                        pop_sq = True
                                        move_on = True
                                        break
                        # Get out of second for loop!!!
                        if move_on:
                            break

                    print("out of for loops")

                    # Check if it is the right team's piece 
                    if on_piece == False:
                        print("place2")
                        self.board_gui.updateMessage(
                            "Please click on a \n" +
                            self.board_gui.checkTurnColor() +
                            " piece!")
                        pop_sq = True
                if pop_sq:
                    print("go over here to remove!")
                    clicked_sqs[0].resetClicked()
                    clicked_sqs.pop(0)

                print("before clicked_sqs:", clicked_sqs)

                #### SECOND CLICK STUFF - AFTER ONE VALID CLICK ####

                # Expect a second click that is a square
                click_two = self.board_gui.allClicks()
                if click_two[1] != "square" or not click_two[0].checkActive():
                    print("not an option")
                    continue

                print("active squares: ", self.board_gui.getActiveSquares())
                # If the square is active, append it to the list of clicks
                for sq in self.board_gui.getActiveSquares():
                    if sq.getLocation() == click_two[0].getLocation():
                        print("clicking on an active sq")
                        clicked_sqs.append(click_two[0])
                        clicked_sq += 1
                        valid_move = True
                        break
                    # If not an active square, display error message
                    else:
                        print("error1111")
                        valid_move = False
                        self.board_gui.updateMessage(
                            "That is not a valid move. \n"
                            "Please try again.")
                        click_two[0].resetClicked()

##                # Check again if another square has already been clicked
##                #   in case the first click was inauthentic
##                for square in self.board_gui.squares:
##                    if square.checkClicked():
##                        for i in clicked_sqs:
##                            if i not in clicked_sqs:
##                                print("checking clicks correctly")
##                                clicked_sq += 1
##                                clicked_sqs.append(square)

                print("after clicked_sqs:", clicked_sqs)
                print("after counter:", clicked_sq)
                
                # If placing a piece (already one authentic square click)
                if clicked_sq == 2:
                    print("2 clicks!!")
                    # Check if the clicked square is occupied
                    for piece in pieces:
                        for p in piece:
                            print("beginning",p.getPieceType(),p.checkColor())
                            # If occupied, check the piece's team
                            if (p.getLocationXY() ==
                                click_two[0].getLocation()):
                                # If same team, update message
                                if (p.checkColor() ==
                                    choice[0].checkColor()):
                                    print("error2222")
                                    self.board_gui.updateMessage(
                                        "That is not a valid move. \n"
                                        "Please try again.")
##                                    clicked_sqs[1].resetClicked()
##                                    clicked_sqs.pop(1)
                                # If other team, check if it's a valid move
                                # (not putting king in check,possible move)
                                # If so, capture the piece and remove it
                                else:
                                    print("sahil1")
                                    enemyPieces = selectedPiece.movePiece(click_two[0].getLocation(),self.getEnemyTeam())
                                    for piece in enemyPieces:
                                        if piece.getEaten() == True:
                                            for sq in self.board_gui.squares:
                                                if (sq.getLocation()[0] == piece.getLocationXY()[0]) and (sq.getLocation()[1] == piece.getLocationXY()[1]):
                                                    sq.resetOccupiedSquare()
                                            self.removePiece(piece)
                                    self.board_gui.drawPiece(selectedPiece)
                                    # Sahil's stuff here?
                                    # actually moving the piece
                                    # make sure to update message
                                    # BREAK OUT OF THE WHILE LOOP
                            # If empty, check if it's a valid move
                            # (not putting king in check,possible move)
                            else:
                                print("validMove",valid_move)
                                print(p.checkPieceID)
                                print(choice[0].checkPieceID)
                                if valid_move: #and (p.checkPieceID == choice[0].checkPieceID):
                                    print("sahil2")
                                    # sahil stuff here
                                    #move the piece
                                    x,y = selectedPiece.getLocationXY()
                                    enemyPieces = selectedPiece.movePiece(click_two[0].getLocation(),self.getEnemyTeam())
                                    for piece in enemyPieces:
                                        if piece.getEaten():
                                            print("a piece is eaten")
                                            for sq in self.board_gui.squares:
                                                if (sq.getLocation()[0] == piece.getLocationXY()[0]) and (sq.getLocation()[1] == piece.getLocationXY()[1]):
                                                    sq.resetOccupiedSquare()
                                            self.removePiece(piece)
                                    #reset square
                                    click[0].resetOccupiedSquare()
                                    self.board_gui.drawPiece(selectedPiece)
                                    print("CHOICEXY:",x,y)
                                    print("CHOICE LOC:", choice[0].getLocationXY())
                                    
                                    #self.board_gui.undrawPiece(piece)
                                    for sq in self.board_gui.getActiveSquares():
                                        sq.deactivate()
                                    #self.board_gui.drawPiece(p)
                                    
                                    
                                    # actually moving the piece to an
                                    #   empty square
                                    self.board_gui.updateTurn()
                                    #REPLACE W AFTERMOVEMESSAGE FUNCTION
                                    message = (
                                        selectedPiece.checkColor(),"moved",
                                        selectedPiece.getPieceType(),"to",
                                        self.board_gui.locationCoordToLabel(
                                            selectedPiece.getLocationXY()))
                                    self.board_gui.updateMessage(message)
                                    for sq in self.board_gui.squares:
                                        sq.resetClicked()
                                    
                
                                    
                                    break
                                else:
                                    print("here")
                                    continue
##                                    clicked_sqs.remove(click_two[0])
                                    x,y = p.getLocationXY()
                                    #enemyPieces = p.movePiece(click_two[0].getLocation(),self.getEnemyTeam())
                                    #reset square
                                    #click[0].resetOccupiedSquare()
                                    self.board_gui.drawPiece(p)
                                    #print("CHOICEXY:",x,y)
                                    #print("CHOICE LOC:", choice[0].getLocationXY())
                                    p1 = Point(x-0.5,y-0.5)
                                    p2 = Point(x+0.5,y+0.5)
                                    rect=Rectangle(p1,p2)
                                    rect.setFill(click[0].getColor())
                                    rect.draw(self.board_gui.win)
                                    #self.board_gui.undrawPiece(piece)
                                    for sq in self.board_gui.getActiveSquares():
                                        sq.deactivate()
                                # Sahil's stuff here?
                                # actually moving the piece
                                # make sure to update message
                                # break out of the while loop
                        break

        while True:
           click = self.board_gui.allClicks()
           if str(click) != ("quit","quit"):
                self.board_gui.closeGame()
                ChessGame().main()        
        
ChessGame().main()

#TO-DOs:
#   1. Function to check for checkmate in Piece Class that returns boolean
#   2. Pawn transformation into Queen (del pawn object and create w queen?)
#   3. Update square and button with edits, make sure importing the correct
#       module.
#   4. Make sure the pieces can distinguish between going through other
#       pieces when moving, exception: knights
#   5. Update the message after each turn to specifics of the move.

#QUESTIONS:
#   1. Do you want us to show both "It is white's/black's move" AND ex.
#       "White moved bishop to f4 -- it is now Black’s move." or just the
#       latter?
