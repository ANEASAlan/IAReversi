
# -*- coding: utf-8 -*-

import time
import Reversi
import random
from random import randint
from playerInterface import *

class myPlayer(PlayerInterface):

    bonmouv = []

    def heuristique2(self):
        for m in self._board.legal_moves():
            if m[1] == 0 and m[2] == 0:
                return m
            if m[1] == 9 and m[2] == 9:
                return m
            if m[1] == 0 and m[2] == 9:
                return m
            if m[1] == 9 and m[2] == 0:
                return m
        return -1

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Equipe type"

    def heuristique3(self):
        for m in self._board.legal_moves():
            if m[1] == 0 and m[1] == 1:
                return -150
            if m[1] == 1 and m[2] == 0:
                return -150
            if m[1] == 8 and m[2] == 0:
                return -150
            if m[1] == 0 and m[2] == 8:
                return -150
            if m[1] == 9 and m[2] == 1:
                return -150
            if m[1] == 8 and m[2] == 9:
                return -150
            if m[1] == 1 and m[2] == 9:
                return -150
            if m[1] == 9 and m[2] == 8:
                return -150

            if m[1] == 0 and m[1] == 2:
                return 30
            if m[1] == 2 and m[2] == 0:
                return 30
            if m[1] == 7 and m[2] == 0:
                return 30
            if m[1] == 0 and m[2] == 7:
                return 30
            if m[1] == 2 and m[2] == 9:
                return 30
            if m[1] == 9 and m[2] == 2:
                return 30
            if m[1] == 7 and m[2] == 9:
                return 30
            if m[1] == 9 and m[2] == 7:
                return 30

            if m[1] == 0 and m[1] == 3:
                return 10
            if m[1] == 0 and m[2] == 4:
                return 10
            if m[1] == 0 and m[2] == 5:
                return 10
            if m[1] == 0 and m[2] == 6:
                return 10
            if m[1] == 9 and m[2] == 3:
                return 10
            if m[1] == 9 and m[2] == 4:
                return 10
            if m[1] == 9 and m[2] == 5:
                return 10
            if m[1] == 9 and m[2] == 6:
                return 10
            if m[1] == 3 and m[1] == 0:
                return 10
            if m[1] == 4 and m[2] == 0:
                return 10
            if m[1] == 5 and m[2] == 0:
                return 10
            if m[1] == 6 and m[2] == 0:
                return 10
            if m[1] == 3 and m[2] == 9:
                return 10
            if m[1] == 4 and m[2] == 9:
                return 10
            if m[1] == 5 and m[2] == 9:
                return 10
            if m[1] == 6 and m[2] == 9:
                return 10

            if m[1] == 1 and m[1] == 1:
                return -250
            if m[1] == 1 and m[2] == 8:
                return -250
            if m[1] == 8 and m[2] == 1:
                return -250
            if m[1] == 8 and m[2] == 8:
                return -250

            if m[1] == 2 and m[1] == 2:
                return 1
            if m[1] == 3 and m[2] == 2:
                return 1
            if m[1] == 4 and m[2] == 2:
                return 1
            if m[1] == 5 and m[2] == 2:
                return 1
            if m[1] == 6 and m[2] == 2:
                return 1
            if m[1] == 7 and m[2] == 2:
                return 1
            if m[1] == 2 and m[2] == 7:
                return 1
            if m[1] == 3 and m[2] == 7:
                return 1
            if m[1] == 4 and m[1] == 7:
                return 1
            if m[1] == 5 and m[2] == 7:
                return 1
            if m[1] == 6 and m[2] == 7:
                return 1
            if m[1] == 7 and m[2] == 7:
                return 1
            if m[1] == 2 and m[2] == 2:
                return 1
            if m[1] == 2 and m[2] == 3:
                return 1
            if m[1] == 2 and m[2] == 4:
                return 1
            if m[1] == 2 and m[2] == 5:
                return 1
            if m[1] == 7 and m[1] == 3:
                return 1
            if m[1] == 7 and m[2] == 4:
                return 1
            if m[1] == 7 and m[2] == 5:
                return 1
            if m[1] == 7 and m[2] == 6:
                return 1

            if m[1] == 3 and m[1] == 3:
                return 2
            if m[1] == 6 and m[2] == 3:
                return 2
            if m[1] == 3 and m[2] == 6:
                return 2
            if m[1] == 6 and m[2] == 6:
                return 2

            if m[1] == 3 and m[1] == 4:
                return 6
            if m[1] == 3 and m[2] == 5:
                return 6
            if m[1] == 4 and m[2] == 3:
                return 6
            if m[1] == 5 and m[2] == 3:
                return 6
            if m[1] == 6 and m[2] == 4:
                return 6
            if m[1] == 6 and m[2] == 5:
                return 6
            if m[1] == 4 and m[2] == 6:
                return 6
            if m[1] == 5 and m[2] == 6:
                return 6

            else :
                return 0

    def negamax(self, profondeur,color,alpha=-float('infinity'),beta=float('infinity') ):
        nbMoves = self._board._nbWHITE + self._board._nbBLACK
        #print (nbMoves)
        if  nbMoves >= 80:
            if profondeur <= 0:
                return color * self._board.heuristique()

            valeur = -float('infinity')

            for mov in self._board.legal_moves():
                #valeur = max(valeur, -self.negamax(profondeur - 1,-color,-beta,-alpha ))
                #if mov[0] == 1:
                #self.bonmouv.append(valeur)
                #self.bonmouv.append(mov)
                self._board.push(mov)
                if self._board._nextPlayer == self._board._WHITE:
                    self._board._nextPlayer = self._board._BLACK
                    valeur = max(valeur, -self.negamax(profondeur - 1, 1, -beta, -alpha))
                else:
                    self._board._nextPlayer = self._board._WHITE
                    valeur = max(valeur, self.negamax(profondeur - 1, 1, -beta, -alpha))
                self._board.pop()
                alpha = max(alpha, valeur)
                self.bonmouv.append(valeur)
                self.bonmouv.append(mov)
                if alpha >= beta:
                    break

            return valeur
        else:

            if profondeur <= 0:
                #print ("res :", (color * self.heuristique3()) + (0.5 * -self._board.heuristique()))
                return color * len(self._board.legal_moves()*2)+(color * self.heuristique3()) + (0.8 * -self._board.heuristique())

            valeur = -float('infinity')

            for mov in self._board.legal_moves():
                # valeur = max(valeur, -self.negamax(profondeur - 1,-color,-beta,-alpha ))
                # if mov[0] == 1:
                # self.bonmouv.append(valeur)
                # self.bonmouv.append(mov)
                self._board.push(mov)
                if self._board._nextPlayer == self._board._BLACK:
                    self._board._nextPlayer = self._board._WHITE
                    valeur = max(valeur, -self.negamax(profondeur - 1, 1, -beta, -alpha))
                else:
                    self._board._nextPlayer = self._board._WHITE
                    valeur = max(valeur, self.negamax(profondeur - 1, 1, -beta, -alpha))
                self._board.pop()
                alpha = max(alpha, valeur)
                self.bonmouv.append(valeur)
                self.bonmouv.append(mov)
                if alpha >= beta:
                    break

            return valeur



    def getGoodMouv(self,alpha):
        if(self.heuristique2()!=-1):
            return self.heuristique2()
        else:
            for i in range(0,len(self.bonmouv),2) :
                if self.bonmouv[i] >= alpha :
                    mo = self.bonmouv[i+1]
                    if self._board.is_valid_move(mo[0],mo[1],mo[2]):
                        return mo


    def getPlayerMove(self):
        if self._board.is_game_over():
            #print("Referee told me to play but the game is over!")
            return (-1,-1)
        nbMoves = self._board._nbWHITE + self._board._nbBLACK
        if nbMoves <= 80:
            alpha = self.negamax(4,1)
            move = self.getGoodMouv(alpha)
            self._board.push(move)

            self.bonmouv = []
            #print("I am playing ", move)
            (c,x,y) = move
            assert(c==self._mycolor)
            #print("My current board :")
            #print(self._board)
            return (x,y)
        else:
            alpha = self.negamax(20,1)
            move = self.getGoodMouv(alpha)
            self._board.push(move)

            self.bonmouv = []
            #print("I am playing ", move)
            (c,x,y) = move
            assert(c==self._mycolor)
            #print("My current board :")
            #print(self._board)
            return (x,y)





    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        #print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")
