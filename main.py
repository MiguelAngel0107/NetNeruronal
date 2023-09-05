import matplotlib.pyplot as plt
import numpy as np
from Model.model import ModeloNeuronal


# Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
modelo = ModeloNeuronal(capa_entrada=[0.5, 0.7], capas_ocultas=[
                        3, 3], num_salidas=1)


def dibujar_neurona(x, y, pesos, destino_x, destino_y):
    # Crea un objeto de neurona como un círculo
    circulo = plt.Circle((x, y), 0.1, color='blue', fill=False)
    plt.gca().add_patch(circulo)

    print('Dentro de Pesos es:', pesos)
    print('La variable X es:', x)
    print('La variable Y es:', y)

    # Dibuja los pesos como flechas
    for i, peso in enumerate(pesos):

        plt.arrow(x, y, destino_x - x, destino_y - y,
                  head_width=0.02, head_length=0.02, fc='red', ec='red')
        plt.text(destino_x + 0.12, destino_y + 0.12 + i/10, f'\n w{i+1} = {peso:.2f}', color='red')


def dibujar_red_neuronal(modelo):
    # Configura la figura
    plt.figure()
    plt.axis('equal')
    plt.axis('off')

    # Coordenadas iniciales para las capas
    # Cambia esto según tu número de capas ocultas
    capa_x = [0.2, 0.5, 0.8, 1.1]
    capa_y = np.linspace(0.1, 0.9, len(capa_x))

    # Dibuja las neuronas y sus pesos para cada capa
    for i, capa in enumerate(modelo.capas):
        for j, neurona in enumerate(capa.neuronas):

            x = capa_x[i]
            y = capa_y[j]

            pesos = neurona.pesos

            # Calcula las coordenadas de destino
            if i + 1 < len(capa_x):
                destino_x = capa_x[i + 1]
                destino_y = capa_y[int(j / len(capa_y) * len(capa_x))]
            else:
                destino_x = capa_x[i] + 0.3
                destino_y = y


            dibujar_neurona(x, y, pesos, destino_x, destino_y)


    # Muestra el diagrama de flujo
    plt.show()


dibujar_red_neuronal(modelo)
