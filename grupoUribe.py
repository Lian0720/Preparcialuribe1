import secrets

lista=[]

for _ in range(1,6):
    
    id_random=secrets.token_urlsafe(6)
    
    diccionario={
        "id":id_random, 
        "nombre del asesor":input("ingrese los nombres del asesor: "),
        "marca":input("ingrese la marca del asesor: "),
        "correo":input("ingrese el correo del asesor: "),
        "contraseña":input("ingrese la contraseña del asesor ")
    }

    lista.append(diccionario)
    print(f"Asesor con id {id_random} registrado con éxito.")
        #el id sea entero o cadena alfanumérica por python
   
print("Lista de asesores registrados:")
print(lista)