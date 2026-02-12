# Recorrer una lista y obtener el promedio numerico.
import random


def calcular_promedio_mediciones(cantidad=100, minimo=0, maximo=50):
    lista = [random.randint(minimo, maximo) for _ in range(cantidad)]
    suma = sum(lista)
    promedio = suma / len(lista)

    if 0 < promedio <= 20:
        estado = "Rotacion baja. ⬇️"
    elif 20 < promedio < 30:
        estado = "Rotacion normal. ➡️"
    else:
        estado = "Rotacion alta, ⬆️ se debe reabastecer"

    return lista, promedio, estado


def eliminar_ultima_medicion(lista):
    if not lista:
        print("No hay mediciones para eliminar. ❌")
        return

    medicion_eliminada = lista.pop()
    print(f"Se elimino la ultima medicion: 🗑️   {medicion_eliminada}")


def buscar_posicion_medicion(lista):
    if not lista:
        print("No hay mediciones para buscar. ⚠️")
        return

    try:
        medicion = int(input("Ingrese la medicion a buscar 🔍: "))
        posicion = lista.index(medicion)
        print(f"La medicion {medicion} esta en la posicion {posicion}. ✅")
    except ValueError:
        print("La medicion no existe en la lista o el valor ingresado no es valido. ❌")


def eliminar_medicion_por_posicion(lista):
    if not lista:
        print("No hay mediciones para eliminar. ⚠️")
        return

    try:
        posicion = int(input(f"Ingrese la posicion a eliminar 🗑️ (0 a {len(lista) - 1}): "))
        medicion_eliminada = lista.pop(posicion)
        print(f"Se elimino la medicion {medicion_eliminada} de la posicion {posicion}. 🗑️")
    except (ValueError, IndexError):
        print("La posicion ingresada no es valida. ❌")


def gestionar_mediciones(lista):
    while True:
        print("\n==============================\nOpciones de gestión de mediciones 📊\n==============================")
        print("1. Eliminar ultima medicion. 🗑️")
        print("2. Buscar posicion de una medicion. 🔍")
        print("3. Eliminar medicion por posicion. 🔍🗑️")
        print("4. Salir ⚠️")

        opcion = input("Seleccione una opcion ▶️: ")

        if opcion == "1":
            eliminar_ultima_medicion(lista)
        elif opcion == "2":
            buscar_posicion_medicion(lista)
        elif opcion == "3":
            eliminar_medicion_por_posicion(lista)
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. ❌")

        print(f"Lista actual de mediciones 📊: {lista}")


def mostrar_reporte_promedio(cantidad=100, minimo=0, maximo=50):
    lista, promedio, estado = calcular_promedio_mediciones(cantidad, minimo, maximo)
    print(f"La lista de mediciones es ▶️: {lista}")
    print(f"El promedio de las {cantidad} mediciones 📊 es: {promedio:.2f}")
    print(estado)

    gestionar_mediciones(lista)


if __name__ == "__main__":
    mostrar_reporte_promedio()
