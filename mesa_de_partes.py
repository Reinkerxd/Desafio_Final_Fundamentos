""" Programa de Mesa de Partes """


# 1. REGISTRAR UN EXPEDIENTE
def registrar_expediente():
    """ Función para registrar expedientes """

    print("\n--- REGISTRO DE EXPEDIENTE ---")

    while True:
        try:
            dni = input("Ingrese DNI de 8 digitos: ")

            if len(dni) != 8 or not dni.isdigit():
                print("Error: el DNI debe tener 8 digitos.")
            else:
                break
        except ValueError:
            print("Error: el DNI debe ser un numero.")

    while True:
        try:
            nombres = input("Ingrese nombres y apellidos: ")

            if nombres == "":
                print("Error: los nombres son obligatorios.")
            else:
                break
        except ValueError:
            print("Error: Nombres deben ser una cadena de texto.")

    while True:
        try:
            print("\nTipos de tramite:")
            print("1. Solicitud")
            print("2. Licencia")
            print("3. Reclamo")

            opcion = int(input("Seleccione el tipo de tramite: "))

            match opcion:
                case 1:
                    tipo = "Solicitud"
                    break
                case 2:
                    tipo = "Licencia"
                    break
                case 3:
                    tipo = "Reclamo"
                    break
                case _:
                    print("Error: opcion invalida.")
        except ValueError:
            print("Error: opcion invalida.")

    while True:
        try:
            asunto = input("Ingrese el asunto: ")

            if asunto == "":
                print("Error: el asunto es obligatorio.")
            else:
                break
        except ValueError:
            print("Error: el asunto debe ser una cadena de texto.")

    while True:
        try:
            folios = int(input("Ingrese el numero de folios: "))

            if folios <= 0:
                print("Error: los folios deben ser positivos.")
            else:
                break
        except ValueError:
            print("Error: los folios deben ser un numero entero positivo.")

    # Crear el expediente
    archivo = open("Expedientes.txt", "a", encoding="utf-8")
    archivo.write(f"{dni}, {nombres}, {tipo}, {asunto}, {folios}\n")
    archivo.close()


# 2. AGREGAR EXPEDIENTE A LA LISTA EXPEDIENTES
def agregar_expediente():
    """ Función que agrega expedientes a la lista de expedientes """
    expedientes = []
    with open("Expedientes.txt", "r", encoding="utf-8") as archivo:
        for data in archivo:
            expediente = data.strip().split(',')
            expedientes.append(expediente)
    return expedientes


# 3. MOSTRAR LOS DATOS DE UN EXPEDIENTE
def mostrar_expediente(expediente):
    """ Función para mostrar los datos de los expedientes """

    print("\n--------------------------------")
    print("DNI:", expediente[0])
    print("Nombres:", expediente[1])
    print("Tipo:", expediente[2])
    print("Asunto:", expediente[3])
    print("Folios:", expediente[4])
    print("--------------------------------")


# 4. MOSTRAR TODOS LOS EXPEDIENTES
def listar_expedientes():
    """ Función para listar los expedientes """
    lista = agregar_expediente()

    if len(lista) == 0:
        print("\nERROR: No hay expedientes registrados")
    else:
        print("\n==== LISTADO DE EXPEDIENTES ====")

        for expediente in lista:
            mostrar_expediente(expediente)


# 5. MENU PRINCIPAL
def menu():
    """ Función para ejecutar el menú del programa """

    while True:
        try:
            print("\n==================================")
            print(" SISTEMA DE MESA DE PARTES")
            print("==================================")
            print("1. Registrar expediente")
            print("2. Mostrar expedientes")
            print("3. Salir")
            print("==================================")

            opcion = int(input("Seleccione una opcion: "))

            match opcion:
                case 1:
                    registrar_expediente()
                case 2:
                    listar_expedientes()
                case 3:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Error: opcion invalida.")
        except ValueError:
            print("Error: opcion invalida.")


# INICIO DEL PROGRAMA
menu()
