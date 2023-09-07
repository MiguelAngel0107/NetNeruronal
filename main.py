from Graficador.graficador import Graficador
from Model.model import ModeloNeuronal
import tkinter as tk


def main():
    ventana = tk.Tk()

    radio_circular_inputs = 25
    radio_circular_hidden = 25
    espaciado_x = 280
    espaciado_y = 100

    # Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
    modelo = ModeloNeuronal(capa_entrada=[0.3, 0.7, 0.5], capas_ocultas=[
                            2, 2], num_salidas=1)

    graficador = Graficador(ventana, radio_circular_inputs,
                            radio_circular_hidden, espaciado_x, espaciado_y, modelo)
    graficador.create_graphics()

    def up() -> None:
        graficador.update_graphics()

    boton = tk.Button(ventana, text="Clic aquí",
                      bg="white", command=up)
    boton.pack(padx=20, pady=20)

    ventana.mainloop()


if __name__ == "__main__":
    main()
