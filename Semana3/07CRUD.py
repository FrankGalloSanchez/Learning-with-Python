#CRUD Create - Read - Update - Delete
import time
import os #nos permite usar instrucciones de nuestro sistema opertivo
import mysql.connector

#creamos la conecciona  la base de datos
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pruebda"
)
mycursor=mydb.cursor()

while True:
    print("****** MENU DEL SISTEMA *******"
          "\n 1. Insertar un dato"
          "\n 2. Eliminar un dato"
          "\n 3. Buscar un dato"
          "\n 4. Sobreescribir un dato"
          "\n 5. Mostrar el contenido de la tabla"
          "\n 6. Salir del sistema")
    opcion=int(input("Elige una opcion: "))
    if opcion==1: #Create (insertar)
        dato=input("Ingresa el producto a insertar : ")
        sql='INSERT INTO datos (dato) VALUES (%s)'
        val=(dato,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"Registros insertados")
        time.sleep(2)
        os.system('cls')
    if opcion==2: #opcion eliminar
        id=int(input("Ingrese el id del producto a eliminar :"))
        dato=input("Ingresa el producto a eliminar : ")
        sql='DELETE FROM datos WHERE dato=%s'
        val=(dato,id)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"Registros eliminados")
        time.sleep(2)
        os.system('cls')
    if opcion==3:
        dato=input("Ingresa el producto a buscar : ")
        sql='SELECT * FROM datos WHERE dato=%s'
        val=(dato,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if myresult:
            print("El dato existe en la tabla")
        else:
            print("El dato no existe en la tabla")
        time.sleep(2)
        os.system("cls")
    if opcion==4:
        id=int(input("Ingresa el id del dato :"))
        dato=input("Ingresa el producto a sobreescribir : ")
        sql = "UPDATE datos SET dato=%s WHERE id=%s"
        val=(dato,id)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"Registros sobreescritos")
        time.sleep(2)
        os.system('cls')
    if opcion==5:
        sql='SELECT * FROM datos'
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        time.sleep(2)
        os.system('cls')
    if opcion==6: #salir
        respuesta = print("Estas seguro? (s/n)")
        if respuesta.upper()=="S":
            print("Saliendo del sistema")
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
        print("Opcion no valida intenta de nuevo ...")
        time.sleep(2)
        os.system('cls')

#cerrar la base de datos
mydb.close()