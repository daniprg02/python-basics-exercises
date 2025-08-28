numeros = [1, 2, 3]
print(numeros)
letras = ["a", "b", "c"]
print(letras)
palabras = ["Hola", 1, "o"]
print(
    palabras
)  # A diferencia de Java, esta es una lista donde puede almacenar diferentes tipos de datos, parecido a un Array
# Aquí llamado listas
booleans = [True, False, True]
print(booleans)

matriz = [[0, 1], [1, 0]]
print(matriz)

ceros = [0] * 10  # Se pueden hacer operaciones con las listas
print(ceros)

alfanumerico = numeros + letras
print(alfanumerico)

rango = []  # Lista vacía
print(rango)

rango2 = list(
    range(1, 11)
)  # Se le deben de pasar parámetros iterables y con range podemos especificar los valores iniciales y finales
print(rango2)

chars = list("Hola mundo")  # Un String es iterable
print(chars)
