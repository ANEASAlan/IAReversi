import Reversi
import myPlayerCorners
import randomPlayer
import time
from io import StringIO
import sys
import random

def createBoard(size):
    return Reversi.Board(size)

def assignColors():
    players = []

    player1 = myPlayerCorners.myPlayerCorners()
    player2 = randomPlayer.randomPlayer()

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

count = {
    'Corners' : 0,
    'Random' : 0
}

for i in range(10):
    board = createBoard(10)
    players = assignColors()

    t = play(board, players)

    res = printWinner(board, t)

    addPoints(count, res)

print(count)
