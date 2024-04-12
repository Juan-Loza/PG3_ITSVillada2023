meses = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")
while True:
    try:
        num_mes = int(input("Número del mes: "))
        print("El mes es:")
        print(meses[num_mes -1])

    except IndexError:
        print("Ese mes no existe")
        continue