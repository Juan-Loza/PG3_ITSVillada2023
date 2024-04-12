print("Vamos a hacer una división")
while True:
    print("\n¿Qué desea hacer?")
    print("1 - Hacer una división")
    print("2 - Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            n1 = int(input("Escriba su primer valor: "))
            n2 = int(input("Escriba su segundo valor: "))
            resultado = n1 / n2              
            print(f"El resultado es: {resultado}")
        except (ZeroDivisionError, ValueError):
            print("Por favor, ingrese números válidos. No se puede dividir por cero o ingrese un número entero.")
        continue  
    elif opcion == "2":
        break
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
