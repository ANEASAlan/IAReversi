# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayer():

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = 2

    def getPlayerName(self):
        return "TNHalfBrain"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        moves = [m for m in self._board.legal_moves()]
        nb = -1000
        move = moves[randint(0,len(moves)-1)]          
        (h,move) = self.MiniMax(3,-1000,1000)
        self._board.push(move)
##        print("I am playing ", move) 
        (c,x,y) = move
        assert(c==self._mycolor)
        print("My current board :")
        print(self._board)
        return (x,y)



    def MiniMax(self,n,alpha,beta):
        if(self._board.is_game_over()):
            (nbW,nbB) = self._board.get_nb_pieces()
            return (nbW - nbB,0)

        elif(n == 0):
            return (self.heuristique(),0)
    
        maxi = -10000
        for i in self._board.legal_moves():
            self._board.push(i)
            (alpha,move) = self.MaxMin(n-1,alpha,beta)
            if(alpha > maxi):
                maxi = alpha
                play = i
                if(alpha>=beta):
                    self._board.pop()
                    return (beta,play)
            elif(alpha == maxi):
                if(randint(0,1)):
                    play = i
            self._board.pop()
        return (alpha,play)

    def MaxMin(self,n,alpha,beta):
        if(self._board.is_game_over()):
            (nbW,nbB) = self._board.get_nb_pieces()
            return (nbW - nbB,0)

        elif(n == 0):
            return (self.heuristique(),0)
        
        mini = 10000
        for i in self._board.legal_moves():
            self._board.push(i)
            (beta,move) = self.MiniMax(n-1,alpha,beta)
            if(beta < mini):
                mini = beta
                play = i
                if(beta<=alpha):
                    self._board.pop()
                    return (alpha,play)
            elif(beta == mini):
                if(randint(0,1)):
                    play = i
            self._board.pop()
        return (beta,play)

    def heuristique(self):
##        (nbW,nbB) = self._board.get_nb_pieces()
##        score = nbW - nbB
        score = 0
        for x in range (9):
                for y in range (9):
                    if( self._board._board[x][y] == 1 ):
                        val = -1
                    elif( self._board._board[x][y] == 2 ):
                        val = 1
                    else:
                        break
                    if(( x == 0 or x == 9 ) and ( y == 0 or y == 9 )):
                        score += 50*val
                    #elif((0 <= x <= 1 or 8 <= x <= 9) and (0 <= y <= 1 or 8 <= y <= 9)):
                    elif((x == 8 or x == 1) and (y == 1 or y == 8)):
                        score += -10 * val
##                    elif( x == 0 or x == 9 or y == 0 or y == 9 ):
##                        score += 2*val
                    else:
                        score += val
        moves = [m for m in self._board.legal_moves()]
        for i in moves:
            score -=2
        return score
    
    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
##        print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def fight(turn):
        if self._board.is_game_over():
            print("Resultat : ", self._board.result())
            return
    
        if(turn%2 == 1):
            (maxi,move) = Minimax(1)
            self._board.push(move)
        else:
            (maxi,move) = Minimax(3)
            self._board.push(move)
        print("h = ", heuristique())
        print("turn : ", turn)
        print(self._board)
        print()
        fight(self._board,turn+1)
    


