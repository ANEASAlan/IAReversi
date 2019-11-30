import Reversi
import time
from io import StringIO
import pygame
import sys
import random

sys.path.insert(1, 'Heuristics/Easy')
sys.path.insert(1, 'Heuristics/Medium')
sys.path.insert(1, 'Heuristics/Hard')
sys.path.insert(1, 'Player')
sys.path.insert(1, 'UI')
sys.path.insert(1, 'Utils')

import UI
import Tournament
import ExcelFile

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
import Fusion
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

# cette fonction permet d'ajouter un joueur à la liste des joueurs pour le
# "tournoi"
def addPlayer(players, name, heuristic):
    players.append(Tournament.PlayerTournament(name, heuristic))

# Cette fonction ajoute tous les joueurs qui participeront au "tournoi"
def addAllPlayers(players):
    addPlayer(players, "Move", MoveCounting.heuristic)
    addPlayer(players, "Fusion", Fusion.heuristic)
    # addPlayer(players, "Colors", ColorsCounting.heuristic)
    # addPlayer(players, "ColumnsLines", ColumnsLinesCounting.heuristic)
    # addPlayer(players, "Corners", CornersCounting.heuristic)
    # addPlayer(players, "MonteCarlo", MonteCarlo.heuristic)
    # addPlayer(players, "Carlito (1)", MonteCarlito1.heuristic)
    # addPlayer(players, "Carlito (2)", MonteCarlito2.heuristic)
    # addPlayer(players, "Carlito (3)", MonteCarlito3.heuristic)
    # addPlayer(players, "Carlito (4)", MonteCarlito4.heuristic)
    # addPlayer(players, "Carlito (5)", MonteCarlito5.heuristic)
    # addPlayer(players, "Random", Random.heuristic)

# Cette fonction affiche les statistiques du tournoi
def results(players):
    for player in players:
        player.printPlayer()

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

# La taille du plateau
boardSize = 8

# Un objet tournoi pour réaliser des tournoi
tournament = None

# Nombre de tournoi lancés à la suite
nbTournament = 10

################################################################################
############################# MAIN #############################################
################################################################################

# On lance l'interface utilisateur si withUi est à True
UI.initUI(withUI, boardSize)

# board = createBoard(10)
# player = myPlayer.myPlayer(CornersCounting.heuristic, 0)
# print(player.heuristicMethod(board, []))

# On ajoute tous les joueurs qui vont participer
addAllPlayers(players)

# On crée un nouveau tounoi
tournament = Tournament.Tournament()

# On ajoute tous les matchs possibles (tous les joueurs se rencontrent deux fois)
tournament.createAllMatchs(players)

# On initialise la matrice avec des 0 partout
ExcelFile.initMat(players, matchMatrice)

# On effectue tous les matchs
for i in range(nbTournament):
    tournament.startTournament(boardSize, withUI)
    ExcelFile.fillMat(players, tournament.matchs, matchMatrice)

# On affiche les résultats
results(players)

ExcelFile.saveResults("Data/Results.xlsx", players, matchMatrice, nbTournament)
