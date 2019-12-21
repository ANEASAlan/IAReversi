# -*- coding: utf-8 -*-

#notre joueur, à implémenter en modifiant getPlayerMove()

import time
import Reversi
import random
import createTab
import PositivePowerSpots as PPS
import sys
sys.path.insert(1,"Heuristics/Easy")
from Random import heuristic as Rd
from playerInterface import *
from enum import Enum

# Cette classe est utilisé dans l'algorithme alpha beta avec mémoire
# Cela permet de stocker si on doit modifier alpha, beta ou retourner
# immédiatemment de la fonction
class Flag(Enum):
    VALUE = 1
    LOW = 2
    UP = 3

# Cette classe permet de stocker un noeud dans notre mémoire
class NodeValue():

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.flag = Flag.VALUE
        self.startingDepth = 0

class myPlayer(PlayerInterface):

    def __init__(self, heuristicMethod, maxTime, boardSize, randomnessTheo = 0, randomnessAlan = 0): # penser à enelever les arguments (sauf self)

        self.randomnessTheo = randomnessTheo
        self.randomnessAlan = randomnessAlan

        # Notre plateau de jeu
        self._board = Reversi.Board(boardSize)

        # Notre couleur
        self._mycolor = None

        # - infini
        self.minInt = - 2 ** 64

        # + infini
        self.maxInt = - self.minInt

        # La méthode heuristique que nosu utilisons
        self.heuristicMethod = heuristicMethod

        # Notre mémoire
        self.memory = {}

        # La table de hashage (3 * (size * size))
        self.table = []
        self.generateBaseHash()

        # Le temps écouler depuis que nous faisons une recherche dans notre
        # arbre
        self.time = 0

        # Le temps maximal durant lequel nous pouvons faire une recherche
        self.maxTime = maxTime

        self.myPowerSpots = [
            [99,  -8,  8,  6,  3,  3,  6,  8,  -8, 99],
            [-8, -24, -4, -3, -3, -3, -3, -4, -24, -8],
            [ 8,  -4,  7,  4,  2,  2,  4,  7,  -4,  8],
            [ 6,  -3,  4,  0,  0,  0,  0,  4,  -3,  6],
            [ 3,  -3,  2,  0,  0,  0,  0,  2,  -3,  3],
            [ 3,  -3,  2,  0,  0,  0,  0,  2,  -3,  3],
            [ 6,  -3,  4,  0,  0,  0,  0,  4,  -3,  6],
            [ 8,  -4,  7,  4,  2,  2,  4,  7,  -4,  8],
            [-8, -24, -4, -3, -3, -3, -3, -4, -24, -8],
            [99,  -8,  8,  6,  3,  3,  6,  8,  -8, 99]
        ]

        self.ennemyPowerSpots = [
            [99,  -8,  8,  6,  3,  3,  6,  8,  -8, 99],
            [-8, -24, -4, -3, -3, -3, -3, -4, -24, -8],
            [ 8,  -4,  7,  4,  2,  2,  4,  7,  -4,  8],
            [ 6,  -3,  4,  0,  0,  0,  0,  4,  -3,  6],
            [ 3,  -3,  2,  0,  0,  0,  0,  2,  -3,  3],
            [ 3,  -3,  2,  0,  0,  0,  0,  2,  -3,  3],
            [ 6,  -3,  4,  0,  0,  0,  0,  4,  -3,  6],
            [ 8,  -4,  7,  4,  2,  2,  4,  7,  -4,  8],
            [-8, -24, -4, -3, -3, -3, -3, -4, -24, -8],
            [99,  -8,  8,  6,  3,  3,  6,  8,  -8, 99]
        ]

        self.powerCarlito1 = createTab.createTab(1, self._board._boardsize)
        self.powerCarlito2 = createTab.createTab(2, self._board._boardsize)
        self.powerCarlito3 = createTab.createTab(3, self._board._boardsize)
        self.powerCarlito4 = createTab.createTab(4, self._board._boardsize)
        self.powerCarlito5 = createTab.createTab(5, self._board._boardsize)

    # Returns your player name, as to be displayed during the game
    def getPlayerName(self):
        return "ANEAS DE CASTRO PINTO"

    # Renvoie la couleur inverse de color
    def reverseColor(self, color):
        if color == self._board._BLACK:
            return self._board._WHITE
        return self._board._BLACK

    # Génère une valeur de base pour la table de hashage
    def generateBaseHash(self):

        # La taille du plateau
        size = self._board.get_board_size()

        # Le plateau
        board = self._board._board

        # La superficie du plateau
        area = size * size

        # Pour chaque case du tableau
        for i in range(area):

            # Une ligne de la table de hashage
            tmp = []

            # Pour chaque type de case possible
            for j in range(3):

                # On ajoute un nombre codé sur 64 bits aléatoire
                tmp.append(random.randint(0, self.maxInt - 1))

            # On ajoute la ligne crée
            self.table.append(tmp)

    # On calcule le hash de chaque case
    def computeHash(self):

        # Hash de base
        hash = 0

        # Taille du plateau
        size = self._board.get_board_size()

        # Le plateau
        boardArray = self._board._board

        # On parcourt le tableau
        for x in range(size):
            for y in range(size):

                # Si la cellule n'est pas vide
                if boardArray[x][y] != self._board._EMPTY:

                    # On récupère la pièce
                    piece = boardArray[x][y]

                    # On modifie le hash dans la case correspondante
                    hash = hash ^ self.table[x * size + y][piece]

        # On retourne le hash final correspondant au plateau actuel
        return hash

    # Version sans mémoire de neg alpha beta
    # PAS A JOUR NE PAS UTILISER POUR L'INSTANT !!!!
    def negAlphaBeta(self, depth, alpha, beta, color):

        # Si le jeu est terminé, on renvoie la valeur de l'heuristique
        # On va aussi utiliser une profondeur d'arrêt
        if depth == 0 or self._board.is_game_over():
            return (None, self.heuristicMethod(self._board))

        # Le coup a retourné, celui à jouer, None par défaut mais normalement
        # il est toujours possible d'au moins changer cette valeur
        moveToPlay = None

        # La valeur heuristique maximale trouvée
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

            # On inverse la valeur récupérée puisque c'était le maximum ennemi
            maxVal = max(-val, maxVal)

            # Si la valeur récupéré est meilleure que notre pire coup
            if maxVal > alpha:
                moveToPlay = move
                alpha = maxVal

                # Si le pire coup est meilleur que tout meilleur coup (élagage)
                if alpha >= beta:
                    return (moveToPlay, alpha)

        return (moveToPlay, alpha)

    # Neg alpha beta avec mémoire
    def negAlphaBetaWithMemory(self, depth, alpha, beta, color, hash, playedMove):

        if random.random() < self.randomnessTheo :
            return (None, alpha)

        # On récupère le temps écoulé depuis le début de l'algorithme
        elapsedTime = time.time() - self.time

        # Si on a passé plus que le temps maximal possible à chercher un coup
        # On s'arrête ici
        if self.startingDepth != depth and elapsedTime >= self.maxTime:
            return (None, self.heuristicMethod(self._board, playedMove,self))

        # La valeur d'alpha au moment de commencer la recherche à partir de cette racine
        alphaOrig = alpha

        # Si cette table existe déjà dans la liste des tables
        if hash in self.memory:

            # On récupère les données du noeud déjà calculées
            nodeVal = self.memory[hash]

            # Si le noeud était plus profond que la profondeur actuelle
            if nodeVal.depth >= depth:

                # Si nous ne sommes pas sur le premeir noeud nosu retournons
                # immédiatemment la valeur
                if self.startingDepth != depth and nodeVal.flag == Flag.VALUE:
                    return (None, nodeVal.value)

                # Si la valeur était la valeur d'alpha
                elif nodeVal.flag == Flag.LOW:
                    alpha = max(alpha, nodeVal.value)

                # Sinon c'est la valeur de beta
                else:
                    beta = min(beta, nodeVal.value)

                # Si alpha >= beta, on coupe quand dans l'algo sans mémoire
                if self.startingDepth != depth and alpha >= beta:
                    return (None, nodeVal.value)


        # Si le jeu est terminé, on renvoie la valeur de l'heuristique
        # On va aussi utiliser une profondeur d'arrêt
        if depth == 0 or self._board.is_game_over():
            # # print("Reached the end!")
            return (None, self.heuristicMethod(self._board, playedMove, self))

        # Le coup a retourné, celui à jouer
        moveToPlay = None

        # La valeur heuristique maximale trouvée
        maxVal = self.minInt

        # On parcourt la liste des coups valides
        for move in self._board.legal_moves():

            # On joue le premier coup valide
            self._board.push(move)

            # On calcule le hash de la nouvelle table grâce à un XOR astucieux
            tmpHash = hash ^ (self.table[move[1] * self._board.get_board_size() + move[2]][move[0]])

            # Recursivité pour parcourir l'arbre
            # On diminue la profondeur de un afin d'être sûr de s'arrêter
            (_, val) = self.negAlphaBetaWithMemory(depth - 1, -beta, -alpha, self.reverseColor(color), tmpHash, move)

            # On retire le coup que nous venos de jouer
            self._board.pop()

            # On inverse la valeur récupérée puisque c'était le maximum ennemi
            maxVal = max(-val, maxVal)

            # Si la valeur récupéré est meilleure que notre pire coup
            if maxVal > alpha:
                moveToPlay = move
                alpha = maxVal

                # Si le pire coup est meilleur que tout meilleur coup (élagage)
                if alpha >= beta:
                    break

            # Si on a cherché pendant plus que la maximum accordé, on quitte
            elapsedTime = time.time() - self.time
            if elapsedTime >= self.maxTime:
                break

        # On crée les données du noeud actuel
        nodeVal = NodeValue(maxVal, depth)

        # On prépare le flag dans le cas où on retomberait sur ce plateau
        if maxVal <= alphaOrig:
            nodeVal.flag = Flag.UP
        elif maxVal >= beta:
            nodeVal.flag = Flag.LOW
        else:
            nodeVal.flag = Flag.VALUE

        # On lie le hash de la table à ce noeud
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

        move = None

        if self.heuristicMethod == Rd :
            move = random.choice(self._board.legal_moves())
        else:
            # (move, _) = self.negAlphaBeta(3, self.minInt, self.maxInt)
            # moveToPlay = None
            # if random.randint(0, 100) == 0:
            #     self.memory = {}

            # On stocke le temps auquel la recherche a commencé
            self.time = time.time()

            # Iterative Deepening, on cherche pour 1, 2, 3 ..., n-1
            for i in range(1, 100):

                # La profondeur de base (ce n'est pas 0, on stocke la profondeur à
                # laquelle on veut aller)
                self.startingDepth = i

                # La recherche !
                move = None
                if random.random() < self.randomnessAlan :
                    move = random.choice(self._board.legal_moves())
                else :
                    (move, _) = self.negAlphaBetaWithMemory(i, self.minInt, self.maxInt, self._mycolor, self.computeHash(), None)
                # print(heur1)

                # print(move)
                # print(heur1)

                # Si il n y a pas de coup retourné par l'algorithme
                if move == None:
                    move = self._board.legal_moves()[0]

                # Si le temps maximum de recherche est dépassé, on s'arrête
                elapsedTime = time.time() - self.time
                if elapsedTime >= self.maxTime:
                    break

        # print("Move played :")
        # print(moveToPlay)
        # print("------------")
        # (move2, heur2) = self.negAlphaBeta(4, self.minInt, self.maxInt)

        # print("Result = " + str(move) + " / " + str(heur1))
        # print("Expected = " + str(move2) + " / " + str(heur2))

        self._board.push(move) #joue le coup choisi dans move

        # print("I am playing ", move)

        (c,x,y) = move #la case sur laquelle jouer le coup move, (couleur, abscisse, ordonnée)

        assert(c==self._mycolor) #si pas la bonne couleur, problème

        # print("My current board :")

        # print(self._board)
        length = len(self.myPowerSpots)
        if (y == 0 or y == length - 1) and (x == 0 or x == length - 1):
            PPS.PositivePowerSpots(self.myPowerSpots, x, y)

        return (x,y) #renvoyer le coup à jouer

    # Inform you that the oponent has played this move. You must play it
    # with no search (just update your local variables to take it into account)
    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        # # print("Opponent played ", (x,y))
        length = len(self.myPowerSpots)
        if (y == 0 or y == length - 1) and (x == 0 or x == length - 1):
            PPS.PositivePowerSpots(self.ennemyPowerSpots, x, y)
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
