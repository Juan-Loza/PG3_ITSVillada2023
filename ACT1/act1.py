def funcion(numero_buscado,i,lista):
    for i in range(len(lista)):
        if lista[i]==numero_buscado:
            print("El índice de", lista[i], "se encuentra en",i )
        else:
            i+=1
    
i=0
lista=[8,12,9,45]
print(lista, "Elige un numero de la lista")
numero_buscado=int(input("---"))
funcion(numero_buscado,i,lista)