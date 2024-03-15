def funcion(numero):
    numero_str = str(numero)
    longitud = len(numero_str)
    
    for i in range(longitud - 1):  
        digito_actual = int(numero_str[i])
        digito_siguiente = int(numero_str[i + 1])
        
        if abs(digito_actual - digito_siguiente) != 1:
            return False
    
    return True

numero=int(input("Ingresa el numero step:"))
print(funcion(numero))