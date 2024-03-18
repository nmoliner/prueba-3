class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nave: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"


naves = [
    NaveEspacial("Estrella Brillante", 50, 10, 100),
    NaveEspacial("Cometa Veloz", 70, 8, 120),
    NaveEspacial("Titán del Cosmos", 90, 15, 150),
    NaveEspacial("GX-1000", 60, 5, 80),
    NaveEspacial("Voyager", 40, 4, 60),
    NaveEspacial("Galaxia Suprema", 80, 12, 200),
    NaveEspacial("Estrella del Norte", 55, 9, 130),
]

# 1. Ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente
naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
print("Naves ordenadas:")
for nave in naves_ordenadas:
    print(nave)

# 2. Mostrar toda la información de las naves "Cometa Veloz" y "Titán del Cosmos"
print("\nInformación de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
for nave in naves:
    if nave.nombre == "Cometa Veloz" or nave.nombre == "Titán del Cosmos":
        print(nave)

# 3. Determinar las cinco naves con mayor cantidad de pasajeros
top_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
print("\nLas cinco naves con mayor cantidad de pasajeros:")
for nave in top_pasajeros:
    print(nave)

# 4. Indicar la nave que requiere la mayor cantidad de tripulación
nave_mayor_tripulacion = max(naves, key=lambda x: x.tripulantes)
print("\nLa nave que requiere la mayor cantidad de tripulación:")
print(nave_mayor_tripulacion)

# 5. Mostrar todas las naves cuyo nombre comience con "GX"
naves_con_gx = [nave for nave in naves if nave.nombre.startswith("GX")]
print("\nNaves cuyo nombre comienza con 'GX':")
for nave in naves_con_gx:
    print(nave)

# 6. Listar todas las naves que pueden llevar seis o más pasajeros
naves_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
print("\nNaves que pueden llevar seis o más pasajeros:")
for nave in naves_seis_pasajeros:
    print(nave)

# 7. Mostrar toda la información de la nave más pequeña y la más grande
nave_mas_pequena = min(naves, key=lambda x: x.longitud)
nave_mas_grande = max(naves, key=lambda x: x.longitud)
print("\nLa nave más pequeña:")
print(nave_mas_pequena)
print("\nLa nave más grande:")
print(nave_mas_grande)
