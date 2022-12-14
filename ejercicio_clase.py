""" 
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color
Ruedas
Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola. 
"""


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def printColor(self):
        print("El vehiculo es color", self.color)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

toyota = Coche("Blanco", 4, 4, 210, 8)
toyota.printColor()
toyota.color = "Rojo"
toyota.printColor()

nissan = Coche("Negro", 4, 2, 260, 8)
print(nissan.cilindrada)


