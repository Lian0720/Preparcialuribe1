
import secrets

lista=[]

for _ in range(1,6):
    
    id_random=secrets.token_urlsafe(6)
    
    diccionario={
        "id":id_random, 
        "nombres":input("ingrese los nombres del empleado: "),
        "documento":input("ingrese el documento del empleado: "),
        "correo":input("ingrese el correo del empleado: "),
        "contraseña":input("ingrese la contraseña del empleado: ")
    }

    lista.append(diccionario)
    print(f"Empleado con id {id_random} registrado con éxito.")
        #el id sea entero o cadena alfanumérica por python
   
print("Lista de empleados registrados:")
print(lista)