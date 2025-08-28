numeros = [2, 4, 6, 8, 10, 12, 14, 99, 120, 2220, 1, 0]

numeros.sort(reverse=True)  # Ordena descendente
print(numeros)

numeros2 = sorted(numeros, reverse=True)  # Ordena y lo devuelve en una nueva lista
print(numeros2)

usuarios = [["Dani", 4], ["Felipe", 5], ["Alba", 1]]


# def ordenar(elemento):
#     return elemento[1]

# Se puede utilizar la expresión lambda cuando una función como la anterior sólo la vamos a ejecutar 1 vez, es mala práctica
# si la escribieramos en exceso cuando podemos utilizar las funciones

usuarios.sort(
    key=lambda elem: elem[1]
)  # El método sort no puede ordenar por ID si va a l final del arreglo, por eso la función ordenar, para que tome el segundo valor disponible

print(usuarios)
