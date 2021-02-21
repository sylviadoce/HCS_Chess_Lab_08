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


    def createPawns(self) -> list:
        """Creates all white, black pawns in their standard locations."""
        # Stores a list of two lists, pawns in each color (white first)
        pawns = [[],[]]
        
        # Initialize the white (bottom-left) pawn coordinates (a2), create
        x,y = 0.5,1.5
        for i in range(8):
            pawns[0].append(Pawn(Point(x,y),"white","pawn"))
            x += 1

        # Initialize the black (top-left) pawn coordinates (a7), create
        x,y = 0.5,6.5
        for i in range(8):
            pawns[1].append(Pawn(Point(x,y),"black","pawn"))
            x += 1

        return pawns
        
    def createBishops(self) -> list:
        """Creates all white, black bishops in their standard locations."""
        # Stores a list of two lists, bishops in each color (white first)
        bishops = [[],[]]

        # Initialize the white bishop coordinates (c1 and f1), create
        bishops[0].append(Bishop(Point(2.5,0.5),"white","bishop"))
        bishops[0].append(Bishop(Point(5.5,0.5),"white","bishop"))

        # Initialize the black bishop coordinates (c8 and f8), create
        bishops[1].append(Bishop(Point(2.5,7.5),"black","bishop"))
        bishops[1].append(Bishop(Point(5.5,7.5),"black","bishop"))

        return bishops

    def createKnights(self) -> list:
        """Creates all white, black knights in their standard locations."""
        # Stores a list of two lists, knights in each color (white first)
        knights = [[],[]]

        # Initialize the white knight coordinates (b1 and g1), create
        knights[0].append(Knight(Point(1.5,0.5),"white","knight"))
        knights[0].append(Knight(Point(6.5,0.5),"white","knight"))

        # Initialize the black knight coordinates (b8 and g8), create
        knights[1].append(Knight(Point(1.5,7.5),"black","knight"))
        knights[1].append(Knight(Point(6.5,7.5),"black","knight"))

        return knights

    def createRooks(self) -> list:
        """Creates all white, black rooks in their standard locations."""
        # Stores a list of two lists, rooks in each color (white first)
        rooks = [[],[]]

        # Initialize the white rook coordinates (a1 and h1), create
        rooks[0].append(Rook(Point(0.5,0.5),"white","rook"))
        rooks[0].append(Rook(Point(7.5,0.5),"white","rook"))

        # Initialize the black rook coordinates (a8 and h8), create
        rooks[1].append(Rook(Point(0.5,7.5),"black","rook"))
        rooks[1].append(Rook(Point(7.5,7.5),"black","rook"))

        return rooks

    def createQueens(self) -> list:
        """Creates all white, black queens in their standard locations."""
        # Stores a list of two lists, queens in each color (white first)
        queens = [[],[]]

        # Initialize the white queen coordinates (d1), create
        queens[0].append(Queen(Point(3.5,0.5),"white","queen"))

        # Initialize the black queen coordinates (d8), create
        queens[1].append(Queen(Point(3.5,7.5),"black","queen"))

        return queens

    def createKings(self) -> list:
        """Creates all white, black kings in their standard locations."""
        # Stores a list of two lists, kings in each color (white first)
        kings = [[],[]]

        # Initialize the white king coordinates (e1), create
        kings[0].append(King(Point(4.5,0.5),"white","king"))

        # Initialize the black king coordinates (e8), create
        kings[1].append(King(Point(4.5,7.5),"black","king"))

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

    def main(self):
        """Runs the game, using functions to move the pieces."""

        # Create the pieces
        pieces = self.createPieces()

        # Set up a list and counter to track clicked squares
        clicked_sqs = []
        clicked_sq = 0

        # Set up a list to store the authentic click (choosing a piece)
        choice = []

        # Loop while the game is not ended (no king in checkmate)
        while not self.checkmate:
            click = self.board_gui.allClicks()
            if click[1] == "square":
                # Check if another square has already been clicked
                # Check if the square is empty
                # Check if it is choosing or placing a piece

                # Check if another square has already been clicked
                for square in self.board_gui.squares:
                    if square.checkClicked():
                        clicked_sq += 1
                        clicked_sqs.append(square)
                        
                # If choosing a piece (one square click)
                if clicked_sq == 1:
                    for piece in pieces:
                        for p in piece:
                            # Check if the square is empty
                            if (clicked_sqs[0].getLocation()
                                != p.getLocation()):
                                self.board_gui.updateMessage(
                                    "Please click on \n a",
                                    self.board_gui.checkTurnColor(),
                                    "piece!")
                                clicked_sqs[0].resetClicked()
                                clicked_sqs.pop(0)
                            # Check if it is the right team's piece 
                            else:
                                # If wrong team, update message
                                if (p.checkColor() !=
                                    self.board_gui.checkTurnColor()):
                                    self.board_gui.updateMessage(
                                        "Please click on \n a",
                                        self.board_gui.checkTurnColor(),
                                        "piece!")
                                    clicked_sqs[0].resetClicked()
                                    clicked_sqs.pop(0)
                                # If right team, get possible moves
                                else:
                                    # Check if the piece has possible spots
                                    if p.getPossibleMoves("params") != []:
                                        self.board_gui.updateMessage(
                                            "Please select a move \n",
                                            "from the indicated \n",
                                            "options")
                                        # Sahil's stuff here?
                                        # Incorporate the Piece Class
                                        # Activate possible squares
                                        # this is the authentic scenario
                                        choice.append(p)
                                        print("sahil")
                                    # If not, update message
                                    else:
                                        self.board_gui.updateMessage(
                                            "That piece does not have \n",
                                            "any legal moves -- \n",
                                            "please pick another piece.")
                                        clicked_sqs[0].resetClicked()
                                        clicked_sqs.pop(0)

                # Check again if another square has already been clicked
                #   in case the first click was inauthentic
                for square in self.board_gui.squares:
                    if square.checkClicked():
                        clicked_sq += 1
                        clicked_sqs.append(square)
                
                # If placing a piece (already one authentic square click)
                if clicked_sq == 2:
                    # Check if the clicked square is occupied
                    for piece in pieces:
                        for p in piece:
                            # If occupied, check the piece's team
                            if (p.getLocation() ==
                                clicked_sq[1].getLocation()):
                                # If same team, update message
                                if (p.checkColor() ==
                                    choice[0].checkColor()):
                                    self.board_gui.updateMessage(
                                        "That is not a valid move. \n",
                                        "Please try again.")
                                    clicked_sqs[1].resetClicked()
                                    clicked_sqs.pop(1)
                                # If other team, check if it's a valid move
                                # (not putting king in check,possible move)
                                # If so, capture the piece and remove it
                                else:
                                    # Sahil's stuff here?
                                    # actually moving the piece
                                    # make sure to update message
                            # If empty, check if it's a valid move
                            # (not putting king in check,possible move)
                            else:
                                # Sahil's stuff here?
                                # actually moving the piece
                                # make sure to update message
                                
##                self.moveMethod()

        
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
