while True:
    print("\n¿Qué desea hacer?")
    print("1 - Escribir")
    print("2 - Salir")
    opcion = input("Seleccione una opción: ")
    if opcion=="1":
        texto=input("Escriba aqui:")
        try:
             with open("archivo.txt", "w") as archivo:
                    archivo.write(texto)
        except TypeError as e:
                print("Se produjo un error:", e)

    elif opcion=="2":
          break