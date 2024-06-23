#convertiremos de metros a kilomentos


distancia = float(input("Introduce su la cantidad en metros : "))
opcion = input('\n Introduce la cantidad en que quieras convertir :'
                '\n a) Convertir en Kilometros '
                '\n b) Convertir en centimetros'
                '\n Introduce la opcion : ')

if opcion=='a':
    total=distancia/1000
    print("La cantidad convertida a kilometros es :" ,total)
elif opcion=='b':
    total=distancia*100
    print("La cantidad convertida en centimetros es:" , total)
else:
    print ("Opcion no valida")

