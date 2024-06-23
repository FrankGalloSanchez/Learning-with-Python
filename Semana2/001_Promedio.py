#Este programa calcula y muestra el promedio de calificaciones de un alumno
#Float lo que hace es transformar el calculo y contenga decimales
print("El programa calcula el promedio de 3 calificaciones de un alumno")

nombre =input("Escribe tu nombre :")
mat = float(input("Escribir la calificacion de Matematicas :"))
fis = float(input("Escribir la calificacion de Fisica :"))
quim = float(input("Escribir la calificacion de Quimica :"))

promedio = (mat+fis+quim)/3

print(nombre ,"Su promedio es :" , round(promedio),2)
#round lo que hace es por ejemplo solo que permita tantos decimales


if (promedio >= 12 ):
    print("Felicitaciones aprobastes")
else:
    print("Felicidades wawita reprobastes")