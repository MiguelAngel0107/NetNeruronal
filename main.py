import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import tkinter as tk

from Model.model import ModeloNeuronal
radio_circular_inputs = 20
radio_circular_hidden = 20
espaciado_x = 50
espaciado_y = 50


# Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
modelo = ModeloNeuronal(capa_entrada=[0.5, 0.7, 0.5], capas_ocultas=[
                        3, 3], num_salidas=6)


def graphicsNetNeuronal(model):
    for j, inputs in enumerate(model.getDataInput()):
        dibujar_circulo(radio_circular_inputs*2, 
                        j*espaciado_y + espaciado_y, radio_circular_inputs, 'Hola')

    for i, layer in enumerate(model.capas):
        print('Capa', i)
        for j, neurona in enumerate(layer.neuronas):
            dibujar_circulo((i*espaciado_x+espaciado_x)+(radio_circular_inputs*2), 
                            (j*espaciado_y+espaciado_y)+(radio_circular_inputs*2),
                            radio_circular_hidden, str(f'{neurona.output():.4f}'))        
    

    pass

# Función para dibujar un círculo con texto


def dibujar_circulo(x, y, radio, texto):
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue")
    canvas.create_text(x, y, text=texto, fill="white")

# Función para dibujar una línea con texto


def dibujar_linea(x1, y1, x2, y2, texto):
    canvas.create_line(x1, y1, x2, y2, fill="red")
    medio_x = (x1 + x2) / 2
    medio_y = (y1 + y2) / 2
    canvas.create_text(medio_x, medio_y, text=texto, fill="black")


# Crear una ventana
ventana = tk.Tk()
ventana.title("Dibujar Figuras")

# Crear un lienzo (canvas) en la ventana
canvas = tk.Canvas(ventana, width=1500, height=800)
canvas.pack()

graphicsNetNeuronal(modelo)

# Dibujar una línea con texto
dibujar_linea(50, 50, 150, 150, "Línea 1")


# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
