

import json
import os
from datetime import datetime

ARCHIVO = "expedientes.txt"
RESPALDO = "respaldo_expedientes.txt"

expedientes = []


# 1. CARGAR LOS EXPEDIENTES GUARDADOS
def cargar_expedientes():
    if os.path.exists(ARCHIVO):
        try:
            archivo = open(ARCHIVO, "r", encoding="utf-8")
            datos = json.load(archivo)
            archivo.close()
            return datos
        except (OSError, json.JSONDecodeError):
            print("No se pudieron cargar los datos.")

    return []


# 2. GUARDAR LOS EXPEDIENTES Y EL RESPALDO
def guardar_expedientes():
    try:
        archivo = open(ARCHIVO, "w", encoding="utf-8")
        json.dump(expedientes, archivo, indent=4, ensure_ascii=False)
        archivo.close()

        archivo = open(RESPALDO, "w", encoding="utf-8")
        json.dump(expedientes, archivo, indent=4, ensure_ascii=False)
        archivo.close()

        return True

    except OSError:
        print("Error al guardar los archivos.")
        return False


# 3. GENERAR UN CODIGO CORRELATIVO
def generar_codigo():
    mayor = 0

    for expediente in expedientes:
        numero = int(expediente["codigo"].split("-")[1])

        if numero > mayor:
            mayor = numero

    return "EXP-" + str(mayor + 1).zfill(4)


# 4. REGISTRAR UN EXPEDIENTE
def registrar_expediente():
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    dni = input("Ingrese DNI de 8 digitos: ").strip()

    if len(dni) != 8 or not dni.isdigit():
        print("Error: el DNI debe tener 8 digitos.")
        return

    nombres = input("Ingrese nombres y apellidos: ").strip()

    if nombres == "":
        print("Error: los nombres son obligatorios.")
        return

    print("\nTipos de tramite:")
    print("1. Solicitud")
    print("2. Licencia")
    print("3. Reclamo")

    opcion = input("Seleccione el tipo de tramite: ").strip()

    if opcion == "1":
        tipo = "Solicitud"
    elif opcion == "2":
        tipo = "Licencia"
    elif opcion == "3":
        tipo = "Reclamo"
    else:
        print("Tipo de tramite incorrecto.")
        return

    asunto = input("Ingrese el asunto: ").strip()

    if asunto == "":
        print("Error: el asunto es obligatorio.")
        return

    folios = input("Ingrese el numero de folios: ").strip()

    if not folios.isdigit() or int(folios) <= 0:
        print("Error: los folios deben ser positivos.")
        return

    # Crear el expediente
    expediente = {
        "codigo": generar_codigo(),
        "dni": dni,
        "nombres": nombres,
        "tipo": tipo,
        "asunto": asunto,
        "folios": int(folios),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expedientes.append(expediente)

    if guardar_expedientes():
        print("\nExpediente registrado correctamente.")
        print("Codigo asignado:", expediente["codigo"])
        print("Fecha:", expediente["fecha"])
    else:
        expedientes.pop()
        print("No se pudo completar el registro.")


# 5. MOSTRAR LOS DATOS DE UN EXPEDIENTE
def mostrar_expediente(expediente):
    print("\n------------------------------")
    print("Codigo:", expediente["codigo"])
    print("DNI:", expediente["dni"])
    print("Nombres:", expediente["nombres"])
    print("Tipo:", expediente["tipo"])
    print("Asunto:", expediente["asunto"])
    print("Folios:", expediente["folios"])
    print("Fecha:", expediente["fecha"])
    print("------------------------------")


# 6. BUSCAR UN EXPEDIENTE POR CODIGO
def buscar_expediente():
    codigo = input("Ingrese el codigo (ejemplo EXP-0001): ")
    encontrado = False

    for expediente in expedientes:
        if expediente["codigo"] == codigo.upper().strip():
            mostrar_expediente(expediente)
            encontrado = True
            break

    if encontrado == False:
        print("Expediente no encontrado.")


# 7. MOSTRAR TODOS LOS EXPEDIENTES
def listar_expedientes():
    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
    else:
        print("\n--- LISTADO DE EXPEDIENTES ---")

        for expediente in expedientes:
            mostrar_expediente(expediente)


# 8. ORDENAR EXPEDIENTES
def ordenar_expedientes():
    if len(expedientes) == 0:
        print("No hay expedientes para ordenar.")
        return

    print("\n1. Ordenar por numero de folios")
    print("2. Ordenar por fecha")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        expedientes.sort(key=lambda e: e["folios"])
    elif opcion == "2":
        expedientes.sort(key=lambda e: e["fecha"])
    else:
        print("Opcion incorrecta.")
        return

    guardar_expedientes()

    print("\nExpedientes ordenados:")

    for expediente in expedientes:
        print(
            expediente["codigo"],
            "-",
            expediente["nombres"],
            "- Folios:",
            expediente["folios"],
            "- Fecha:",
            expediente["fecha"]
        )


# 9. MENU PRINCIPAL
def menu():
    global expedientes

    expedientes = cargar_expedientes()

    while True:
        print("\n================================")
        print(" SISTEMA DE MESA DE PARTES")
        print("================================")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Mostrar expedientes")
        print("4. Ordenar expedientes")
        print("5. Salir")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            buscar_expediente()
        elif opcion == "3":
            listar_expedientes()
        elif opcion == "4":
            ordenar_expedientes()
        elif opcion == "5":
            print("Datos guardados. Hasta luego.")
            break
        else:
            print("Opcion incorrecta.")


# INICIO DEL PROGRAMA
menu()
