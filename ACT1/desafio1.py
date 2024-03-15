def dibujar_forma(ancho, alto, forma):
    if forma == "cuadrado":
        for i in range(alto):
            for j in range(ancho):
                print("A", end=" ")
            print()
    elif forma == "triangulo":
        for i in range(alto):
            for j in range(i + 1):
                print("A", end=" ")
            print()

ancho = int(input("Ancho: "))
alto = int(input("Alto: "))
forma = input("Forma (cuadrado/triangulo): ")

dibujar_forma(ancho, alto, forma)
