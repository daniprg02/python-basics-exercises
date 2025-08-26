# nombre = ""

# print("¿Cuál es tu nombre? ")
# nombre = input()
# print("Hola " + nombre)
nombre = "Ultimate Python"
descripcion = """
Este curso contempla todos los detalles
necesarios para convertirte en un experto"""

if " " in nombre:  # si contiene al menos un espacio
    print(nombre + " contiene espacios")
else:
    print("No contiene espacios")
