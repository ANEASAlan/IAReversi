# -*- coding: utf-8 -*-

#notre joueur, à implémenter en modifiant getPlayerMove()

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayerCorners(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None
        self.minInt = - 2 ** 64
        self.maxInt = - self.minInt

    # Returns your player name, as to be displayed during the game
    def getPlayerName(self):
        return "ANEAS DE CASTRO PINTO"

    # Neg alpha beta

    def negAlphaBeta(self, depth, alpha, beta):

        # Si le jeu est terminé, on renvoie la valeur de l'heuristique
        # On va aussi utiliser une profondeur d'arrêt
        if depth == 0 or self._board.is_game_over():
            # print("Reached the end!")
            return (None, self.heuristic())

        # Le coup a retourné, celui à jouer
        moveToPlay = None

        # On parcourt la liste des coups valides
        for move in self._board.legal_moves():

            # On joue le premier coup valide
            self._board.push(move)

            # Recursivité pour parcourir l'arbre
            # On diminue la profondeur de un afin d'être sûr de s'arrêter
            (_, val) = self.negAlphaBeta(depth - 1, -beta, -alpha)
            val = - val

            # On retire le coup que nous venos de jouer
            self._board.pop()

            # Si la valeur récupéré est meilleure que notre pire coup
            if val > alpha:
                moveToPlay = move
                alpha = val

                # Si le pire coup est meilleur que tout meilleur coup (élagage)
                if alpha > beta:
                    return (moveToPlay, alpha)

        return (moveToPlay, alpha)


        # moves = [m for m in self._board.legal_moves()]
        # # à modifier, pour garder le move à faire et le renvoyer, genre si on est revenu
        # # à la racine de la récursion on regarde quel est le move avec le plus gros node_val et on renvoie cette valeur
        # node_val = None
        # for a_move in self._board.legal_moves():
        #     self._board.push(a_move)
        #     if node_val == None:
        #         node_val = MiniMax()
        #     elif Reversi._nextPlayer == self._mycolor:
        #         node_val = max(node_val,MiniMax())
        #     else:
        #         node_val = min(node_val,MiniMax())
        #     self._board.pop()
        # return node_val
# ne plus modifier

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

    def heuristic(self):
        # To parse the board you want to do a double for loop
        # Best case would be to do it all in a unique loop but that's
        # difficult

        # The board to use, to avoid multiple dots
        board = self._board._board

        # The board is a square
        size = self._board.get_board_size()

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



    # Returns your move. The move must be a couple of two integers,
    # Which are the coordinates of where you want to put your piece
    # on the board. Coordinates are the coordinates given by the Reversy.py
    # methods (e.g. validMove(board, x, y) must be true if you play '(x,y)')
    # You can also answer (-1,-1) as "pass". Note: the referee will never
    # call your function if the game is over
    def getPlayerMove(self): # à modifier
        if self._board.is_game_over(): # si game_over
            print("Referee told me to play but the game is over!")
            return (-1,-1) #(-1,-1) veut dire "je passe mon tour", si on est deux à passer notre tour, la partie est terminée

        (move, _) = self.negAlphaBeta(4, self.minInt, self.maxInt)

        self._board.push(move) #joue le coup choisi dans move

        print("I am playing ", move)

        (c,x,y) = move #la case sur laquelle jouer le coup move, (couleur, abscisse, ordonnée)

        assert(c==self._mycolor) #si pas la bonne couleur, problème

        print("My current board :")

        print(self._board)

        return (x,y) #renvoyer le coup à jouer


# ma fonction minimax pour tic tac toe
##global_node_count = 0
##def strategie_gagnante_intelligente(b): # _X est ami, _O est ennemi
##    # utiliser is_game_over pour les feuilles, et getresult pour leurs valeurs
##    #_X veut du max
##    #legal_move pour savoir quoi jouer, push ensuite
##    #garder opti_move pour savoir quoi faire lorsqu'on remonte les valeurs
##    global global_node_count
##    global_node_count += 1
##    if b.is_game_over():
##        return getresult(b)
##    node_val = None
##    for a_move in b.legal_moves():
##        b.push(a_move)
##        if node_val == None:
##            node_val = strategie_gagnante_intelligente(b)
##        elif b._nextPlayer == b._X:
##            if node_val != 1:
##                node_val = max(node_val,strategie_gagnante_intelligente(b))
##        else:
##            if node_val != -1:
##                node_val = min(node_val,strategie_gagnante_intelligente(b))
##        b.pop()
##    return node_val



    # Inform you that the oponent has played this move. You must play it
    # with no search (just update your local variables to take it into account)
    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        # print("Opponent played ", (x,y))
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
            print("I won!!!")
        else:
            print("I lost :(!!")

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
