saludo = "Hola global"  # Variable global (mala práctica según PEP8)
# una función puede cambiar el tipo de una variable global, pero no es recomendable


def saludar():
    global saludo
    saludo = "Hola"
    return saludo


def saludaConEducacion():
    saludo = "Hola, ¿cómo estás?"
    return saludo


print(saludar())  # Error, la variable saludo no está definida en este ámbito
print(saludo)  # Accede a la variable global
print(saludaConEducacion())
