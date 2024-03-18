import sys

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    # Añade métodos para operaciones con matrices según sea necesario


class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    # Añade métodos para operaciones con naves espaciales según sea necesario


class PiedraMover:
    def __init__(self):
        # Añade atributos y métodos para mover piedras según sea necesario
        pass


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    # Añade métodos para operaciones con polinomios según sea necesario


def main():
    while True:
        ejercicio = input("Ingrese el número del ejercicio que desea ejecutar (1, 2 o 3), o 0 para salir: ")
        
        if ejercicio == "0":
            sys.exit()
        elif ejercicio == "1":
            # Lógica del ejercicio 1
            matrix = Matrix(3, 3)
            print("Matriz creada:", matrix.data)
        elif ejercicio == "2":
            # Lógica del ejercicio 2
            nave = NaveEspacial("Estrella Brillante", 50, 10, 100)
            print("Nave espacial creada:", nave.nombre)
        elif ejercicio == "3":
            # Lógica del ejercicio 3
            piedra_mover = PiedraMover()
            print("PiedraMover creado")
        else:
            print("Ejercicio inválido")

if __name__ == "__main__":
    main()
