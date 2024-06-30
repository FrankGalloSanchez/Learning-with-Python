#Esta programa valida para que solo se introduzcan datos numericos
while True:
    try:
        datos=input("Por favor ingrese una edad :")
        edad=int(datos)
        if(edad<0):
            print("edad no valida")
        else: #si edad es mayor que 0
            break; #se debe salir por que ya tenemos numero valido
    except ValueError:
        print("Error al capturar por favor ingrese un dato numerico")
print("la edad es valida:", edad)