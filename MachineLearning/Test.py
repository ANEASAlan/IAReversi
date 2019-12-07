# -*-coding:Latin-1 -*

import KerasReversi
import random

topology = KerasReversi.Topology()
topology.addLayer(1)
topology.addLayer(3)
topology.addLayer(3)
topology.addLayer(1)


def addNN(topology, l, nb):
    for i in range(nb):
        l.append(KerasReversi.NeuralNetwork(topology))

def computeAll(l, res):
    for i in range(len(l)):
        res.append(l[i].compute([2]))

# for i in range(1):
#     for layer in l[i].getLayers():
#         for weight in layer.get_weights():
#             print(weight.tolist())

def swap(tbl, s, e):
    tmp = tbl[s]
    tbl[s] = tbl[e]
    tbl[e] = tmp

def bubbleSort(tbl1 ,tbl2):
    for i in range(len(tbl1)):
        for j in range(0, len(tbl1) - i - 1):
            if tbl1[j] < tbl1[j + 1]:
                swap(tbl1, j, j+1)
                swap(tbl2, j, j+1)

def haveRabies(tbl, nb):
    for i in range(nb):
        del tbl[len(tbl) - 1]

def modifyWeights(layers):
    i = 0
    for layer in layers:
        for w in layer.get_weights():
            print(w)

def haveBaby(topology, father):
    nn = KerasReversi.NeuralNetwork(topology)
    i = 0
    layers = modifyWeights(father.getLayers())
    for layer in layers:
        nn.model.layers[i].set_weights(layer.get_weights())
        i += 1
    return nn

def haveBabies(topology, tbl, nb):
    size = len(tbl)
    for i in range(size):
        tbl.append(haveBaby(topology, tbl[i]))

l = []
addNN(topology, l, 100)
for i in range(20):
    print("Gen: " + str(i))
    res = []
    computeAll(l ,res)
    bubbleSort(res, l)
    haveRabies(l, 50)
    haveBabies(topology, l, 50)

    print("The best of this generation reached: " + str(l[0].compute([2])))
