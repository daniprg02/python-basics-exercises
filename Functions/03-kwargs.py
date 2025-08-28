def get_product(
    **datos,
):  # La función acepta un número variable de argumentos nombrados, pasan a ser un diccionario
    print(datos["nombre"], datos["id"])


get_product(id=1, nombre="Camisa")  # Llamada a la función con argumentos nombrados
get_product(
    id=2, nombre="Pantalón", precio=15.99, talla="M"
)  # Llamada a la función con más argumentos nombrados
