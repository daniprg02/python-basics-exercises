n1 = input("Ingrese el primer numero: ")
n2 = input("Ingrese el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""Para los numeros {n1} y {n2}
la suma es {suma}
la resta es {resta}
la multiplicacion es {multiplicacion}
la division es {division}"""

print(mensaje)

# Recordar poner la f al inicio de la cadena para que reconozca las variables
# Las tres comillas permiten hacer saltos de linea sin usar \n
# El input siempre devuelve un string, por eso hay que convertir a int o float si se quieren hacer operaciones matematicas
# En Python no es necesario declarar el tipo de variable, se infiere automaticamente
