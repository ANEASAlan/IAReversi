import Reversi
import time
from io import StringIO
import pygame
import sys
import random

withUI = False

argv = sys.argv
if len(argv) > 1 and argv[1] == "UI" :
    withUI = True

sys.path.insert(1, 'Heuristics/Easy')
sys.path.insert(1, 'Heuristics/Medium')
sys.path.insert(1, 'Heuristics/Hard')

sys.path.insert(1, 'Player')

sys.path.insert(1, 'UI')

import UI

# Les joueurs
import myPlayer
import randomPlayer
import myPlayerAlix
import myPlayerTitouan

# Nos heuristiques
# Easy
import CornersCounting
import ColorsCounting
import MoveCounting
import ColumnsLinesCounting

# Medium
import MonteCarlo

# Hard

# REAME :
#-pour lancer les tests : python3 testUI.py
#-pour activer l'interface graphique : python3 testUI.py UI

def nbLegalMoves(board, move):
    pass
    # # To parse the board you want to do a double for loop
    # # Best case would be to do it all in a unique loop but that's
    # # difficult
    #
    # # The board is a square
    # size = board.get_board_size()
    #
    # player = board._nextPlayer
    #
    # moveCount = 0
    # points = 0
    # colors = 0
    # nbWhite = 0
    # nbBlack = 0
    # cornerCount = 0
    # streak = 0
    #
    # moveCount = MoveCounting.heuristic(board, move)
    #
    # board = board._board
    # # points = countPointsPerPos(board, move[1], move[2])
    #
    # for x in range(size):
    #     tmp = [0, 0]
    #     for y in range(size):
    #         colors += colorCounting(board, size, x, y)
    #         points += countPointsPerPos(board, x, y)
    #         if isBlack(board, x, y):
    #             nbBlack += 1
    #         if isWhite(board, x, y):
    #             nbWhite += 1
    #
    # if nbBlack == 0:
    #     return 10000
    # if nbWhite == 0:
    #     return -10000
    #
    # cornerCount += cornerCountingMethod(board, size, 0, 0)
    # cornerCount += cornerCountingMethod(board, size, 0, size - 1)
    # cornerCount += cornerCountingMethod(board, size, size - 1, 0)
    # cornerCount += cornerCountingMethod(board, size, size - 1, size - 1)
    #
    # totalNbPieces = nbBlack + nbWhite
    # colors = nbWhite - nbBlack
    #
    # # if isCorner(size, move[1], move[2]):
    # #     if move[0] == 1:
    # #         corner = 100 + 900 * totalNbPieces // 85
    # #     else:
    # #         corner = -100 - 900 * totalNbPieces // 85
    #
    # moveCountWeight = moveCount  * (1.5 - totalNbPieces / 100.0) ** 10
    # colorsWeight = colors * (0.05 + totalNbPieces / 100.0) ** 20
    # pointsWeight = points * (3.0 - totalNbPieces / 100.0) ** 4
    # cornerWeight = cornerCount * (2.0 - totalNbPieces / 100.0) ** 5
    # # print(cornerWeight)
    #
    # return moveCountWeight + pointsWeight + cornerWeight + colorsWeight


count = {
    'Black' : 0,
    'White' : 0
}

UI.initUI(withUI)

# board = createBoard(10)
# player = myPlayer.myPlayer(CornersCounting.heuristic, 0)
# print(player.heuristicMethod(board, []))

for i in range(1000):
    board = UI.createBoard(10)

    player1 = myPlayer.myPlayer(CornersCounting.heuristic, 5)  # myPlayerAlix.myPlayer()
    player2 = myPlayer.myPlayer(MonteCarlo.heuristic, 5)

    players = UI.assignColors(board, player1, player2)

    t = UI.play(board, players, withUI)

    res = UI.printWinner(board, t)

    UI.addPoints(count, res)

print(count)
