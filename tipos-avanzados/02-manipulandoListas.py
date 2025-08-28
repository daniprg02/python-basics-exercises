mascotas = ["Darky", "Ciri", "Pelusa", "Nisky"]
print(mascotas[0])
mascotas[0] = "DarkyBonito"
print(mascotas)
print(mascotas[0:3])
print(
    mascotas[:3]
)  # Si no se especifica el índice, se toma por defecto el primer elemento de la lista
print(
    mascotas[0:]
)  # Si no se especifica el último valor, se toma por defecto el último elemento de la lista
print(mascotas[-1])  # Empieza desde el final de la lista
print(
    mascotas[::2]
)  # De esta forma cogería los pares, va saltando un elemento y toma el siguiente de la lista

print(
    mascotas[1::2]
)  # De esta forma toma el valor 1 de la lista, se salta el siguiente y toma el tercero de la lista


numeros = list(range(21))
print(numeros[1::2])  # Toma los impares específicando el índice

numeros = list(range(1, 21))
print(numeros[::2])  # Toma los impares especificándolo en rango

numeros = list(range(21))
print(numeros[0::2])  # Toma los pares específicando el índice

numeros = list(range(0, 21))
print(numeros[::2])  # Toma los pares especificándolo en rango
