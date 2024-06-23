#el numero pedira un numero para sumarlo
contador = 0
suma = 0
numero = 0

while True: #do - while
    numero=float(input("Escribe un numero para sumarlo (0 para salir) : "))
    if(numero== 0):
        break
    suma+=numero
    contador+=1
    
#cuando haya salido del ciclo
if(contador>0):
    promedio=suma/contador
    print("La suma de los numeros es",suma)
    print("El total de los numeros introducidos por el usuario es :", contador)
    print("El promedio de los numeros ingresados es",promedio)
else:
    print("No se ingresaron numeros validos...")