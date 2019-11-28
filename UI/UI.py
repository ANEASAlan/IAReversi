import Reversi
import time
from io import StringIO
import pygame
import sys
import random

screen = None
cW = None
cB = None
cE = None

## Update the board
def update(b):
    for posX in range(10):
        for posY in range(10):
            if b._board[posX][posY] == b._BLACK:
                screen.blit(cB,(posX*32,posY*32))
            elif b._board[posX][posY] == b._WHITE:
                screen.blit(cW,(posX*32,posY*32))
            else :
                screen.blit(cE,(posX*32,posY*32))
    pygame.display.flip()

def initUI(withUI):

    global screen, cW, cB, cE
    if withUI:
        ## Initialize pygame
        pygame.init()

        ## Set screen
        screen = pygame.display.set_mode((320,320))

        ## Set Refresh
        clock = pygame.time.Clock()
        FPS = 60
        clock.tick(FPS)

        ## Load image
        cW = pygame.image.load("Images/White.png")
        cB = pygame.image.load("Images/Black.png")
        cE = pygame.image.load("Images/Empty.png")


def createBoard(size):
    return Reversi.Board(size)

def assignColors(board, player1, player2):
    players = []

    player1.newGame(board._BLACK)
    player2.newGame(board._WHITE)

    players.append(player1)
    players.append(player2)

    return players

def printWinner(board, totalTime):

    # # print("The game is over")
    # # print(board)

    (nbwhites, nbblacks) = board.get_nb_pieces()
    # # print("Time:", totalTime)
    # # print("Winner: ", end="")

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
        count['Black'] += 1

    elif res == 0:
        count['White'] += 1

def play(board, players, withUI):
    totalTime = [0,0] # total real time for each player
    nextplayer = 0
    nextplayercolor = board._BLACK
    nbmoves = 1

    outputs = ["",""]
    sysstdout= sys.stdout
    stringio = StringIO()

    # # print(b.legal_moves())
    while not board.is_game_over():

        # # print("Referee Board:")
        # # print(board)
        # # print("Before move", nbmoves)
        # # print("Legal Moves: ", b.legal_moves())

        nbmoves += 1
        otherplayer = (nextplayer + 1) % 2
        othercolor = board._BLACK if nextplayercolor == board._WHITE else board._WHITE

        currentTime = time.time()
        sys.stdout = stringio
        move = players[nextplayer].getPlayerMove()
        sys.stdout = sysstdout
        playeroutput = "\r" + stringio.getvalue()
        stringio.truncate(0)

        # # print(("[Player "+str(nextplayer) + "] ").join(playeroutput.splitlines(True)))
        outputs[nextplayer] += playeroutput
        totalTime[nextplayer] += time.time() - currentTime
        # # print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
        (x,y) = move

        if not board.is_valid_move(nextplayercolor,x,y):
            # print(otherplayer, nextplayer, nextplayercolor)
            # print("Problem: illegal move")
            break

        board.push([nextplayercolor, x, y])

        if withUI :
            update(board)

        players[otherplayer].playOpponentMove(x,y)

        nextplayer = otherplayer
        nextplayercolor = othercolor

        # # print(board)

    return totalTime
