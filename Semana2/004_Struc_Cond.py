#El programa indicara un numero de dia y si le imprimira el nombre del dia
print("El programa indicará un número de día y imprimirá el nombre del día")
nombre = input("Introduce tu Nombre: ")
dia = int(input("Introduce el número del día que cubrirá tu guardia (1-7): "))

if dia == 1:
    nombre_dia = "Lunes"
elif dia == 2:
    nombre_dia = "Martes"   
elif dia == 3:
    nombre_dia = "Miércoles"
elif dia == 4:
    nombre_dia = "Jueves"
elif dia == 5:
    nombre_dia = "Viernes"
elif dia == 6:
    nombre_dia = "Sábado"
elif dia == 7:
    nombre_dia = "Domingo"
else:
    nombre_dia = "Número de día inválido"

print(f"{nombre}, tu guardia es el día: {nombre_dia}")
