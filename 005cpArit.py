#Veremos como se manejan algunos operadores de asignacion
num1 = 5
num2 = 10
print("La variable num1 vale:",num1)
print("La variable num2 vale:",num2)
num1+=num2 #Es lo mismo que escribir num1=num1+num2
#Aqui hacemos una Suma a num1
print("Usando el operador += , num1 ahora vale :",num1)
#Aqui Multiplicamos el Num1 * Num2 pero esto dentro de num1 osea el valor sale num1 = 150
num1*=num2
print("Usando el operador *= num1 ahora vale :",num1)
#Aqui Restamos el Num1 - Num2 pero esto dentro de num1 osea el valor sale num1 = 140 
#Osea aqui como agarramos el valor num1 anterior que es num1 = 150 esto lo que hace es restar 10 y sale = 140
num1-=num2
print("Usando el operador -= , num1 ahora vale :",num1)
#Aqui Dividimos el Num1 / Num2 pero esto dentro de num1 osea el valor sale num1 = 14.0 
#Osea aqui como agarramos el valor num1 anterior que es num1 = 140 esto lo que hace es dividir 140 / num2 10  y sale = 14.0
num1/=num2
print("Usando el operador /= , num1 ahora vale :",num1)
