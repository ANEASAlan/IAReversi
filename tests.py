import Reversi
import myPlayer
import randomPlayer
import time
from io import StringIO
import sys
import random

def createBoard(size):
    return Reversi.Board(size)

def assignColors(player1, player2):
    players = []

    player1.newGame(board._BLACK)
    player2.newGame(board._WHITE)

    players.append(player1)
    players.append(player2)

    return players

def printWinner(board, totalTime):

    # print("The game is over")
    # print(board)

    (nbwhites, nbblacks) = board.get_nb_pieces()
    # print("Time:", totalTime)
    # print("Winner: ", end="")

    if nbwhites > nbblacks:
        print("WHITE")
        return 0
    elif nbblacks > nbwhites:
        print("BLACK")
        return 1
    else:
        print("DEUCE")
    return -1

def addPoints(count, res):

    if res == 1:
        count['Corners'] += 1

    elif res == 0:
        count['Random'] += 1

def play(board, players):
    totalTime = [0,0] # total real time for each player
    nextplayer = 0
    nextplayercolor = board._BLACK
    nbmoves = 1

    outputs = ["",""]
    sysstdout= sys.stdout
    stringio = StringIO()

    # print(b.legal_moves())
    while not board.is_game_over():

        # print("Referee Board:")
        # print(board)
        # print("Before move", nbmoves)
        # print("Legal Moves: ", b.legal_moves())

        nbmoves += 1
        otherplayer = (nextplayer + 1) % 2
        othercolor = board._BLACK if nextplayercolor == board._WHITE else board._WHITE

        currentTime = time.time()
        sys.stdout = stringio
        move = players[nextplayer].getPlayerMove()
        sys.stdout = sysstdout
        playeroutput = "\r" + stringio.getvalue()
        stringio.truncate(0)

        # print(("[Player "+str(nextplayer) + "] ").join(playeroutput.splitlines(True)))
        outputs[nextplayer] += playeroutput
        totalTime[nextplayer] += time.time() - currentTime
        # print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
        (x,y) = move

        if not board.is_valid_move(nextplayercolor,x,y):
            print(otherplayer, nextplayer, nextplayercolor)
            print("Problem: illegal move")
            break

        board.push([nextplayercolor, x, y])
        players[otherplayer].playOpponentMove(x,y)

        nextplayer = otherplayer
        nextplayercolor = othercolor

        # print(board)

    return totalTime

################################################################################
#################################### HEURISTICS ################################
################################################################################

def countingCorners(board):
    # To parse the board you want to do a double for loop
    # Best case would be to do it all in a unique loop but that's
    # difficult

    # The board is a square
    size = board.get_board_size()

    # The board to use, to avoid multiple dots
    board = board._board

    # This stores the number of disks in the corners
    # A white one is worth 3 and a black one is worth -3
    # The count is negative if this is the foe's turn (*** TO DO ***)
    # So far, the state of the game doesn't matter, it should (** TO DO **)
    cornerCount = 0
    cornerCount += cornerCountingMethod(board, size, 0, 0)
    cornerCount += cornerCountingMethod(board, size, 0, size - 1)
    cornerCount += cornerCountingMethod(board, size, size - 1, 0)
    cornerCount += cornerCountingMethod(board, size, size - 1, size - 1)
    return cornerCount

################################################################################
######################## Utility functions #####################################
################################################################################

# Cette fonction teste si une position est dans le coin de la table
def isCorner(size, x, y):

    # Coin supérieur gauche
    if x == 0 and y == 0:
        return True

    # Coin supérieur droit
    if x == size - 1 and y == 0:
        return True

    # Coin inférieur gauche
    if x == 0 and y == size - 1:
        return True

    # Coin inférieur droit
    if x == size - 1 and y == size -1:
        return True

    return False

# Une fonction pour rendre le code plus lisible permettant de savoir si un
# palet est blanc
def isWhite(board, x, y):
    if board[x][y] == 1:
        return True
    return False

# Une fonction pour rendre le code plus lisible permettant de savoir si un
# palet est noir
def isBlack(board, x, y):
    if board[x][y] == 2:
        return True
    return False

# Cette fonction est aussi là pour rendre le code plus lisible
# Elle renvoie 3 si le palet en (x, y) est blanc, -3 si il est noir, 0 sinon
def cornerCountingMethod(board, size, x, y):

    if isCorner(size, x, y):

        if isWhite(board, x, y):
            return 3

        if isBlack(board, x, y):
            return -3

    return 0

################################################################################
######################################## CODE ##################################
################################################################################

count = {
    'Corners' : 0,
    'Random' : 0
}

for i in range(10):
    board = createBoard(10)

    player1 = myPlayer.myPlayer(countingCorners)
    player2 = randomPlayer.randomPlayer()

    players = assignColors(player1, player2)
    players[0]

    t = play(board, players)

    res = printWinner(board, t)

    addPoints(count, res)

print(count)