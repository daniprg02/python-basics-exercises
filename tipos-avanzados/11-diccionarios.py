punto = {"x": 25, "y": 50}  # Izquierda String, izquierda cualquier valor
print(punto)

print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

# if para acceder a un valor del diccionario
if "lala" in punto:
    print("encontré lala", punto["lala"])

# método get
print(punto.get("x"))
# devuelve none si no añadimos otro parámetro (97 como ejemplo)
print(punto.get("lala", 97))

# eliminar claves y valor
del punto["x"]
del punto["y"]
print(punto)

punto["x"] = 25

# Acceder a los diccionarios:
for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Daniel"},
    {"id": 2, "nombre": "Alba"},
    {"id": 3, "nombre": "Pepe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
