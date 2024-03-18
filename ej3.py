# Definición de la lista de naves espaciales (nombre, longitud, tripulantes, pasajeros)
naves = [
    {"nombre": "Estrella Brillante", "longitud": 50, "tripulantes": 10, "pasajeros": 100},
    {"nombre": "Cometa Veloz", "longitud": 70, "tripulantes": 8, "pasajeros": 120},
    {"nombre": "Titán del Cosmos", "longitud": 90, "tripulantes": 15, "pasajeros": 150},
    {"nombre": "GX-1000", "longitud": 60, "tripulantes": 5, "pasajeros": 80},
    {"nombre": "Voyager", "longitud": 40, "tripulantes": 4, "pasajeros": 60},
    {"nombre": "Galaxia Suprema", "longitud": 80, "tripulantes": 12, "pasajeros": 200},
    {"nombre": "Estrella del Norte", "longitud": 55, "tripulantes": 9, "pasajeros": 130},
]

# 1. Ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente
naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))
print("Naves ordenadas:")
for nave in naves_ordenadas:
    print(nave)

# 2. Mostrar toda la información de las naves "Cometa Veloz" y "Titán del Cosmos"
print("\nInformación de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
for nave in naves:
    if nave["nombre"] == "Cometa Veloz" or nave["nombre"] == "Titán del Cosmos":
        print(nave)

# 3. Determinar las cinco naves con mayor cantidad de pasajeros
top_pasajeros = sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5]
print("\nLas cinco naves con mayor cantidad de pasajeros:")
for nave in top_pasajeros:
    print(nave)

# 4. Indicar la nave que requiere la mayor cantidad de tripulación
nave_mayor_tripulacion = max(naves, key=lambda x: x["tripulantes"])
print("\nLa nave que requiere la mayor cantidad de tripulación:")
print(nave_mayor_tripulacion)

# 5. Mostrar todas las naves cuyo nombre comience con "GX"
naves_con_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]
print("\nNaves cuyo nombre comienza con 'GX':")
for nave in naves_con_gx:
    print(nave)

# 6. Listar todas las naves que pueden llevar seis o más pasajeros
naves_seis_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]
print("\nNaves que pueden llevar seis o más pasajeros:")
for nave in naves_seis_pasajeros:
    print(nave)

# 7. Mostrar toda la información de la nave más pequeña y la más grande
nave_mas_pequena = min(naves, key=lambda x: x["longitud"])
nave_mas_grande = max(naves, key=lambda x: x["longitud"])
print("\nLa nave más pequeña:")
print(nave_mas_pequena)
print("\nLa nave más grande:")
print(nave_mas_grande)
