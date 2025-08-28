# Los elementos se pasan como argumentos con * con cualquier iterable y ** para diccionarios
lista = [1, 2, 3, 4]
# print(lista)
# print(*lista)

lista2 = [5, 6]

combinada = [*lista, *lista2]

print(combinada)


punto1 = {"x": 19}
punto2 = {"y": 20}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
