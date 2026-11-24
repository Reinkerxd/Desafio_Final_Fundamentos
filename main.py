""" Programa de Mesa de Partes - Módulo principal """

import validaciones
import persistencia


# 1. REGISTRAR UN EXPEDIENTE
def registrar_expediente():
    """ Pide los datos del expediente y lo guarda en el archivo """
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    dni = validaciones.pedir_dni()
    nombres = validaciones.pedir_texto("Ingrese nombres y apellidos: ",
                                       "Error: los nombres son obligatorios.")
    tipo = validaciones.pedir_tipo_tramite()
    asunto = validaciones.pedir_texto("Ingrese el asunto: ",
                                      "Error: el asunto es obligatorio.")
    folios = validaciones.pedir_folios()

    persistencia.guardar_expediente(dni, nombres, tipo, asunto, folios)
    print("\nExpediente registrado correctamente.")


# 2. MOSTRAR LOS DATOS DE UN EXPEDIENTE
def mostrar_expediente(expediente):
    """ Muestra los datos de un expediente """
    print("\n--------------------------------")
    print("DNI:", expediente[0])
    print("Nombres:", expediente[1])
    print("Tipo:", expediente[2])
    print("Asunto:", expediente[3])
    print("Folios:", expediente[4])
    print("--------------------------------")


# 3. MOSTRAR TODOS LOS EXPEDIENTES
def listar_expedientes():
    """ Lista todos los expedientes guardados """
    lista = persistencia.cargar_expedientes()

    if len(lista) == 0:
        print("\nERROR: No hay expedientes registrados")
    else:
        print("\n==== LISTADO DE EXPEDIENTES ====")
        for expediente in lista:
            mostrar_expediente(expediente)


# 4. MENU PRINCIPAL
def menu():
    """ Ejecuta el menú del programa """
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
if __name__ == "__main__":
    menu()
