# -*- coding: utf-8 -*-

#notre joueur, à implémenter en modifiant getPlayerMove()

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    # Returns your player name, as to be displayed during the game
    def getPlayerName(self):
        return "ANEAS DE CASTRO PINTO"

    def MiniMax():
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return Reversi.heuristique(self, self._mycolor)
        moves = [m for m in self._board.legal_moves()]
# à modifier, pour garder le move à faire et le renvoyer, genre si on est revenu à la racine de la récursion on regarde quel est le move avec le plus gros node_val et on renvoie cette valeur
        node_val = None
        for a_move in self._board.legal_moves()]:
            self._board.push(a_move)
            if node_val == None:
                node_val = MiniMax()
            elif Reversi._nextPlayer == self._mycolor:
                node_val = max(node_val,MiniMax())
            else:
                node_val = min(node_val,MiniMax())
            self._board.pop()
        return node_val
# ne plus modifier

    def MiniMaxWithHeuristique():
        

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
        moves = [m for m in self._board.legal_moves()] #liste des coups à pouvoir être joués
# à modifier
        #move = moves[randint(0,len(moves)-1)] #prend aléatoirement un coup à faire
# ne plus modifier
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
        print("Opponent played ", (x,y))
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



