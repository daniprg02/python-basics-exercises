def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(
        f"La suma es: {resultado}"
    )  # Importante la identación, si se llega a dejar a la misma altura que el for, el print ejecutará muchas veces


suma(5, 3)  # Llamada a la función con argumentos posicionales
suma(10, 20, 30, 40, 50)  # Llamada a la función con múltiples argumentos
suma(
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
)  # Llamada a la función con muchos argumentos, estos pasan a ser iterables
suma()  # Llamada a la función sin argumentos
