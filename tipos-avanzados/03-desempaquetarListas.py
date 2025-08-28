numeros = [1, 2, 3, 4, 5, 6, 7]

# Se pueden acceder a los distintos elementos de la lista con * y las variables correspondientes
primero, segundo, *otros, ultimo = numeros

print(primero, segundo, ultimo, otros)


# Ejemplo de por qué funciona el código de arriba, se toman todos los valores
# que están en el * menos el primero en el caso anterior y se empaquetan en una lista
# def n(*numeros):
#     for numero in numeros:
#         print(numero)


# n(1, 2, 3, 8, 7)

# print(n)
