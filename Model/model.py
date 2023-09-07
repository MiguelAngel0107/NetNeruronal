from .layer import Layer

class ModeloNeuronal:
    def __init__(self, capa_entrada, capas_ocultas, num_salidas):
        self.capa_entrada = capa_entrada
        self.capas_ocultas = capas_ocultas
        self.num_salidas = num_salidas
        self.capas = []

        print('------------ Capa Entrada ------------')

        # Crear capa de entrada
        capa_entrada = Layer(
            num_neuronas=len(capa_entrada), inputs=capa_entrada)
        capa_entrada.forward()
        self.capas.append(capa_entrada)

        print('\n\n------------Capas Ocultas ------------')

        # Crear capas ocultas
        for num_neuronas in capas_ocultas:
            capa = Layer(num_neuronas=num_neuronas,
                         inputs=self.capas[-1].forward())
            self.capas.append(capa)

        print('\n\n------------ Capa Salida ------------')

        # Crear capa de salida
        capa_salida = Layer(num_neuronas=num_salidas,
                            inputs=self.capas[-1].forward())
        self.capas.append(capa_salida)

    def forward(self):
        # print('Cantidad de capas', len(self.capas))
        return

    def getDataInput(self):
        return self.capa_entrada