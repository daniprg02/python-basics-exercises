# set significa grupo o conjunto
# Elimina directamente los repetidos
primero = {1, 2, 3}
# print(primero)
# primero.add(5)
# primero.remove(1)
# print(primero)

# Podemos crear una lista [] y añadirla a un set {}
segundo = [3, 4, 5, 5]
segundo = set(segundo)
# print(segundo)

# # Puede unir set mediante union, eliminando los duplicados
# print(primero | segundo)

# # Mediante intersección se pueden unir los que coincidan en ambos sets
# print(primero & segundo)

# Diferencia, quita los elementos mostrando los de la izquierda, y quitando los de la derecha
# Si hay un 3 en la derecha y no en el primero, lo dejaría
print(primero - segundo)

# Diferencia simétrica, devuelve los elementos que estén en el primero y segundo pero no los duplicados en ambas listas
# aunque no se repitan
print(primero ^ segundo)

# No podemos preguntar directamente al set, pero si hacer este if por ejemplo:
if 5 in segundo:
    print("Hola Mundo")
