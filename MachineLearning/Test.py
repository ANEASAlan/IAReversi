# -*-coding:Latin-1 -*

#import KerasReversi
import random
import sys
sys.path.insert(1, 'Utils')
import Tournament
import Reversi
sys.path.insert(1, './')
import testUI
import ChangePowerSpots
sys.path.insert(1, 'Heuristics/Easy')
sys.path.insert(1, 'Heuristics/Medium')
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
import MonteCarlo
sys.path.insert(1, './UI')
import UI

# topology = KerasReversi.Topology()
# topology.addLayer(1)
# topology.addLayer(3)
# topology.addLayer(3)
# topology.addLayer(1)
#
#
# def addNN(topology, l, nb):
#     for i in range(nb):
#         l.append(KerasReversi.NeuralNetwork(topology))
#
# def computeAll(l, res):
#     for i in range(len(l)):
#         res.append(l[i].compute([2]))
#
# # for i in range(1):
# #     for layer in l[i].getLayers():
# #         for weight in layer.get_weights():
# #             print(weight.tolist())
#
# def swap(tbl, s, e):
#     tmp = tbl[s]
#     tbl[s] = tbl[e]
#     tbl[e] = tmp
#
# def bubbleSort(tbl1 ,tbl2):
#     for i in range(len(tbl1)):
#         for j in range(0, len(tbl1) - i - 1):
#             if tbl1[j] < tbl1[j + 1]:
#                 swap(tbl1, j, j+1)
#                 swap(tbl2, j, j+1)
#
# def haveRabies(tbl, nb):
#     for i in range(nb):
#         del tbl[len(tbl) - 1]
#
# def modifyWeights(layers):
#     i = 0
#     for layer in layers:
#         for w in layer.get_weights():
#             print(w)
#
# def haveBaby(topology, father):
#     nn = KerasReversi.NeuralNetwork(topology)
#     i = 0
#     layers = modifyWeights(father.getLayers())
#     for layer in layers:
#         nn.model.layers[i].set_weights(layer.get_weights())
#         i += 1
#     return nn
#
# def haveBabies(topology, tbl, nb):
#     size = len(tbl)
#     for i in range(size):
#         tbl.append(haveBaby(topology, tbl[i]))
#
# l = []
# addNN(topology, l, 100)
# for i in range(20):
#     print("Gen: " + str(i))
#     res = []
#     computeAll(l ,res)
#     bubbleSort(res, l)
#     haveRabies(l, 50)
#     haveBabies(topology, l, 50)
#
#     print("The best of this generation reached: " + str(l[0].compute([2])))


def addPlayer(players, name, heuristic):
    players.append(Tournament.PlayerTournament(name, heuristic))

def addAllPlayers(players):
    addPlayer(players, "Move", MoveCounting.heuristic)
    addPlayer(players, "Fusion", Fusion.heuristic)
    addPlayer(players, "Colors", ColorsCounting.heuristic)
    addPlayer(players, "ColumnsLines", ColumnsLinesCounting.heuristic)
    addPlayer(players, "Corners", CornersCounting.heuristic)
    addPlayer(players, "MonteCarlo", MonteCarlo.heuristic)
    addPlayer(players, "Carlito1", MonteCarlito1.heuristic)
    addPlayer(players, "Carlito2", MonteCarlito2.heuristic)
    addPlayer(players, "Carlito3", MonteCarlito3.heuristic)
    addPlayer(players, "Carlito4", MonteCarlito4.heuristic)
    addPlayer(players, "Carlito5", MonteCarlito5.heuristic)
    addPlayer(players, "Random", Random.heuristic)

def genRandomWeights(nb):
    l = []
    for i in range(nb):
        l.append(random.uniform())

def testNWeights():
    board = Reversi.Board(10)
    players = []
    playerList = []
    addAllPlayers(players)
    player1 = Tournament.getPlayerFromName(players, 'Fusion')
    player2 = Tournament.getPlayerFromName(players, 'Random')
    match = Tournament.Match(player1, player2)
    Tournament.startMatch(board, match, 10, False, 0.1, Fusion.CustomWeights)
    if(match.winner == player1):
        print(board._nbBLACK)
        print(Fusion.CustomWeights)
    ##ChangePowerSpots.ChangeForEntireTable(player1._board, Fusion.CustomWeights[1])


#UI.initUI(True, 10)
testNWeights()
