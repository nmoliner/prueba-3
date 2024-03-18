
class PiedraMover:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def mover_piedra(self):
        if not self.destino or self.origen[-1] < self.destino[-1]:
            piedra = self.origen.pop()
            self.destino.append(piedra)
            print(f"Se movió una piedra de tamaño {piedra} de la columna de origen a la columna de destino.")
        else:
            print("No se puede mover la piedra debido a las restricciones.")

# Crear las columnas
columna_origen = list(range(1, 75))  # Columna de origen con 74 piedras
columna_destino = []

# Crear una instancia de la clase PiedraMover
piedra_mover = PiedraMover(columna_origen, columna_destino)

# Trasladar las piedras de la columna de origen a la columna de destino
while piedra_mover.origen:
    piedra_mover.mover_piedra()

print("Se han trasladado todas las piedras a la columna de destino.")

if __name__ == "__main__":
    # Aquí va el código que quieres ejecutar cuando se ejecute el archivo directamente
    pass
