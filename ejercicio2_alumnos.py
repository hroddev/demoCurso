""" En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. """

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def printName(self):
        print("Hola", self.nombre)

    def printNote(self):
        if self.nota < 69:
            print("No ha aprobado su prueba,", self.nota)
        else:
            print("A aprobado su prueba,", self.nota)

alumno1 = Alumno("Hector", 100)
alumno1.printName()
alumno1.printNote()

    
