import json
import secrets

lista = []
credenciales = []

for _ in range(1, 6):
    id_random = secrets.token_urlsafe(6)

    correo = input("Ingrese el correo del asesor: ")
    contraseña = input("Ingrese la contraseña del asesor: ")

    diccionario = {
        "id": id_random,
        "nombre del asesor": input("Ingrese los nombres del asesor: "),
        "marca": input("Ingrese la marca del asesor: "),
        "correo": correo,
        "contraseña": contraseña,
    }

    lista.append(diccionario)
    credenciales.append({"correo": correo, "contraseña": contraseña})
    print(f"Asesor con id {id_random} registrado con éxito.")

with open("credenciales_asesores.json", "w", encoding="utf-8") as archivo:
    json.dump(credenciales, archivo, ensure_ascii=False, indent=2)

print("Lista de asesores registrados:")
print(lista)
print("Credenciales guardadas en credenciales_asesores.json")
