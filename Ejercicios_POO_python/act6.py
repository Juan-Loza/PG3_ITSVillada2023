class familia:
    def __init__(self):
        self.padre=input("Nombre del Padre:")
        self.madre=input("Nombre de la Madre:")
        
        self.n_hijos=int(input("Cuantos hijos tienen:"))
        self.hijos=[]
        for i in range(self.n_hijos):
            hijo=input("como se llama tu hijo:")
            self.hijos.append(hijo)

    def __str__(self) -> str:
        hijos_str = ', '.join(self.hijos)
        return f"Padre: {self.padre}, Madre: {self.madre}, Hijos: {hijos_str}"


familia1=familia()
print(familia1)
