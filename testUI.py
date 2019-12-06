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
import ArgumentsReader as ArgR

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
    addPlayer(players, "Colors", ColorsCounting.heuristic)
    # addPlayer(players, "ColumnsLines", ColumnsLinesCounting.heuristic)
    # addPlayer(players, "Corners", CornersCounting.heuristic)
    # addPlayer(players, "MonteCarlo", MonteCarlo.heuristic)
    # addPlayer(players, "Carlito1", MonteCarlito1.heuristic)
    # addPlayer(players, "Carlito2", MonteCarlito2.heuristic)
    # addPlayer(players, "Carlito3", MonteCarlito3.heuristic)
    # addPlayer(players, "Carlito4", MonteCarlito4.heuristic)
    # addPlayer(players, "Carlito5", MonteCarlito5.heuristic)
    # addPlayer(players, "Random", Random.heuristic)

# Cette fonction affiche le nom de tous les joueurs disponibles
def displayPlayers(players):
    print("Liste des joueurs :")
    print("")
    for player in players:
        print(player.name)
    print("")

################################################################################
############################# VARIABLES ########################################
################################################################################

# On récupère les arguments donnés par l'utilisateurs
argv = sys.argv

# La liste des arguments
args = ArgR.getArguments(argv)

# Si à True alors une interface graphique apparaît
withUI = args.withUI

# La liste des joueurs
players = []

# La taille du plateau
boardSize = args.boardSize

# Un objet tournoi pour réaliser des tournoi
tournament = None

################################################################################
############################# MAIN #############################################
################################################################################

# On affiche la liste des arguments passés
args.printArgs()

# On lance l'interface utilisateur si withUi est à True
UI.initUI(withUI, boardSize)

# On ajoute tous les joueurs qui existent
addAllPlayers(players)

# Si l'utilisateur l'a demandé, on affiche tous les joueurs disponibles
if args.displayPlayers:
    displayPlayers(players)

# board = createBoard(10)
# player = myPlayer.myPlayer(CornersCounting.heuristic, 0)
# print(player.heuristicMethod(board, []))

# Si l'utilisateur a demandé des tournois
if args.nbTournament:
    Tournament.playTournament(players, args)

# Si l'utilisateur a demandé des matchs
if args.matchs:
    Tournament.playMatchs(players, args)
