#El programa determina si puedes votan o no
nombre = input("Escribe tu nombre wawita :")
edad = int(input("Escribe tu edad :"))

if edad > 18:
    print(nombre ,"Puedes votar causa")
else:
    print(nombre ,"No puedes votar")