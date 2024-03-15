class triangulo:
    def inicializar(self,ladoA,ladoB,ladoC):
        self.lado_1=ladoA
        self.lado_2=ladoB
        self.lado_3=ladoC

    def printear_lado_mayor(self):
        if self.lado_1>self.lado_2 and self.lado_1>self.lado_3 :
            print("el valor del lado mayor es ",self.lado_1)
        elif self.lado_1<self.lado_2 and self.lado_2>self.lado_3:
            print("el valor del lado mayor es ",self.lado_2)
        else:
            print("el valor del lado mayor es ",self.lado_3)

    def equilatero(self):
        if self.lado_1==self.lado_2 & self.lado_1==self.lado_3:
            print("Es equilatero")
        else:
            print("No es equilatero")


triangulo1=triangulo()
triangulo1.inicializar(25,25,25)
triangulo1.printear_lado_mayor()
triangulo1.equilatero()


    