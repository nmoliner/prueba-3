def mover_piedra(origen, destino):
    if not destino or origen[-1] < destino[-1]:
        piedra = origen.pop()
        destino.append(piedra)
        print(f"Se movió una piedra de tamaño {piedra} de la columna de origen a la columna de destino.")
    else:
        print("No se puede mover la piedra debido a las restricciones.")

# Crear las columnas
columna_origen = list(range(1, 75))  # Columna de origen con 74 piedras
columna_destino = []

# Trasladar las piedras de la columna de origen a la columna de destino
while columna_origen:
    mover_piedra(columna_origen, columna_destino)

print("Se han trasladado todas las piedras a la columna de destino.")
