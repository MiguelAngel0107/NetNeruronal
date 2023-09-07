from Graficador.graficador import Graficador
from Model.model import ModeloNeuronal

def main():
    radio_circular_inputs = 25
    radio_circular_hidden = 25
    espaciado_x = 280
    espaciado_y = 100

    # Crear un modelo neuronal con 2 entradas, 2 capas ocultas de 3 neuronas cada una y 1 salida
    modelo = ModeloNeuronal(capa_entrada=[0.3, 0.7, 0.5], capas_ocultas=[
                            2, 2, 5,6,3,9,8,1,6,2], num_salidas=1)

    graficador = Graficador(radio_circular_inputs, radio_circular_hidden, espaciado_x, espaciado_y, modelo)
    graficador.create_graphics()

if __name__ == "__main__":
    main()
