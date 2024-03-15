class persona:
    def __init__(self):
        self.nombre = input("nombre:")
        self.edad = int(input("edad:"))
        self.imprimir()

    def imprimir(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad}")


class empleado(persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("sueldo: "))
        self.paga_impuestos()

    def imprimir(self):
        super().imprimir()

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


persona1 = persona()
empleado1 = empleado()

