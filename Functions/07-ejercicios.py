def eliminaEspacios(texto):
    return texto.replace(" ", "")


def es_palindromo(texto):
    texto = eliminaEspacios(texto)
    texto = texto.lower()
    alreves = ""

    for letras in texto:
        alreves = letras + alreves

    return alreves == texto


print(es_palindromo("Amo La Paloma"))


# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palidromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola Mundo", es_palindromo("Hola Mundo"))
