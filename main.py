import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from Model.model import ModeloNeuronal


# Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
modelo = ModeloNeuronal(capa_entrada=[0.5, 0.7, 0.5], capas_ocultas=[
                        3,3,3,6], num_salidas=10)


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
        plt.text(destino_x + 0.12, destino_y + 0.12 + i /
                 10, f'\n w{i+1} = {peso:.2f}', color='red')


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


def plot_neural_network(modelo):
    # Crear una figura de matplotlib
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_aspect('equal')

    # Diccionario para almacenar las coordenadas de las neuronas
    neuron_coordinates = {}

    # Tamaño de las neuronas
    neuron_radius = 0.5

    # Espacio horizontal entre capas
    x_spacing = 2.5

    # Espacio vertical entre neuronas en cada capa
    y_spacing = 2

    # Espacio vertical entre neuronas en cada capa
    x_spacing_text_neurona = -0.15

    # Dibujar neuronas de entrada
    input_layer = modelo.capas[0]

    arreglo = modelo.capas
    subarreglo_mas_largo = max(arreglo, key=lambda x: len(x.neuronas))

    x_position = 1
    for i, neurona in enumerate(input_layer.neuronas):
        y_position = (i + 1) * y_spacing
        neuron_coordinates[neurona] = (x_position, y_position)
        ax.add_patch(plt.Circle((x_position, y_position),
                     neuron_radius, color='blue'))
        ax.text(x_position + x_spacing_text_neurona, y_position + 0.25,
                f'I {i + 1}', va='center', fontsize=8, color='white')
        ax.text(x_position + x_spacing_text_neurona - 0.2, y_position,
                    f'{neurona.output():.4f}', va='center', fontsize=8, color='white')

    # Dibujar capas ocultas
    x_position += x_spacing
    for capa in modelo.capas[1:-1]:
        for i, neurona in enumerate(capa.neuronas):
            y_position = (i + 1) * y_spacing
            neuron_coordinates[neurona] = (x_position, y_position)
            ax.add_patch(plt.Circle((x_position, y_position),
                         neuron_radius, color='green'))
            ax.text(x_position + x_spacing_text_neurona, y_position + 0.25,
                    f'H {i + 1}', va='center', fontsize=8, color='white')
            ax.text(x_position + x_spacing_text_neurona - 0.2, y_position,
                    f'{neurona.output():.4f}', va='center', fontsize=8, color='white')

        x_position += x_spacing

    # Dibujar neurona de salida
    output_layer = modelo.capas[-1]
    x_position += x_spacing
    for i, neurona in enumerate(output_layer.neuronas):
        y_position = (i + 1) * y_spacing
        neuron_coordinates[neurona] = (x_position, y_position)
        ax.add_patch(plt.Circle((x_position, y_position),
                     neuron_radius, color='red'))
        ax.text(x_position + x_spacing_text_neurona, y_position + 0.25,
                f'O {i + 1}', va='center', fontsize=8, color='white')
        ax.text(x_position + x_spacing_text_neurona - 0.2, y_position,
                    f'{neurona.output():.4f}', va='center', fontsize=8, color='white')

    # Dibujar conexiones entre neuronas
    for capa in modelo.capas[:-1]:
        for neurona in capa.neuronas:
            for siguiente_capa in modelo.capas[modelo.capas.index(capa) + 1:]:
                for siguiente_neurona in siguiente_capa.neuronas:
                    ax.arrow(neuron_coordinates[neurona][0], 
                             neuron_coordinates[neurona][1],
                             neuron_coordinates[siguiente_neurona][0] - neuron_coordinates[neurona][0],
                             neuron_coordinates[siguiente_neurona][1] - neuron_coordinates[neurona][1],
                             head_width=0.04, head_length=0.05, fc='black', ec='black', linewidth=0.5
                            )

    ax.set_xlim(0, x_position + 1)
    ax.set_ylim(0, len(subarreglo_mas_largo.neuronas) * y_spacing + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def crear_grafo_red_neuronal(modelo):
    G = nx.Graph()  # Crea un grafo vacío

    # Agrega nodos para las capas y las neuronas
    for capa_idx, capa in enumerate(modelo.capas):
        for neurona_idx, neurona in enumerate(capa.neuronas):
            nodo_id = f"Capa {capa_idx + 1}, Neurona {neurona_idx + 1}"
            G.add_node(nodo_id)

    # Agrega bordes entre neuronas conectadas
    for capa_idx in range(len(modelo.capas) - 1):
        for neurona_idx, neurona in enumerate(modelo.capas[capa_idx].neuronas):
            for siguiente_neurona_idx, siguiente_neurona in enumerate(modelo.capas[capa_idx + 1].neuronas):
                G.add_edge(
                    f"Capa {capa_idx + 1}, Neurona {neurona_idx + 1}",
                    f"Capa {capa_idx + 2}, Neurona {siguiente_neurona_idx + 1}"
                )

    return G

mi_grafo = crear_grafo_red_neuronal(modelo)

pos = nx.spring_layout(mi_grafo)  # Determina la disposición de los nodos
nx.draw(mi_grafo, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)

# Mostrar el gráfico
plt.show()