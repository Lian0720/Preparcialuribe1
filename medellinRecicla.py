import json
import secrets

from login import login_gestor
from generarListas import mostrar_reporte_promedio


def registrar_gestores(cantidad=5, ruta_archivo="credenciales_gestores.json"):
    lista = []
    credenciales = []

    for _ in range(cantidad):
        id_random = secrets.token_urlsafe(6)

        correo = input("Ingrese el correo del gestor 📧: ")
        contrasena = input("Ingrese la contrasena del gestor 🔑: ")

        diccionario = {
            "id": id_random,
            "nombre del gestor": input("Ingrese los nombres del gestor 👨‍💼: "),
            "empresa": input("Ingrese la empresa del gestor 🏛️:  "),
            "rol": input("Ingrese el rol del gestor 🌱: "),
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
    registrar_gestores()

    print("\n==============================\nInicio de login de gestores ambientales ✅\n==============================")
    login_exitoso = login_gestor()

    if login_exitoso:
        print("\nLogin correcto ✅. Ejecutando medicones 📊...")
        mostrar_reporte_promedio()
    else:
        print("No se puede continuar con el promedio sin login valido. ❌")


if __name__ == "__main__":
    ejecutar_flujo_completo()
