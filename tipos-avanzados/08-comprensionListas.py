usuarios = [["Dani", 4], ["Felipe", 5], ["Alba", 1]]

nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Esta segunda opción de sacar elementos de la listas, en el primer parámetro se la pasa la expresión que vamos a iterar
# segundo lugar donde lo vamos a guardar, y tercero qué lista vamos a utilizar, más elegante que la versión anterior comentada

# Filter y map de primera forma:

# map
# nombres = [usuario[0] for usuario in usuarios]

# Filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# #Filter y map de segunda forma:

# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# nombres = list(map(lambda usuario: usuario[0], usuarios))

# utilizando filter, si returna True lambda si retorna lo expresado
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
