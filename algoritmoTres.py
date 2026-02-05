#recorrer una lista y obtener el promedio númerico
import random

lista=[random.randint(0,450) for _ in range(20)]
suma=0

for elemento in lista:
    suma+=elemento
    promedio=suma/len(lista)
print(f"La lista generada es: {lista}")
print(f"El promedio de la lista es: {promedio}")

if promedio>0 and promedio<=250:
    print("Operación detenida por falta de agua")
elif promedio>250 and promedio<400:
    print("Operación con normalidad")
else:
    print("Deben abrirse las compuertas")