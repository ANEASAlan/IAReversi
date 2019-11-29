import Reversi
import time
from io import StringIO
import pygame
import sys
import random
import csv
from xlwt import Workbook
import xlwt

sys.path.insert(1, 'Heuristics/Easy')
sys.path.insert(1, 'Heuristics/Medium')
sys.path.insert(1, 'Heuristics/Hard')
sys.path.insert(1, 'Player')
sys.path.insert(1, 'UI')

import UI

################################################################################
############################# JOUEURS ##########################################
################################################################################

import myPlayer
import randomPlayer
import myPlayerAlix
import myPlayerTitouan

################################################################################
############################# HEURISTIQUES #####################################
################################################################################

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

# Cette classe permet de stocker un joueur dans un "tournoi"
class PlayerTournament:

    # Initialisation de l'objet (seule fonction, cette classe est en réalité
    # plus proche d'une structure qu'autre chose mais ça n'existe pas en Python)
    def __init__(self, name, heuristic):

        # Le nom du joueur
        self.name = name

        # L'heuristique que le joueur utilise

        # Cette dernière doit avoir pour définition :
        # heuristic(board, move)

        # Les paramètres sont importants car lorsqu'elle est appelée par le
        # joueur, le plateau et le dernier move effectué lui sont passés en
        # paramètres, ne pas avoir cette définition causera donc une erreur lors
        # de l'exécution du code

        # Elle doit renvoyer une valeur dépendant de la couleur
        # Si la valeur témoigne d'un bon coup pour les blancs, la valeur doit
        # être positive, sinon elle doit être négative. Elle est nulle si le
        # coup n'avantage personne
        self.heuristic = heuristic

        # Cette variable permet de compte combien d'autre joueur ce joueur a
        # battu lors du "tournoi"
        self.wins = 0

        # Cette variable permet de compte combien de défaites à subi ce joueur
        # lors du "tournoi"
        self.loses = 0

        # Cette variable permet de compter combien de fois lors du "tournoi"
        # ce joueur a fait match nul
        self.deuces = 0

        # La liste des joueurs que le joueur a battu
        self.won = []

        # La liste des joueurs qui ont battu le ce joueur
        self.lost = []

        # La liste des joueurs contre qui ce joueur a fait match nul
        self.deuced = []

        # Le pourcentage de victoire ce joueur
        self.winRate = 0

    # Cette fonction affiche toutes les données corcernant le joueur actuel
    def printPlayer(self):
        print("----------------------------------\n")
        print("Le joueur " + str(self.name) + " : \n")

        print("A gagné " + str(self.wins) + " fois contre:\n")
        self.printAllPlayers(self.won)
        print("")

        print("A perdu " + str(self.loses) + " fois contre:\n")
        self.printAllPlayers(self.lost)
        print("")

        print("A fait " + str(self.deuces) + " match nul(s) contre:\n")
        self.printAllPlayers(self.deuced)
        print("")

        print("Son win rate est de " + str(self.winRate) + "\n")
        print("----------------------------------\n")

    def printAllPlayers(self, array):
        for player in array:
            print(player.name)

    def computeWinRate(self):
        self.winRate = self.wins / self.loses

# Cette classe représente un match
class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.loser = None

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

# Cette fonctio nlance un match entre tous les joueurs disponibles
# Heuristique est une liste de tous les joueurs possibles
def startTournament(players, matchs):

    # On va traverser les joueurs pour qu'ils s'affrontent, d'abord noir v blanc
    # puis blanc v noir
    for black in players:
        for white in players:

            print("Noir : " + str(black.name))
            print("Blanc : " + str(white.name))

            # On Crée le match courant
            match = Match(black, white)

            # On crée le plateau de jeu avec une taille de 10
            board = UI.createBoard(10)

            # On crée nos deux joueurs avec les bonnes heuristiques
            # On leur laisse 5 secondes pour décider chaque coup

            player1 = myPlayer.myPlayer(black.heuristic, 5)
            player2 = myPlayer.myPlayer(white.heuristic, 5)

            # On donne au plyer1 les noirs et au player2 les blancs
            competitors = UI.assignColors(board, player1, player2)

            # On démarre le match
            t = UI.play(board, competitors, withUI)

            # On récupère le résultat
            res = UI.printWinner(board, t)

            # Si les blancs ont gagné
            if res == 0:
                modifyPlayers(white, black)
                match.winner = white
                match.loser = black

            # Si les noirs ont gagné
            elif res == 1:
                modifyPlayers(black, white)
                match.winner = black
                match.loser = white

            # Si il y a eu égalité
            else:
                white.deuces += 1
                black.deuces += 1
                white.deuced.append(white)
                black.deuced.append(black)

            # On ajout le match à la liste des matchs
            matchs.append(match)

# cette fonction permet d'ajouter un joueur à la liste des joueurs pour le
# "tournoi"
def addPlayer(players, name, heuristic):
    players.append(PlayerTournament(name, heuristic))

# Cette fonction ajoute tous les joueurs qui participeront au "tournoi"
def addAllPlayers(players):
    addPlayer(players, "Colors", ColorsCounting.heuristic)
    # addPlayer(players, "ColumnsLines", ColumnsLinesCounting.heuristic)
    addPlayer(players, "Corners", CornersCounting.heuristic)
    addPlayer(players, "MonteCarlo", MonteCarlo.heuristic)
    addPlayer(players, "Move", MoveCounting.heuristic)
    # addPlayer(players, "Carlito (1)", MonteCarlito1.heuristic)
    # addPlayer(players, "Carlito (2)", MonteCarlito2.heuristic)
    # addPlayer(players, "Carlito (3)", MonteCarlito3.heuristic)
    # addPlayer(players, "Carlito (4)", MonteCarlito4.heuristic)
    # addPlayer(players, "Carlito (5)", MonteCarlito5.heuristic)
    # addPlayer(players, "Random", Random.heuristic)

# Cette fonction modifie les joueurs en fonction de qui a gagné et qui a perdu
# Le premier joueur est le gagnant et le second le perdant
def modifyPlayers(winner, loser):
    winner.wins += 1
    loser.loses += 1
    if not loser in winner.won:
        winner.won.append(loser)
    if not winner in loser.lost:
        loser.lost.append(winner)

# Cette fonction affiche les statistiques du tournoi
def results(players):
    for player in players:
        player.printPlayer()

# retourne l'index du joueur dans le tableau
def getPlayerIndex(players, player):
    i = 0
    for p in players:
        if p == player:
            return i
        i += 1
    return -1

# Cette fonction initialise la matrice passée en paramètre en fonction du
# nombre de joueur
def initMat(players, matrice):
    for x in range(len(players)):
        tmp = []
        for y in range(len(players)):
            tmp.append(0)
        matrice.append(tmp)

# Cette fonction rempli la matrcie en fonction des matchs qui ont été joués
# Une victoire ajoute un point, une défaite enlève un point
def fillMat(matchs, matrice):
    for match in matchs:
        # Si il n'y a pas eu de gagnants il n'y a rien à faire
        if match.winner != None:
            winner = getPlayerIndex(players, match.winner)
            loser = getPlayerIndex(players, match.loser)
            matrice[loser][winner] -= 1
            matrice[winner][loser] += 1

# Cette fonction sauvegarde les données stockés dans la matrice dans un fichier
# csv
def saveResults(filename, players, matrice):

    # On ouvre un book pour écrire dedans (c'est comme un fichier)
    book = Workbook()

    # On ajoute une feuille (il peut y en avoir plusieurs, il faut donc en
    # spécifier une)
    sheet = book.add_sheet('Sheet')

    # On écrit la liste des joueurs sur la première ligne (avec une cellule
    # vide tout à gauche)
    for x_index in range(len(players)):
        sheet.write(x_index + 1, 0, players[x_index].name)

    # On remplit les scores
    for y_index in range(len(players)):

        # On écrit le nom du joueur en premier sur la ligne
        sheet.write(0, y_index + 1, players[y_index].name)

        # On écrit ses résultats en fonction de ses adversaires
        for x_index in range(0, len(players)):

            # On choisit la couleur de fond (vert > 0, rouge < 0, bleu = 0)
            st = xlwt.easyxf('pattern: pattern solid;')
            if matrice[x_index][y_index] > 0:
                st.pattern.pattern_fore_colour = 3
            elif matrice[x_index][y_index] < 0:
                st.pattern.pattern_fore_colour = 2
            else:
                st.pattern.pattern_fore_colour = 4
            sheet.write(x_index + 1, y_index + 1, str(matrice[x_index][y_index]), st)

    # On sauvegarde le book en fichier
    book.save(filename)

################################################################################
############################# VARIABLES ########################################
################################################################################

# Si à True alors une interface graphique apparaît
withUI = False

# On récupère les arguments donnés par l'utilisateurs
argv = sys.argv

# Si il y a au moins un argument, on vérifie que le premier soit UI, si c'est le
# cas, alors on passe UI à True (lancement d'une interface graphique plus tard)
if len(argv) > 1 and argv[1] == "UI" :
    withUI = True

# La liste des joueurs
players = []

# La liste des matchs du tournoi
matchs = []

# Cette matrice contient les victoires/défaites de chaque IA
# Exemple :
#           Colors Corners Columns
# Colors     0        -2      -2
# Corners    2         0       0
# Columns    2         0       0
#
# Ici Colors a perdu 2 fois contre Corners et Columns, Corners a gagné autant
# de fois qu'il a perdu contre columns
matchMatrice = []

################################################################################
############################# MAIN #############################################
################################################################################

# On lance l'interface utilisateur si withUi est à True
UI.initUI(withUI)

# board = createBoard(10)
# player = myPlayer.myPlayer(CornersCounting.heuristic, 0)
# print(player.heuristicMethod(board, []))

# On ajoute tous les joueurs qui vont participer
addAllPlayers(players)

# On lance un match entre tous les joueurs disponibles (2 matchs par joueur)
startTournament(players, matchs)

# On affiche les résultats
# results(players)

initMat(players, matchMatrice)
fillMat(matchs, matchMatrice)
saveResults("Data/Results.xlsx", players, matchMatrice)
