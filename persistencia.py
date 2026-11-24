""" Módulo de persistencia: guarda y lee los expedientes en el archivo de
texto """

ARCHIVO = "Expedientes.txt"
SEPARADOR = "|"


def guardar_expediente(dni, nombres, tipo, asunto, folios, estado):
    """ Guarda un expediente como una nueva línea al final del archivo """
    linea = SEPARADOR.join([dni, nombres, tipo, asunto, str(folios), estado])

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def guardar_todos(expedientes):
    """ Reescribe el archivo completo con la lista de expedientes.
        Se usa cuando se modifica un expediente que ya existía """
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for expediente in expedientes:
            linea = SEPARADOR.join(expediente)
            archivo.write(linea + "\n")


def cargar_expedientes():
    """ Lee el archivo y devuelve una lista de expedientes.
        Cada expediente es una lista:
        [dni, nombres, tipo, asunto, folios, estado] """
    expedientes = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    expediente = linea.split(SEPARADOR)
                    expedientes.append(expediente)
    except FileNotFoundError:
        # Si el archivo aún no existe, no hay expedientes:
        # se devuelve la lista vacía
        pass

    return expedientes
