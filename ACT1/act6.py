def funcion(frase):
    vocales = {'a', 'e', 'i', 'o', 'u'}
    frase = frase.lower()
    contador_vocales = 0
    for caracter in frase:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales

frase = input("frase: ")
cantidad_vocales = funcion(frase)
print("cantidad de vocales:", cantidad_vocales)