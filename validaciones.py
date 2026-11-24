""" Módulo de validaciones: pide los datos al usuario y verifica que sean
correctos """


def pedir_dni():
    """ Pide un DNI hasta que tenga exactamente 8 dígitos """
    while True:
        dni = input("Ingrese DNI de 8 digitos: ").strip()

        if len(dni) != 8 or not dni.isdigit():
            print("Error: el DNI debe tener 8 digitos.")
        else:
            return dni


def pedir_texto(mensaje, mensaje_error):
    """ Pide un texto obligatorio (no vacío). Sirve para nombres y asunto """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print(mensaje_error)
        elif "|" in texto:
            print("Error: no se permite el caracter '|'.")
        else:
            return texto


def pedir_tipo_tramite():
    """ Muestra los tipos de trámite y devuelve el elegido """
    while True:
        try:
            print("\nTipos de tramite:")
            print("1. Solicitud")
            print("2. Licencia")
            print("3. Reclamo")

            opcion = int(input("Seleccione el tipo de tramite: "))

            match opcion:
                case 1:
                    return "Solicitud"
                case 2:
                    return "Licencia"
                case 3:
                    return "Reclamo"
                case _:
                    print("Error: opcion invalida.")
        except ValueError:
            print("Error: opcion invalida.")


def pedir_estado():
    """ Muestra los estados posibles y devuelve el elegido """
    while True:
        try:
            print("\nEstados del expediente:")
            print("1. No visto")
            print("2. En proceso")
            print("3. Completado")

            opcion = int(input("Seleccione el nuevo estado: "))

            match opcion:
                case 1:
                    return "No visto"
                case 2:
                    return "En proceso"
                case 3:
                    return "Completado"
                case _:
                    print("Error: opcion invalida.")
        except ValueError:
            print("Error: opcion invalida.")


def pedir_numero_expediente(cantidad):
    """ Pide el número de un expediente entre 1 y la cantidad que existe """
    while True:
        try:
            numero = int(input("Ingrese el numero del expediente: "))

            if numero < 1 or numero > cantidad:
                print(f"Error: el numero debe estar entre 1 y {cantidad}.")
            else:
                return numero
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def pedir_folios():
    """ Pide el número de folios hasta que sea un entero positivo """
    while True:
        try:
            folios = int(input("Ingrese el numero de folios: "))

            if folios <= 0:
                print("Error: los folios deben ser positivos.")
            else:
                return folios
        except ValueError:
            print("Error: los folios deben ser un numero entero positivo.")
