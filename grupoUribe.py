import json
import secrets

from login import login_asesor
from generarListas import mostrar_reporte_promedio


def registrar_asesores(cantidad=2, ruta_archivo="credenciales_asesores.json"):
    lista = []
    credenciales = []

    for _ in range(cantidad):
        id_random = secrets.token_urlsafe(6)

        correo = input("Ingrese el correo del asesor 📧: ")
        contrasena = input("Ingrese la contrasena del asesor 🔑: ")

        diccionario = {
            "id": id_random,
            "nombre del asesor": input("Ingrese los nombres del asesor 👨‍💼: "),
            "marca": input("Ingrese la marca del asesor 👕: "),
            "correo": correo,
            "contrasena": contrasena,
        }

        lista.append(diccionario)
        credenciales.append({"correo": correo, "contrasena": contrasena})
        print(f"Asesor con id {id_random} registrado con exito. ✅")

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(credenciales, archivo, ensure_ascii=False, indent=2)

    print("Lista de asesores registrados 👨‍💼👩‍💼:")
    print(lista)
    print("Credenciales registradas correctamente. ✅")

    return lista, credenciales


def ejecutar_flujo_completo():
    registrar_asesores()

    print("\n==============================\nInicio de login de asesores ✅\n==============================")
    login_exitoso = login_asesor()

    if login_exitoso:
        print("\nLogin correcto ✅. Ejecutando medicones 📊...")
        mostrar_reporte_promedio()
    else:
        print("No se puede continuar con el promedio sin login valido. ❌")


if __name__ == "__main__":
    ejecutar_flujo_completo()
