# Generar una pequeña calculadora, hay que verificar si se ha introducido un número
# Si ya ha ingresado un número, se le solicita que ingrese una operación (+, -, *, /) si no lo ha hecho se le pide que lo ingrese
# Ingrese el segundo número, muestra los resultados y se guarda este valor como el primer número, otra vez se le pide que ingrese una operación
# Y se realiza la operación con el segundo número ingresado
# Si se ingresa "salir" en cualquier momento, el programa termina

print("Bienvenido a la calculadora")
print('Para salir escribe "Salir"')
print("Las operaciones son suma, multi, div y resta")

print("Ingresa un número: ")

num1 = input()
if num1.lower() == "salir":
    exit()

while True:
    print("Elige una operación")
    operacion = input()

    if operacion.lower() == "salir":
        break

    print("Elige un segundo número")

    num2 = input()
    comando2 = num2
    if comando2.lower() == "salir":
        break

    if operacion.lower() == "suma":
        resultado = float(num1) + float(num2)
        print("Resultado:", resultado)
        num1 = resultado
    elif operacion.lower() == "multi":
        resultado = float(num1) * float(num2)
        print("Resultado:", resultado)
        num1 = resultado
    elif operacion.lower() == "div":
        resultado = float(num1) / float(num2)
        print("Resultado:", resultado)
        num1 = resultado
    elif operacion.lower() == "resta":
        resultado = float(num1) - float(num2)
        print("Resultado:", resultado)
        num1 = resultado
    else:
        print("Operación no válida. Intenta de nuevo.")
