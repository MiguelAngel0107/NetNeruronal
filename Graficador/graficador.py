import tkinter as tk
import math
import random


class Graficador:
    def __init__(self, radio_circular_inputs, radio_circular_hidden, espaciado_x, espaciado_y, model):
        self.radio_circular_inputs = radio_circular_inputs
        self.radio_circular_hidden = radio_circular_hidden
        self.espaciado_x = espaciado_x
        self.espaciado_y = espaciado_y
        self.model = model

        self.ventana = tk.Tk()
        self.ventana.title("Red Neuronal")
        # Cambiar el color del borde de la ventana
        self.ventana.configure(bg='black', bd=2, highlightbackground='white')

        # Crear un lienzo (canvas) en la ventana
        self.canvas = tk.Canvas(self.ventana, width=1500, height=800)
        self.canvas.configure(bg='black', highlightbackground='black')
        self.canvas.pack()
        

    def obtener_color_neurona(self):
        return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def dibujar_circulo(self, x, y, radio, texto, color='#3A1078'):
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color)
        self.canvas.create_text(x, y, text=texto, fill="white")

    def dibujar_linea(self, x1, y1, x2, y2, texto, color='red'):
        self.canvas.create_line(x1, y1, x2, y2, fill=color)

        pendiente = (y2 - y1) / (x2 - x1)
        angulo_radianes = math.atan(pendiente)

        medio_x = (x1 + x2) / 2
        medio_y = (y1 + y2) / 2

        medio_x = (x1 + medio_x) / 2
        medio_y = (y1 + medio_y) / 2

        if x1 <= x2:
            anchor = 'e'  # Anclaje a la izquierda
        else:
            anchor = 'w'  # Anclaje a la derecha

        angulo_grados = math.degrees(angulo_radianes)

        self.canvas.create_text(medio_x, medio_y-8, text=texto, fill="white", angle=-angulo_grados, anchor=anchor)

    def dibujar_linea_vertical(self, x, y1, y2, texto):
        self.canvas.create_line(x, y1, x, y2, fill="red")
        medio_y = (y1 + y2) / 2
        self.canvas.create_text(x, medio_y, text=texto, fill="black")

    def create_graphics(self):
        for i, layer in enumerate(self.model.capas):
            pesos_layer = layer.getDicPesos()
            for j, for_layer in enumerate(pesos_layer):
                color_peso = self.obtener_color_neurona()
                for k, peso in enumerate(for_layer):
                    self.dibujar_linea(((i*self.espaciado_x+self.espaciado_x) + (self.radio_circular_inputs*2))-self.espaciado_x,
                                      (k*self.espaciado_y + self.espaciado_y),
                                      ((i*self.espaciado_x+self.espaciado_x) + (self.radio_circular_inputs*2)),
                                      (j*self.espaciado_y + self.espaciado_y),
                                      f'{peso:.4f}', color_peso)

        for j, inputs in enumerate(self.model.getDataInput()):
            self.dibujar_circulo(self.radio_circular_inputs*2,
                                j*self.espaciado_y + self.espaciado_y, self.radio_circular_inputs,
                                str(f'{inputs}'), 'green')

        for i, layer in enumerate(self.model.capas):
            for j, neurona in enumerate(layer.neuronas):
                self.dibujar_circulo((i*self.espaciado_x+self.espaciado_x) + (self.radio_circular_inputs*2),
                                    (j*self.espaciado_y+self.espaciado_y),
                                    self.radio_circular_hidden, str(f'{neurona.output():.4f}'))
                

        self.ventana.mainloop()