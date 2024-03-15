class Alumno:
    def inicializar(self,nom,no):
        self.nombre=nom
        self.nota=no
    def imprimir(self):
        print("Nombre:",self.nombre,"Nota:",self.nota)
        self.aprobar()
    def aprobar(self):
        if self.nota>=6:
            print("Regular")
        elif self.nota<=6:
            print("No Regular")


Alumno1=Alumno()
Alumno1.inicializar("Pepito",8)
Alumno1.imprimir()


Alumno2=Alumno()
Alumno2.inicializar("Maria",5)
Alumno2.imprimir()