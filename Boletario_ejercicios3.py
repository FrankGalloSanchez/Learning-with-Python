#Listas y bucles:
#Escribe un programa que imprima todos los elementos de una lista.
lista = [23,24,25]
print(lista)
#Escribe un programa que calcule la suma de todos los números en una lista.
numeros = [23,24,25]
suma = 0
for numero in numeros:
    suma += numero
print("La suma es", suma)
#Escribe un programa que encuentre el número más grande en una lista.
numeros = [3, 5, 2, 8, 1]
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("El mayor número es:", mayor)
#Filtrar Elementos en una Lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print("Números pares:", pares)