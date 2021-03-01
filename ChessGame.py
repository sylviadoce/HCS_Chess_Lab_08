# Sylvia Chin
# HCS Lab 08 - Chess
#
# This is the ChessGame module that runs the game as a class, using the
# BoardGUI and Piece Classes (and subclasses).
#
from Piece import *
from SylviaPieceSubclasses import *
from BishopKingQueen_Sahil import *
from BoardGUI import *

class ChessGame:
    def __init__(self):
        """Initializes the class that runs the game, including
            variables to get other modules, a list of pieces,
            a checkmate boolean, and a list of the board squares."""
        self.board_gui = BoardGUI("white")

        # Create a list of two lists storing all pieces
        self.pieces = [[],[]]

        self.checkmate = False

        # Store the list of all squares
        self.squares = self.board_gui.getSquares()

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
        """Returns a list of all created pieces, divided into list items
            by their team color and drawn to the board."""
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

    def pawnToQueen(self,team,sq) -> bool:
        """Replaces a pawn with a queen once at the end of the board."""
        for piece in team:
            if piece.getPieceType() == "pawn":
                x,y = piece.getLocationXY()
                if piece.checkColor() == "white":
                    if y == 7.5:
                        self.removePiece(piece)
                        self.addPiece(Queen(Point(x,y),"white","queen","wq"))
                        sq.resetOccupiedSquare()
                        return True
                else:
                    if y == 0.5:
                        self.removePiece(piece)
                        self.addPiece(Queen(Point(x,y),"black","queen","bq"))
                        sq.resetOccupiedSquare()
                        return True
        return False

    def getEnemyTeam(self):
        """Returns a list of the current enemy team."""
        if self.board_gui.checkTurnColor() == "white":
            self.enemyPieces = self.pieces[1]
        else:
            self.enemyPieces = self.pieces[0]

        return self.enemyPieces

    def getMyTeam(self):
        """Returns a list of the current team."""
        if self.board_gui.checkTurnColor() == "white":
            self.sameTeam = self.pieces[0]
        else:
            self.sameTeam = self.pieces[1]

        return self.sameTeam

    def removePiece(self,piece):
        """Removes a piece from its team's list."""
        if piece.checkColor() == "white":
            self.pieces[0].remove(piece)
        else:
            self.pieces[1].remove(piece)

    def addPiece(self,piece):
        """Adds a piece to its color's team's list."""
        if piece.checkColor() == "white":
            self.pieces[0].append(piece)
        else:
            self.pieces[1].append(piece)
            
    def getEnemyKing(self) -> list:
        """Returns the current enemy king."""
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
        """Returns the current king."""
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

    def errorMessage(self,num):
        """Updates the message with the proper error."""
        if num == 1:
            self.board_gui.updateMessage(
                "Please click on a \n" +
                self.board_gui.checkTurnColor().capitalize() + " piece!")
        elif num == 2:
            self.board_gui.updateMessage("Please select a move \n"
                                         "from the indicated \n"
                                         "options.")
        elif num == 3:
            self.board_gui.updateMessage("That is not a \n"
                                         "valid move.\n\n"
                                         "Please try again.")
        else:
            self.board_gui.updateMessage("That piece does not \n"
                                         "have any legal moves -- \n\n"
                                         "please pick another piece.")

    def nextTurn(self):
        """Prepares for the next team's turn by deactivating
            all squares and changing the team's turn."""
        # Deactivate all squares for next round
        for sq in self.board_gui.getActiveSquares():
            sq.deactivate()

        # Change team turns, display the correct after-move message
        self.board_gui.updateTurn()

    def resetTurn(self):
        """User did not click on a valid move, so reset the turn."""
        # Deactivate all squares for next round
        for sq in self.board_gui.getActiveSquares():
            sq.deactivate()

    def afterMoveMessage(self,p,captured):
        """Updates the message with the proper after-move message,
            determined whether it there is checkmate, check, a
            captured piece, or just a move."""
        if p.getOppCheckMate():
            message = (p.checkColor().capitalize() + " moved \n" +
            p.getPieceType() + " to " +
            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
            "-- \n\n Checkmate!")
        elif p.getOppCheck():
            message = (p.checkColor().capitalize() + " moved \n"
            + p.getPieceType() + " to " +
            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
            " (Check) -- \n\n It is now \n" +
            self.board_gui.checkTurnColor().capitalize() + "'s move.")
        elif captured != "":
            message = (p.checkColor().capitalize() + "'s "
            + p.getPieceType() + " captured \n" +
            self.board_gui.checkTurnColor().capitalize() + "'s " +
            captured.getPieceType() + " at " +
            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
            " -- \n\n It is now \n" +
            self.board_gui.checkTurnColor().capitalize() + "'s move.")
        else:
            message = (p.checkColor().capitalize() + " moved \n"
            + p.getPieceType() + " to " +
            self.board_gui.locationCoordToLabel(p.getLocationXY()) +
            " -- \n\n It is now \n" +
            self.board_gui.checkTurnColor().capitalize() + "'s move.")

        self.board_gui.updateMessage(message)

    def checkQuit(self):
        """Quits the program if the quit button is clicked."""
        # Always expect a quit button click
        while True:
           pt = self.board_gui.allClicks()
           if str(pt) != ("quit","quit"):
                self.board_gui.closeGame()

    def main(self):
        """Runs the game: carries out actions according to user clicks
            and checks the validity of actions."""
        # Create the pieces and a list to store the chosen piece and square
        pieces = self.createPieces()
        choice = []
        # Loop while the game is not ended (no king in checkmate)
        while not self.checkmate:
            # Expect a click in the graphics window
            click = self.board_gui.allClicks()
            # If the click is not on a square, loop
            if click[1] != "square":
                continue 
            # False (choosing a piece) or True (placing a valid piece)
            clicktwo = False
            for sq in self.squares:
                if sq.checkActive():
                    clicktwo = True
                    break
            if not clicktwo:
                for lstPiece in pieces:
                    for p in lstPiece:
                        invalid = False
                        # Check if a piece is on the square
                        if (click[0].getLocation() == p.getLocationXY()):
                            # If wrong team, update message
                            if (p.checkColor() !=
                                self.board_gui.checkTurnColor()):
                                self.errorMessage(1)
                                invalid = True
                                break
                            # If right team, get possible moves
                            else:
                                spots = p.getPossibleMoves(
                                    self.getMyKing(),
                                    self.getEnemyKing(),
                                    self.getMyTeam(),
                                    self.getEnemyTeam(),"y")
                                selectedPiece = p
                                # Check if the piece has possible spots
                                if spots != []:
                                    self.errorMessage(2)
                                    # Activate possible spots
                                    for spot in spots:
                                        for sq in self.squares:
                                            x,y = spot.getX(),spot.getY()
                                            if (x == sq.getLocation()[0]
                                                and
                                                y == sq.getLocation()[1]):
                                                sq.activate()
                                    # Choice stores the valid piece, square
                                    choice.append(p)
                                    choice.append(click[0])
                                    invalid = True
                                    break
                                else:
                                    self.errorMessage(4)
                                    invalid = True
                                    break
                        else:
                            self.errorMessage(1)
                    if invalid:
                        break
            if clicktwo:
                if click[0].checkActive():
                    # Move the piece to the clicked square
                    x,y = selectedPiece.getLocationXY()
                    enemyPieces = selectedPiece.movePiece(
                        click[0].getLocation(),self.getEnemyTeam())
                    captured = ""
                    # Check if a piece was eaten, save it to a variable
                    for piece in enemyPieces:
                        if piece.getEaten():
                            captured = piece
                            # Reset the captured piece's square
                            for sq in self.squares:
                                sqx,sqy = (sq.getLocation()[0],
                                           sq.getLocation()[1])
                                x,y = selectedPiece.getLocationXY()
                                if sqx == x and sqy == y:
                                    sq.resetOccupiedSquare()
                            # Remove captured piece from the pieces list
                            self.removePiece(piece)
                    # Check if a pawn needs to be converted to a queen
                    newQueen = self.pawnToQueen(self.getMyTeam(),click[0])
                    if newQueen:
                        selectedPiece = self.getMyTeam()[-1]
                    # Reset og square, redraw piece, turn, choice, message
                    choice[1].resetOccupiedSquare()
                    self.board_gui.drawPiece(selectedPiece)
                    self.nextTurn()
                    choice = []
                    self.afterMoveMessage(selectedPiece,captured)
                else:
                    self.errorMessage(3)
                    self.resetTurn()
                    choice = []
                    continue
                self.checkmate = selectedPiece.getOppCheckMate()
        # Quit the program if the quit button is clicked
        self.checkQuit()

# Call the main function using the ChessGame Class
ChessGame().main()
