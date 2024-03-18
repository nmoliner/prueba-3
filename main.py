import sys
from PiedraMover import PiedraMover
from Matrix import Matrix
from NaveEspacial import NaveEspacial
from Polynomial import Polynomial

def main():
    while True:
        ejercicio = input("Ingrese el número del ejercicio que desea ejecutar (1, 2, 3 o 4), o 0 para salir: ")

        if ejercicio == "0":
            sys.exit()
        elif ejercicio == "1":
            PiedraMover()
        elif ejercicio == "2":
            Matrix()
        elif ejercicio == "3":
            NaveEspacial()
        elif ejercicio == "4":
            Polynomial()
        else:
            print("Ejercicio inválido")

if __name__ == "__main__":
    main()
