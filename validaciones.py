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
