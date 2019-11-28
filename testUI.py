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
import MonteCarlito1
import MonteCarlito2
import MonteCarlito3
import MonteCarlito4
import MonteCarlito5
import Random

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

def allPlayers(heuristics):
    for black in heuristics:
        for white in heuristics:
            board = UI.createBoard(10)

            player1 = myPlayer.myPlayer(heuristics[black][0], 5)
            player2 = myPlayer.myPlayer(heuristics[white][0], 5)

            players = UI.assignColors(board, player1, player2)

            t = UI.play(board, players, withUI)

            res = UI.printWinner(board, t)

            if res == 0:
                heuristics[white][1].append(black)
                heuristics[white][2] += 1
                heuristics[black][3] += 1
            elif res == 1:
                heuristics[black][1].append(white)
                heuristics[black][2] += 1
                heuristics[white][3] += 1
            else:
                heuristics[white][1].append("Deuce " + str(black))
                heuristics[black][1].append("Deuce " + str(white))
                heuristics[black][4] += 1
                heuristics[white][4] += 1

    for key in heuristics:
        print("------------------")
        print(str(key) + " a battu " + str(heuristics[key][1]))
        print(str(key) + " a gagné " + str(heuristics[key][2]))
        print(str(key) + " a perdu " + str(heuristics[key][3]))
        print(str(key) + " a ni gagné ni perdu " + str(heuristics[key][4]))
        print("")

heuristics = {
    'Colors' : [ColorsCounting.heuristic, [], 0, 0, 0],
    'Columns' : [ColumnsLinesCounting.heuristic, [], 0, 0, 0],
    'Corners' : [CornersCounting.heuristic, [], 0, 0, 0],
    'Monte' : [MonteCarlo.heuristic, [], 0, 0, 0],
    'Move' : [MoveCounting.heuristic, [], 0, 0, 0],
    'Carlito1' : [MonteCarlito1.heuristic, [], 0, 0, 0],
    'Carlito2' : [MonteCarlito2.heuristic, [], 0, 0, 0],
    'Carlito3' : [MonteCarlito3.heuristic, [], 0, 0, 0],
    'Carlito4' : [MonteCarlito4.heuristic, [], 0, 0, 0],
    'Carlito5' : [MonteCarlito5.heuristic, [], 0, 0, 0],
    'Random' : [Random.heuristic, [], 0, 0, 0]
}

UI.initUI(withUI)

# board = createBoard(10)
# player = myPlayer.myPlayer(CornersCounting.heuristic, 0)
# print(player.heuristicMethod(board, []))
allPlayers(heuristics)
