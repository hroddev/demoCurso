class Cars():
    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas

    def __repr__(self):
        return f"Marca: {self.marca}, Color: {self.color}, Puertas: {self.puertas}"

    def getData(self):
        return f"Marca: {self.marca}\nColor: {self.color}\nPuertas: {self.puertas}"
    
    def writeFile(self, file, data):
        f = open(file, 'w')
        f.write(data)
        f.close

    def readFile(self, file):
        f = open(file, 'r')
        data = f.read()
        print(data)
        f.close


car1 = Cars("Toyota", "Blanco", 4)
car1.writeFile("car1.txt", car1.getData())
car1.readFile("car1.txt")
