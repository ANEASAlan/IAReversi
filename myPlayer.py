# -*- coding: utf-8 -*-

#notre joueur, à implémenter en modifiant getPlayerMove()

import time
import Reversi
from random import randint
from playerInterface import *
from enum import Enum

class Flag(Enum):
    VALUE = 1
    LOW = 2
    UP = 3

class NodeValue():

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.flag = Flag.VALUE
        self.startingDepth = 0

class myPlayer(PlayerInterface):

    def __init__(self, heuristicMethod, maxTime): # penser à enelever les arguments (sauf self)
        self._board = Reversi.Board(10)
        self._mycolor = None
        self.minInt = - 2 ** 64
        self.maxInt = - self.minInt
        self.heuristicMethod = heuristicMethod
        self.memory = {}
        self.table = []
        self.time = 0
        self.maxTime = maxTime

    # Returns your player name, as to be displayed during the game
    def getPlayerName(self):
        return "ANEAS DE CASTRO PINTO"

    def reverseColor(self, color):
        if color == self._board._BLACK:
            return self._board._WHITE
        return self._board._BLACK

    def generateBaseHash(self):
        size = self._board.get_board_size()
        board = self._board._board
        area = size * size

        for i in range(area):
            tmp = []
            for j in range(3):
                tmp.append(randint(0, self.maxInt - 1))
            self.table.append(tmp)

    def computeHash(self):
        hash = 0
        size = self._board.get_board_size()
        board = self._board._board

        for x in range(size):
            for y in range(size):
                if board[x][y] != 0:
                    piece = board[x][y]
                    hash = hash ^ self.table[x * size + y][piece]
        return hash

    # Neg alpha beta

    def negAlphaBeta(self, depth, alpha, beta, color=None):

        if color == None:
            color = self._mycolor

        # Si le jeu est terminé, on renvoie la valeur de l'heuristique
        # On va aussi utiliser une profondeur d'arrêt
        if depth == 0 or self._board.is_game_over():
            # # print("Reached the end!")
            if color == self._mycolor:
                return (None, self.heuristicMethod(self._board))
            else:
                return (None, - self.heuristicMethod(self._board))

        # Le coup a retourné, celui à jouer
        moveToPlay = None
        maxVal = self.minInt

        # On parcourt la liste des coups valides
        for move in self._board.legal_moves():

            # On joue le premier coup valide
            self._board.push(move)

            # Recursivité pour parcourir l'arbre
            # On diminue la profondeur de un afin d'être sûr de s'arrêter
            (_, val) = self.negAlphaBeta(depth - 1, -beta, -alpha, self.reverseColor(color))

            # On retire le coup que nous venos de jouer
            self._board.pop()

            maxVal = max(-val, maxVal)

            # Si la valeur récupéré est meilleure que notre pire coup
            if maxVal > alpha:
                moveToPlay = move
                alpha = maxVal

                # Si le pire coup est meilleur que tout meilleur coup (élagage)
                if alpha >= beta:
                    return (moveToPlay, alpha)

        return (moveToPlay, alpha)

    # Neg alpha beta with memory!

    def negAlphaBetaWithMemory(self, depth, alpha, beta, color=None, hash=None, playedMove=None):
        elapsedTime = time.time() - self.time

        if elapsedTime >= self.maxTime:
            print(elapsedTime)
            if color == self._mycolor:
                return (None, self.heuristicMethod(self._board, playedMove))
            else:
                return (None, - self.heuristicMethod(self._board, playedMove))

        alphaOrig = alpha

        if self.table == []:
            self.generateBaseHash()

        if hash == None:
            hash = self.computeHash()

        if color == None:
            color = self._mycolor

        if hash in self.memory:
            nodeVal = self.memory[hash]
            if nodeVal.depth >= depth:

                if self.startingDepth != depth and nodeVal.flag == Flag.VALUE:
                    return (None, nodeVal.value)

                elif nodeVal.flag == Flag.LOW:
                    alpha = max(alpha, nodeVal.value)

                else:
                    beta = min(beta, nodeVal.value)

                if self.startingDepth != depth and alpha >= beta:
                    return (None, nodeVal.value)


        # Si le jeu est terminé, on renvoie la valeur de l'heuristique
        # On va aussi utiliser une profondeur d'arrêt
        if depth == 0 or self._board.is_game_over():
            # # print("Reached the end!")
            if color == self._mycolor:
                return (None, self.heuristicMethod(self._board, playedMove))
            else:
                return (None, - self.heuristicMethod(self._board, playedMove))

        # Le coup a retourné, celui à jouer
        moveToPlay = None
        maxVal = self.minInt

        # On parcourt la liste des coups valides
        for move in self._board.legal_moves():

            # On joue le premier coup valide
            self._board.push(move)
            tmpHash = hash ^ (self.table[move[1] * self._board.get_board_size() + move[2]][move[0]])
            playedMove = move

            # Recursivité pour parcourir l'arbre
            # On diminue la profondeur de un afin d'être sûr de s'arrêter
            (_, val) = self.negAlphaBetaWithMemory(depth - 1, -beta, -alpha, self.reverseColor(color), tmpHash, playedMove)

            # On retire le coup que nous venos de jouer
            self._board.pop()

            maxVal = max(-val, maxVal)

            # Si la valeur récupéré est meilleure que notre pire coup
            if maxVal > alpha:
                moveToPlay = move
                alpha = maxVal

                # Si le pire coup est meilleur que tout meilleur coup (élagage)
                if alpha >= beta:
                    break

            elapsedTime = time.time() - self.time
            if elapsedTime >= self.maxTime:
                break

        nodeVal = NodeValue(maxVal, depth)
        if maxVal <= alphaOrig:
            nodeVal.flag = Flag.UP
        elif maxVal >= beta:
            nodeVal.flag = Flag.LOW
        else:
            nodeVal.flag = Flag.VALUE

        self.memory[hash] = nodeVal
        return (moveToPlay, maxVal)

    # La fonction heuristique, après quelques recherches :

    # Un palet placé dans un coin vaut des points car il ne peut pas être pris
    # Un palet juste à côté d'un coin est très mauvais car ilest garanti d'être
    # pris

    # Un palet dans un coin vaut plus de points en début qu'en fin de partie

    # Moins l'adversaire a de possibilité de mouvement après le coup plus ce
    # coup est intéressant

    # Plus le palet joué est entouré d'autres palets mieux c'est

    # On peut mettre un poids sur chaque palet placé. Ce poids dépend des idées
    # au-dessus (autre idée)

    # Returns your move. The move must be a couple of two integers,
    # Which are the coordinates of where you want to put your piece
    # on the board. Coordinates are the coordinates given by the Reversy.py
    # methods (e.g. validMove(board, x, y) must be true if you play '(x,y)')
    # You can also answer (-1,-1) as "pass". Note: the referee will never
    # call your function if the game is over
    def getPlayerMove(self): # à modifier
        if self._board.is_game_over(): # si game_over
            # print("Referee told me to play but the game is over!")
            return (-1,-1) #(-1,-1) veut dire "je passe mon tour", si on est deux à passer notre tour, la partie est terminée

        # (move, _) = self.negAlphaBeta(3, self.minInt, self.maxInt)
        moveToPlay = None
        self.time = time.time()
        if randint(0, 100) == 0:
            self.memory = {}
        for i in range(1, 5):
            self.startingDepth = i
            (move, heur1) = self.negAlphaBetaWithMemory(i, self.minInt, self.maxInt)
            # print(move)
            # print(heur1)
            if move != None:
                moveToPlay = move
            elapsedTime = time.time() - self.time
            if elapsedTime >= self.maxTime:
                break
        # print("Move played :")
        # print(moveToPlay)
        # print("------------")
        # (move2, heur2) = self.negAlphaBeta(4, self.minInt, self.maxInt)

        # print("Result = " + str(move) + " / " + str(heur1))
        # print("Expected = " + str(move2) + " / " + str(heur2))

        self._board.push(moveToPlay) #joue le coup choisi dans move

        # print("I am playing ", move)

        (c,x,y) = moveToPlay #la case sur laquelle jouer le coup move, (couleur, abscisse, ordonnée)

        assert(c==self._mycolor) #si pas la bonne couleur, problème

        # print("My current board :")

        # print(self._board)

        return (x,y) #renvoyer le coup à jouer

    # Inform you that the oponent has played this move. You must play it
    # with no search (just update your local variables to take it into account)
    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        # # print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])

    # Starts a new game, and give you your color.
    # As defined in Reversi.py : color=1 for BLACK, and color=2 for WHITE
    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    # You can get a feedback on the winner
    # This function gives you the color of the winner
    def endGame(self, winner):
        if self._mycolor == winner:
            pass
            # print("I won!!!")
        else:
            pass
            # print("I lost :(!!")
