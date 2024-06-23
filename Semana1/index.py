# Pedir al usuario que ingrese los dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Definir la función para sumar los dos números
def suma(num1, num2):
    return num1 + num2
def resta(num1,num2):
    return num1 - num2

# Llamar a la función y almacenar el resultado
resultado = suma(num1, num2)

# Mostrar el resultado
print("El resultado es el siguiente:", resultado)
