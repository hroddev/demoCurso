
countries = set()

menu = ""

while menu != "9":
    menu = input("Elija una opcion:\n1. Ingrese un pais\n2. Muestrar paises ingresados\n9. Salir\n: ")
    if menu == "1":
        add_country = input("Ingrese el nombre del pais: ")
        countries.add(add_country)
        continue
    if menu == "2":
        set_sorted = sorted(countries)
        print(set_sorted)
        continue
    if menu == "9":
        print("salir")
    else:
        print("Opcion no esta disponible")
        continue
