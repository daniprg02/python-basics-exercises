# Funciones en Python
# Si ponemos = en un parámetro, le estamos dando un valor por defecto
# Si no le pasamos un valor al llamar a la función, tomará el valor por defecto de ese parámetro


def hola(nombre, apellido="Encantado de verte"):  # nombre es el parámetro
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


# Los dos espacios de indentación son necesarios según PEP8 como estándar de Python
hola("Daniel", "Pérez")  # Daniel es el argumento
hola("Ana")
hola("Luis", "Martínez")


hola(
    apellido="Rodríguez", nombre="María"
)  # Llamada a la función con argumentos nombrados
