def main():

    usuarios = listarUsuario()

    for usuario in usuarios:
        print(f"Usuario: {usuario}")

def listarUsuario():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close
    usuarios = []
    for i in range(0, len(datos)):
        if datos[i][0] == '_':
            continue

        usuarios.append(datos[i].split(":")[0])

    return usuarios


if __name__ == '__main__':
    main()
