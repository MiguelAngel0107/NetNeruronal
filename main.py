import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk

from Model.model import ModeloNeuronal
radio_circular_inputs = 25
radio_circular_hidden = 25
espaciado_x = 240
espaciado_y = 100


# Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
modelo = ModeloNeuronal(capa_entrada=[0.3, 0.7, 0.5], capas_ocultas=[
                        2, 2], num_salidas=1)


def graphicsNetNeuronal(model):
    for j, inputs in enumerate(model.getDataInput()):
        dibujar_circulo(radio_circular_inputs*2,
                        j*espaciado_y + espaciado_y, radio_circular_inputs,
                        str(f'{inputs}'), 'green')

    for i, layer in enumerate(model.capas):
        for j, neurona in enumerate(layer.neuronas):
            dibujar_circulo((i*espaciado_x+espaciado_x)  # Espacio para la capa de entrada
                            + (radio_circular_inputs*2),
                            (j*espaciado_y+espaciado_y),
                            radio_circular_hidden, str(f'{neurona.output():.4f}'))

    for i, layer in enumerate(model.capas):
        #print('Capas numero:', i)
        pesosLayer = layer.getDicPesos()
        for j, forLayer in enumerate(pesosLayer):
            #print('Capa de Pesos:', j)
            for k, peso in enumerate(forLayer):
                #print('coordenadas: \n x1 -> ', i*espaciado_x + espaciado_x, '\n x2 -> ', i*espaciado_x + espaciado_x +
                #      10, '\n y1 -> ', (k*espaciado_y + espaciado_y), '\n y2 -> ', (j*espaciado_y + espaciado_y+espaciado_y))
                dibujar_linea(((i*espaciado_x+espaciado_x)+ (radio_circular_inputs*2))-espaciado_x,
                              (k*espaciado_y + espaciado_y),
                              ((i*espaciado_x+espaciado_x)+ (radio_circular_inputs*2)),
                              (j*espaciado_y + espaciado_y),
                              f'{peso:.4f}')

# Función para dibujar un círculo con texto


def dibujar_circulo(x, y, radio, texto, color='blue'):
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color)
    canvas.create_text(x, y, text=texto, fill="white")

# Función para dibujar una línea con texto


def dibujar_linea(x1, y1, x2, y2, texto):
    canvas.create_line(x1, y1, x2, y2, fill="red")
    medio_x = (x1 + x2) / 2
    medio_y = (y1 + y2) / 2
    canvas.create_text(medio_x, medio_y, text=texto, fill="black")


def dibujar_linea_vertical(x, y1, y2, texto):
    canvas.create_line(x, y1, x, y2, fill="red")
    medio_y = (y1 + y2) / 2
    canvas.create_text(x, medio_y, text=texto, fill="black")


# Crear una ventana
ventana = tk.Tk()
ventana.title("Dibujar Figuras")

# Crear un lienzo (canvas) en la ventana
canvas = tk.Canvas(ventana, width=1500, height=800)
canvas.pack()

graphicsNetNeuronal(modelo)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
