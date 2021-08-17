import connection as con
import os

db = con.client.test

mydb1 = con.client["Evaluacion01"]
mycol = mydb1["CE"]

while True:
    #Panel de inicio
    os.system("cls")
    print("Inicio:")
    print("1. Ingresar nuevo Centro Escolar")
    print("2. Mostrar Centros Escolares")
    print("3. Actualizar")
    print("4. Eliminar Centro Escolar")
    print("5. Salir")

    opcion = input("Ingrese el número de la acción: ")
    
    #Crear
    if opcion == "1":
        dato1 = input("Inserte el  número de ID: ")
        dato2 = input("Inserte el nombre del Centro Escolar: ")
        dato3 = input("Inserte el nombre del Departamento: ")
        dato4 = input("Inserte el nombre del Municipio: ")

        mydata = { "_id": int(dato1), "nombre": dato2, "departamento": dato3, "municipio": dato4 }
        mydict = mycol.insert_one(mydata)
        input("¡Centro Escolar "+dato2+ " ingresado correctamente! \n Presione ENTER para continuar")
    
    
    #Buscar todos
    elif opcion == "2":
        for x in mycol.find(): 
            print(x)    
        input("Presione ENTER para continuar") 

    #Actualizar
    elif opcion == "3":
        dato1 = input("Inserte el  número de ID: ")
        dato2 = input("Inserte el nombre del Centro Escolar: ")
        dato3 = input("Inserte el nombre del Departamento: ")
        dato4 = input("inserte el nombre del Municipio: ")

        val = { "_id": int(dato1) }
        setVal = {"$set": { "nombre": dato2, "departamento": dato3, "municipio": dato4 } }
        mydict = mycol.update_one(val, setVal)
        input("¡Centro Escolar actualizado correctamente! \n Presione ENTER para continuar") 

    #Borrar
    elif opcion == "4":
        id = input("Ingrese el número de ID: ")
        val = { "_id": int(id) }

        valOut = mycol.delete_one(val)
        input("¡Centro Escolar eliminado correctamente! \n Presione ENTER para continuar")

    #Salir
    elif opcion == "5":
        print("Saliendo del Sistema \n Presione ENTER para continuar")
        input()
        break  
    
    else:
        print("Opción incorrecta")
        input("Pruebe otra opción \n Presione ENTER para continuar")
        continue   
  