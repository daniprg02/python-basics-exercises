# numero = 1
# while numero <= 10:
#     print(numero)
#     numero += 1  # Equivalente a numero = numero + 1
# print("Fin del bucle")
# Evitar bucles infinitos
# Ctrl + C para salir de un bucle infinito

# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print("comando:", comando)

#     if comando.lower() == "salir":
#         print("Adiós")
#         break

# Como terminar un bucle infinito
while True:
    comando = input("$ ")
    print("comando:", comando)

    if comando.lower() == "salir":
        print("Adiós")
        break
