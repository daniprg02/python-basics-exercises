mascotas = ["Darky", "Ciri", "Pelusa", "Nisky", "Darky"]

# if "Lilu" in mascotas:               Esta linea se añade si no queremos que arroje error a no encontrar algo en la lista, en Python hay que manejar este error
# Python no devuelve -1 como en otros lenguajes de programación


print("La mascota se encuentra en el índice: ", mascotas.index("Nisky"))
print("La mascota aparece en la lista: ", mascotas.count("Darky"), "veces")
