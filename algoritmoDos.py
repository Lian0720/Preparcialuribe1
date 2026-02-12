# Algoritmo para login de asesores, se permiten 3 intentos.

import json


def cargar_credenciales(ruta_archivo="credenciales_asesores.json"):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontraron credenciales guardadas.")
        print("Primero ejecuta grupoUribe.py para registrar asesores.")
        return []


credenciales_bd = cargar_credenciales()

if credenciales_bd:
    intentos = 3
    contador = 0

    while contador < intentos:
        correo_input = input("Ingrese su correo: ")
        contraseña_input = input("Ingrese su contraseña: ")

        login_exitoso = any(
            credencial["correo"] == correo_input
            and credencial["contraseña"] == contraseña_input
            for credencial in credenciales_bd
        )

        if login_exitoso:
            print("¡Login exitoso!")
            break

        contador += 1
        print(f"Credenciales incorrectas. Intento {contador} de {intentos}.")

        if contador == intentos:
            print("Has excedido el número máximo de intentos. Acceso bloqueado.")
