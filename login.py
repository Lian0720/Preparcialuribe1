# Algoritmo para login de gestores, se permiten 3 intentos.

import json


def cargar_credenciales(ruta_archivo="credenciales_gestores.json"):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontraron credenciales guardadas. ❌")
        print("Primero debes registrar los asesores. ⚠️")
        return []


def login_gestor(credenciales_bd=None, intentos=3):
    if credenciales_bd is None:
        credenciales_bd = cargar_credenciales()

    if not credenciales_bd:
        return False

    contador = 0

    while contador < intentos:
        correo_input = input("Ingrese su correo 📧: ")
        contrasena_input = input("Ingrese su contrasena 🔑: ")

        login_exitoso = any(
            credencial.get("correo") == correo_input
            and credencial.get("contrasena") == contrasena_input
            for credencial in credenciales_bd
        )

        if login_exitoso:
            print("Login exitoso. ✅")
            return True

        contador += 1
        print(f"Credenciales incorrectas. ❌ Intento {contador} de {intentos}. ⚠️")

    print("Has excedido el numero maximo de intentos. Acceso bloqueado. ❌")
    return False


if __name__ == "__main__":
    login_gestor()
