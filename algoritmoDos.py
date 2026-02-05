#Algoritmo para login de usuario, se permiten 3 intentos.

correoBD="correo@gmail.com"
contraseñaBD="contraseña123"

intentos=3
contador=0

while contador<intentos:
    correoInput=input("Ingrese su correo: ")
    contraseñaInput=input("Ingrese su contraseña: ")
    
    if correoInput==correoBD and contraseñaInput==contraseñaBD:
        print("¡Login exitoso!")
        break
    else:
        contador+=1
        print(f"Credenciales incorrectas. Intento {contador} de {intentos}.")
        
        if contador==intentos:
            print("Has excedido el número máximo de intentos. Acceso bloqueado.")