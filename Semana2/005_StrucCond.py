#el programa pedira una cantidad en pesos mexicanos y mostrara
#un menu con opciones para convertir a dolares

usuario = input("Introduzca su nombre :")
pesos = int(input("Introduzca la cantidad de pesos : "))
opcion = int(input("1 : Pesos , 2: Dolares : "))


mensaje1 = "La cantidad convertida a Dolares es :"
mensaje2 = "La cantidad convertida a pesos es :"
ancho=80


if(opcion==1):
    total=pesos/17
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,round(total,2))
elif(opcion==2):
    total=pesos/4
    mensaje2=mensaje2.center(ancho)
    print(mensaje2,round(total,2))
else:
    print("Elegiste una opcion no valida")