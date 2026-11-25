""" Módulo de validaciones: pide los datos al usuario y verifica que sean
correctos """


def pedir_dni():
    """ Pide un DNI hasta que tenga exactamente 8 dígitos """
    while True:
        dni = input("Ingrese DNI de 8 dígitos: ").strip()

        if len(dni) != 8 or not dni.isdigit():
            print("Error: el DNI debe tener 8 dígitos.")
        else:
            return dni


def pedir_nombres():
    """ Pide nombres y apellidos: solo letras y espacios """
    while True:
        nombres = input("Ingrese nombres y apellidos: ").strip()

        if nombres == "":
            print("Error: los nombres son obligatorios.")
        elif not nombres.replace(" ", "").isalpha():
            print("Error: los nombres solo pueden contener letras y espacios.")
        else:
            return nombres


def pedir_texto(mensaje, mensaje_error):
    """ Pide un texto obligatorio (no vacío). Sirve para nombres y asunto """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print(mensaje_error)
        elif "|" in texto:
            print("Error: no se permite el carácter '|'.")
        else:
            return texto


def pedir_tipo_tramite():
    """ Muestra los tipos de trámite y devuelve el elegido """
    while True:
        try:
            print("\nTipos de trámite:")
            print("1. Solicitud")
            print("2. Licencia")
            print("3. Reclamo")

            opcion = int(input("Seleccione el tipo de trámite: "))

            match opcion:
                case 1:
                    return "Solicitud"
                case 2:
                    return "Licencia"
                case 3:
                    return "Reclamo"
                case _:
                    print("Error: opción inválida.")
        except ValueError:
            print("Error: opcion inválida.")


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
                    print("Error: opción inválida.")
        except ValueError:
            print("Error: opción inválida.")


def pedir_numero_expediente(cantidad):
    """ Pide el número de un expediente entre 1 y la cantidad que existe """
    while True:
        try:
            numero = int(input("Ingrese el número del expediente: "))

            if numero < 1 or numero > cantidad:
                print(f"Error: el número debe estar entre 1 y {cantidad}.")
            else:
                return numero
        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_folios():
    """ Pide el número de folios hasta que sea un entero positivo """
    while True:
        try:
            folios = int(input("Ingrese el número de folios: "))

            if folios <= 0:
                print("Error: los folios deben ser positivos.")
            else:
                return folios
        except ValueError:
            print("Error: los folios deben ser un número entero positivo.")
