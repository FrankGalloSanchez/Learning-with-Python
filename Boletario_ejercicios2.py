#Escribe un programa que determine si un número ingresado por el usuario es par o impar.

n1 = int(input("Ingrese el numero : "))

if n1 % 2 == 0 :
    print(f"{n1}El valor es par")
else :
    print(f"{n1} El valor es impar")

#Escribe un programa que encuentre el número mayor entre tres números ingresados por el usuario.
n1 = int(input("Ingrese el Primer numero :"))
n2 = int(input("Ingrese el Segundo numero :"))
n3 = int(input("ingrese el Tercer numero :"))

if n1 > n2 > n3 :
    print("El Primer numero es Mayor :" , n1)
elif  n2 > n1 > n3:
    print("El segundo Numero es Mayor :",n2)
else : n3 > n1 > n2 
print("El Tercer nunero es el mayor :",n3)

#Escribe un programa que verifique si un número ingresado por el usuario es positivo, negativo o cero.
n1 = int(input("Ingrese el numero wawita : "))

if n1 >= 1 :
    print("Es Positivo")
elif n1 < 1 :
    print("El Negativo")
else:   
    print("Es 0 wawita")
