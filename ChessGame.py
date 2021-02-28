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
            pawns[0].append(Pawn(Point(x,y),"white","pawn","wp"+str(i+1)))
            x += 1

        # Initialize the black (top-left) pawn coordinates (a7), create
        x,y = 0.5,6.5
        for i in range(8):
            pawns[1].append(Pawn(Point(x,y),"black","pawn","bp"+str(i+1)))
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

        # Set up a list to store the authentic click (choosing a piece)
        choice = []

        # Loop while the game is not ended (no king in checkmate)
        while not self.checkmate:
            valid_move = False

            # Expect a click in the graphics window
            click = self.board_gui.allClicks()

            # If the click is not on a square, loop
            if click[1] != "square":
                continue
            
            # Check if clicktwo is False (choosing a piece) or
                # True (placing a valid piece)
            clicktwo = False
            for sq in self.board_gui.squares:
                if sq.checkActive():
                    print("clicktwo is True")
                    clicktwo = True
                    valid_move = True
                    break

            # clicktwo is False (choosing a piece)
            if not clicktwo:
                #print("one click")
                for lstPiece in pieces:
                    for p in lstPiece:
                        invalid = False
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
                                invalid = True
                                break
                            # If right team, get possible moves
                            else:
                                print("over here")
                                spots = p.getPossibleMoves(
                                    self.getMyKing(),
                                    self.getEnemyKing(),
                                    self.getMyTeam(),
                                    self.getEnemyTeam(),"y")
                                selectedPiece = p
                                # Check if the piece has possible spots
                                if spots != []:
                                    self.board_gui.updateMessage(
                                        "Please select a move \n"
                                        "from the indicated \n"
                                        "options")
                                    # this is the authentic scenario
                                    # Activate possible spots
                                    for spot in spots:
                                        for sq in self.board_gui.squares:
                                            x,y = spot.getX(),spot.getY()
                                            if (x == sq.getLocation()[0]
                                                and
                                                y == sq.getLocation()[1]):
                                                sq.activate()
                                    # Choice stores the valid piece,square
                                    choice.append(p)
                                    choice.append(click[0])
                                    valid_move = True
                                    invalid = True
                                    break
                                # If not, update message
                                else:
                                    self.board_gui.updateMessage(
                                        "That piece does not have \n"
                                        "any legal moves -- \n"
                                        "please pick another piece.")
                                    invalid = True
                                    break
                    # If invalid, get out of 2nd for loop
                    if invalid:
                        break

            # clicktwo is True (placing a piece)
            if clicktwo:
                print("sahil2")
                # Move the piece to the clicked square
                x,y = selectedPiece.getLocationXY()
                enemyPieces = selectedPiece.movePiece(
                    click[0].getLocation(),self.getEnemyTeam())
                # Check whether a piece was eaten, save it to a variable
                for piece in enemyPieces:
                    if piece.getEaten():
                        print("a piece is eaten")
                        captured = piece
                        # Reset the captured piece's square
                        for sq in self.board_gui.squares:
                            if ((sq.getLocation()[0] ==
                                 piece.getLocationXY()[0]) and
                                (sq.getLocation()[1] ==
                                 piece.getLocationXY()[1])):
                                sq.resetOccupiedSquare()
                        # Remove the captured piece from the pieces list
                        self.removePiece(piece)
                # Reset the original square, redraw the piece at new loc
                choice[1].resetOccupiedSquare()
                self.board_gui.drawPiece(selectedPiece)

                # Deactivate all squares for next round
                for sq in self.board_gui.getActiveSquares():
                    sq.deactivate()
                
                # Change team turns
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

                print("resetting choice2")
                choice = []

        # If the quit button is clicked, quit the program
        while True:
           pt = self.board_gui.allClicks()
           if str(pt) != ("quit","quit"):
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

