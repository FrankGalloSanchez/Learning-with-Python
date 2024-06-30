#Creamos un login
import time
import mysql.connector
import os

#creamos la conecciona  la base de datos
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pruebda"
)

mycursor=mydb.cursor()
while True:
    print("****** LOGIN*******")
    print("1. Ingresar")
    print("2. Salir")
    print("3. Registrarse")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        print("****** LOGIN*******")
        usuario=input("Ingrese su usuario: ")
        password=input("Ingrese su contraseña: ")
        sql="SELECT * FROM usuarios WHERE usuario=%s AND password=%s"
        val=(usuario,password)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if myresult:
            print("Bienvenido")
            break
    if opcion==3:
        print("****** REGISTRO*******")
        usuario=input("Ingrese su usuario: ")
        password=input("Ingrese su contraseña")
        sql="INSERT INTO usuarios (usuario,password) VALUES (%s,%s)"
        val=(usuario,password)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Usuario registrado")
    if opcion==2:
        print("Saliendo")
        break