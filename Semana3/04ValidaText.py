#Esta programa valida para que solo se introduzcan datos de texto
while True:
    try:
        dato=input("Ingrese tu nombre de usuario :")
        nombre=int(dato)
        print("El dato ingresado es un numero")
    except ValueError:
        break
print("Tu nombre de usuario es:",dato)