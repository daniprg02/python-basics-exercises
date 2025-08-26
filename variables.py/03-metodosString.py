animal = "  Wetan de los andes  "
print(animal.upper())
print(animal.lower())
print(animal.title())  # primera letra de cada palabra en mayúscula
print(animal.count("a"))  # cuántas veces aparece la letra "a"
print(animal.strip().capitalize())  # elimina espacios al inicio y al final
# Se puede encadenar métodos para en este caso eliminar espacios y luego capitalizar
print(animal.capitalize())  # primera letra en mayúscula
print(animal.lstrip())  # elimina espacios al inicio
print(animal.rstrip())  # elimina espacios al final
print(
    animal.find("9")
)  # posición donde inicia la subcadena "we", -1 si no la encuentra
print(animal.replace("a", "4"))  # reemplaza "a" por "4"
print("Wetan" in animal)  # True si "Wetan" está en la variable animal
print("wetan" in animal)  # False, no es lo mismo "W"
