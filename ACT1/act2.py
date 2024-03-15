def bisiesto(anio):
    if anio % 400 == 0:
        print("El año", anio, "es bisiesto")
    elif anio % 100 == 0:
        print("El año", anio, "no es bisiesto")
    elif anio % 4 == 0:
        print("El año", anio, "es bisiesto")
    else:
        print("El año", anio, "no es bisiesto")

anio = int(input("Escribe un año y te digo si es bisiesto: "))
bisiesto(anio)