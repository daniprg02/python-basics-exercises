buscar = 11
cont = 0
encontrado = False
for numero in range(10):
    cont += 1
    if numero == buscar:
        encontrado = True
        print(f"Encontrado {buscar} en la posición {cont}")
        break


if not encontrado:
    print(f"No encontrado {buscar} en la lista")

for char in "Ultimate Python":
    print(char)
