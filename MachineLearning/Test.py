# source /net/ens/DeepLearning/tensorflow/bin/activate dans le terminal.
# python2
# exec(open('lab1_skeleton.py').read())



# -*-coding:Latin-1 -*

import KerasReversi

topology = KerasReversi.Topology() # Creation des couches du reseaux
topology.addLayer(1)
topology.addLayer(3)
topology.addLayer(3)
topology.addLayer(1)

l = [] # Layers, couches
res = []
for i in range(100):
    l.append(KerasReversi.NeuralNetwork(topology))

for i in range(100):
    res.append(l[i].compute([2]))

for i in range(1):
    for layer in l[i].getLayers():
        for weight in layer.get_weights():
            print(weight.tolist())
