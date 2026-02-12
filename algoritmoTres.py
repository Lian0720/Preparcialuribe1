#recorrer una lista y obtener el promedio númerico
import random

lista=[random.randint(0,50) for _ in range(100)]
suma=0

for elemento in lista:
    suma+=elemento
    promedio=suma/len(lista)
print(f"La lista de mediciones es: {lista}")
print(f"El promedio de las 100 mediciones es: {promedio}")

if promedio>0 and promedio<=20:
    print("Rotación Baja")
elif promedio>20 and promedio<30:
    print("Rotación Normal")
else:
    print("Rotación Alta, se debe reabastecer.")