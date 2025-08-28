# Es lo mismo que la listas, pero no se pueden modificar, eliminar o agregar, se pueden crear nuevas en base a otras

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Se puede crear una tupla con elementos iterables
punto = tuple([1, 2])
print(punto)

# No modifica la tubla, simplemente guardo sus valores en una nueva lista
menosNumeros = numeros[:2]
print(menosNumeros)

# Desempaquetar
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Iterar las tuplas

for n in numeros:
    print(n)


listaNumeros = list(numeros)
listaNumeros[0] = ["Hola"]

# Se puede modificar la lista, pero la tupla sigue intacta
# Esto daría error: numeros[0] = 5
print(numeros)
print(listaNumeros)
