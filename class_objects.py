class Toys:
    _turnStatus = False

    def turnOn(self):
        self._turnStatus = True

    def turnOff(self):
        self._turnStatus = False

    def isTurnOn(self):
        return self._turnStatus


class Potato(Toys):

    def removeEar(self):
        print("Quitar oreja")

    def putEar(self):
        print("Poner oreja")


p = Potato()
p.turnOn()
print(p.isTurnOn())


class Dino(Toys):
    color = None
    name = None

    def __init__(self) -> None:
        super().__init__()
        self.color = "Verde"
        self.name = "T-rex"

d = Dino()

print(d.color)
