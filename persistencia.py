""" Módulo de persistencia: guarda y lee los expedientes en el archivo
de texto """

ARCHIVO = "Expedientes.txt"
SEPARADOR = "|"


def guardar_expediente(dni, nombres, tipo, asunto, folios):
    """ Guarda un expediente como una nueva línea al final del archivo """
    linea = SEPARADOR.join([dni, nombres, tipo, asunto, str(folios)])

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def cargar_expedientes():
    """ Lee el archivo y devuelve una lista de expedientes.
        Cada expediente es una lista: [dni, nombres, tipo, asunto, folios] """
    expedientes = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    expediente = linea.split(SEPARADOR)
                    expedientes.append(expediente)
    except FileNotFoundError:
        # Si el archivo aún no existe,
        # no hay expedientes: se devuelve la lista vacía
        pass

    return expedientes
