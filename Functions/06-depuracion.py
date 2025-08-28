def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado  # La función devuelve el valor de resultado, si está mal identado, el return se ejecuta una vez pero termina la función


print("Depuración de código")
l = largo("Hola mundo")  # Llamada a la función con un argumento
print(l)
