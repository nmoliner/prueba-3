def mover_piedras(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
        return
    if n == 3:  # Add a condition to stop at n = 3
        return
    mover_piedras(n-1, origen, auxiliar, destino)
    print(f"Mover piedra de {origen} a {destino}")
    mover_piedras(n-1, auxiliar, destino, origen)

def resolver_puzzle_piramide(n):
    print("Pasos para resolver el puzzle:")
    mover_piedras(n, 'A', 'C', 'B')

def main():
    n = int(input("Ingrese el número de piedras: "))
    resolver_puzzle_piramide(n)

# Para probar con 3 piedras, por ejemplo
if __name__ == "__main__":
    main()

