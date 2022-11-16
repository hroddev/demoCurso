def writeFile(file, data):
    f = open(file, 'w')
    for line in data:
        if not line.endswith('\n'):
            line += "\n"
        f.write(line)
    f.close

def readFile(file):
    f = open(file, 'r')
    data = f.read()
    print(data)
    f.close

lineas = ["info de relleno 1", "info de relleno 2",
          "info de relleno 3"]

writeFile("archivo.txt", lineas)
readFile("archivo.txt")
readFile("archivo.txt")
