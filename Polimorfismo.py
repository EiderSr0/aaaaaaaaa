#Polimorfismo

class Auto():
    def __init__(self, nombre):
        self.nombre = nombre
    def desplazamiento(self):
        rueda = 4
        print(f'el {self.nombre} auto se esta desplazando sobre ',rueda,' ruedas')

class Moto():
    def __init__(self, nombre):
        self.nombre = nombre
    def dezplazamiento(self):
        rueda = 2
        print(f'la moto {self.nombre} se esta desplazando sobre ',rueda,' ruedas')


Vehiculo1 = Moto('Kawasaki')
Vehiculo1.dezplazamiento()
Vehiculo2 = Auto('Audi')
Vehiculo2.desplazamiento()
    
    