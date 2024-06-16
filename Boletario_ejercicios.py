#Escribe un programa que sume dos números ingresados por el usuario.
num1 = int(input("Ingrese el primer valor :"))
num2 = int(input("Ingrese el primer valor :"))

def suma (num1 , num2):
    return num1 + num2

resultado = suma(num1,num2)

print("La suma de usted es la siguiente",resultado)
#Calcula el área de un triángulo con base y altura ingresadas por el usuario.
base = float(input("ingrese la base del triangulo : "))
altura = float(input("ingrese la altura del triangulo :"))

area =base*altura

print("El resultado es" , area)
#Convierte grados Celsius a Fahrenheit (F = C * 9/5 + 32).

gradoscelsius = int(input("Ingrese Grados celsius"))

def Fahrenheit(gradoscelsius):
    return  gradoscelsius * 9/5 + 32

resultado = Fahrenheit(gradoscelsius)

print("La conversion es : " , resultado)