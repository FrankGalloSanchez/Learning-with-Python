#crearemos una funcion para que sea par o impar
def Es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero=int(input("Escribe un numero y determinare si es par o impar : "))

if Es_par(numero):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")