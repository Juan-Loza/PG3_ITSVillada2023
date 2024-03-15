palabra=(input("Escribe palabra capicua:"))
def funcion(palabra):
    palabra=palabra.lower()
    palabra2=palabra[::-1]
    if palabra==palabra2:
        return True
    else:
        return False

print(funcion(palabra))