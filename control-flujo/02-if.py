edad = 18
# if edad > 65:
#     print("Tienes un descuento por jubilado")
# elif edad > 18:
#     print("Eres mayor de edad")
# elif edad == 18:
#     print("Tienes 18 años, eres mayor de edad")
# else:
#     print("Eres menor de edad")

mensaje = "es mayor de edad" if edad >= 18 else "es menor de edad"  # Operador ternario
print(mensaje)

# Estructura if, elif, else
# La condición más restrictiva va primero
# La condición else es opcional
# Se pueden agregar múltiples condiciones elif
# La condición if es obligatoria
# No es necesario usar llaves {}
# La identación es obligatoria (4 espacios o tabulación)
# https://docs.python.org/3/tutorial/controlflow.html#if-statements
