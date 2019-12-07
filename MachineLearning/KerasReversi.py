# -*-coding:Latin-1 -*

import sys

sys.path.insert(1, '../')

import Reversi
import numpy
from keras.models import Sequential
from keras.layers import Dense

# Une classe représentant la topologie
class Topology:

    def __init__(self):
        self.topology = []

    def addLayer(self, nbNeurons):
        self.topology.append(nbNeurons)

    def getLength(self):
        return len(self.topology)

    def getLayerSize(self, i):
        return self.topology[i]

class NeuralNetwork:

    MIN_TOPOLOGY_LENGTH = 3 # Au moins une entrée, une couche et une sortie

    def __init__(self, topology):

        # La topologie du réseau de neurone, c'est-à-dire le nombre de couches
        # et le nombre de neurones par couche
        self.topology = topology

        # Le modèle keras (le réseau de neurones en tant que tel)
        self.model = Sequential()

        # On crée le réseau
        self.createModel()

        # Position de la dernière couche
        self.last = self.topology.getLength() - 2

        # Dummy y values
        self.dummyY = []

    # Cette fonction crée le modèle keras à utiliser
    def createModel(self):

        # S'il n'y a pas au moins une entrée, une couche et une sortie,
        # on ne crée pas le modèle
        if self.topology.getLength() >= self.MIN_TOPOLOGY_LENGTH:

            # On crée la couche d'entrée et la première couche cachée
            self.model.add(Dense(self.topology.getLayerSize(1),
                       input_dim=self.topology.getLayerSize(0),
                       activation='sigmoid'))

            # On crée toutes les autres couches
            for layer in range(2, self.topology.getLength()):
                self.model.add(Dense(self.topology.getLayerSize(layer),
                       activation='sigmoid'))

            # On compile le modèle
            self.model.compile(loss=self.dummyLoss, optimizer='adam', metrics=['accuracy'])

    # Utilisation du réseau de neurones
    def compute(self, inputs):
        # self.dummyY = self.generateDummyY(len(inputs))
        return self.model.predict(inputs)

    def dummyLoss(self, y_true, y_pred):
        return y_pred

    def generateDummyY(self, size):
        dummy = []
        for i in range(size):
            dummy.append(i)
        return dummy

    def getLayers(self):
        return self.model.layers
