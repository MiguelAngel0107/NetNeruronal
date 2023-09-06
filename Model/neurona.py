import math


class Neurona:
    def __init__(self, pesos, entradas):
        self.entradas = entradas
        self.pesos = pesos

        print('___________ Neurona ___________')
        print('Entradas: ', entradas)
        print('Pesos: ', pesos)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def weighted_sum(self):
        # Calcula la suma ponderada de las entradas y pesos
        suma_ponderada = sum(x * w for x, w in zip(self.entradas, self.pesos))
        return suma_ponderada

    def output(self):
        # Calcula la salida aplicando la función sigmoide a la suma ponderada
        suma_ponderada = self.weighted_sum()
        #print('Suma Ponderada: ', suma_ponderada)
        #print('Suma Ponderada + F(activacion): ', self.sigmoid(suma_ponderada))
        return self.sigmoid(suma_ponderada)

    def getPesos(self):
        print('Estos pesos estoy imprimiendo', self.pesos)
        return self.pesos

    def updatePesos(self):
        pass
