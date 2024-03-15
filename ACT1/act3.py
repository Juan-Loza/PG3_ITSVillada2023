def funcion(ancho,alto): 
    for i in range(alto):
        for j in range(ancho):
            print("A", end=" ")
        print()
ancho = int(input("ancho:"))
alto = int(input("alto:"))

funcion(ancho,alto)