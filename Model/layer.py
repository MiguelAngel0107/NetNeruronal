import random
from .neurona import Neurona


class Layer:
    def __init__(self, num_neuronas, inputs):
        self.num_neuronas = num_neuronas
        self.neuronas = [Neurona([random.uniform(-1, 1) for _ in inputs], inputs)
                         for _ in range(num_neuronas)]

    def forward(self):
        # Calcular las salidas de todas las neuronas en la capa
        salidas = [neurona.output() for neurona in self.neuronas]
        #print(salidas)
        return salidas

    def getDicPesos(self):
        # Calcular las salidas de todas las neuronas en la capa
        pesosLayer = [neurona.getPesos() for neurona in self.neuronas]
        #print('Estruct Pesos:', pesosLayer)
        return pesosLayer
