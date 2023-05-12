#Herencia
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
class Auto(Vehiculo):

    def desplazamiento(self):
        rueda = 4
        print(f'el {self.marca} auto se esta desplazando sobre ',rueda,' ruedas')

class Moto(Vehiculo):

    def dezplazamiento(self):
        rueda = 2
        print(f'la moto {self.marca} se esta desplazando sobre ',rueda,' ruedas')


Vehiculo1 = Moto('Kawasaki')
Vehiculo1.dezplazamiento()
Vehiculo2 = Auto('Audi')
Vehiculo2.desplazamiento()


#Herencia multiple

class Estudiante:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado


class Materia:
    def __init__(self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion


class Boletin(Estudiante, Materia):
    def mostrar(self):
        print(f" El estudiante {self.nombre} de grado {self.grado} obtuvo la calificacion de {self.calificacion} en la materia {self.materia} ")


Estudiante1 = Estudiante("Pepito perez", 1102)
Materia1 = Materia("Matematicas", 3.2)

Boletin1 = Boletin(Estudiante1, Materia1)
Boletin1.mostrar()