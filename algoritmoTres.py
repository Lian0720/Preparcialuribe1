# Recorrer una lista y obtener el promedio numerico.
import random


def calcular_promedio_mediciones(cantidad=100, minimo=0, maximo=50):
    lista = [random.randint(minimo, maximo) for _ in range(cantidad)]
    suma = sum(lista)
    promedio = suma / len(lista)

    if 0 < promedio <= 20:
        estado = "Rotacion baja"
    elif 20 < promedio < 30:
        estado = "Rotacion normal"
    else:
        estado = "Rotacion alta, se debe reabastecer"

    return lista, promedio, estado


def mostrar_reporte_promedio(cantidad=100, minimo=0, maximo=50):
    lista, promedio, estado = calcular_promedio_mediciones(cantidad, minimo, maximo)
    print(f"La lista de mediciones es: {lista}")
    print(f"El promedio de las {cantidad} mediciones es: {promedio:.2f}")
    print(estado)


if __name__ == "__main__":
    mostrar_reporte_promedio()
