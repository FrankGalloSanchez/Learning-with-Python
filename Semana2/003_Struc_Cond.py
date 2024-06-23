#El programa evaluara la estatura del usuario 
# si la estatura es menor que 160 cms imprimira Eres pequeño
# si la estatura es entre 160 y 175 cms imprimira eres de estatura mediana
# Si la estatira es amyor a 175 cms imprimira eres alto

print("El programa evaluara la estatura del usuario")
usuario = input("Introduce tu nombre : ")
estatura = int(input("Introduce tu estatura en cms : "))

if estatura < 160:
    print(usuario ,"Eres pequeño")
elif estatura <=175:
    print(usuario , "Tu eres de estatura mediana")
else:
    print(usuario ,"Eres alto")

#Otra manera menos escalable
#if estatura < 160:
#    print(usuario ,"Eres pequeño")

#if estatura >= 160 and estatura <= 175:
#    print(usuario ,"Tu estatura es mediana")

#if estatura > 175:
#    print(usuario , "Eres alto")