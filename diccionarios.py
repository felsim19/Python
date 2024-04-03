datos = {}
clave = ""
def AgregarValor(clave, valor):
    datos[clave] = valor
    
for i in range(5):
    while True:
        clave = input(f"Ingrese clave {i + 1}: ")
        if not(clave in datos):
            datos[clave] = ""
            break
        else:
            print("Clave ya existe")
        


while True:
    print("MENU")
    print("1. Consultar diccionario.")
    print("2. Agregar valor a clave. ")
    print("3. Eliminar clave. ")
    print("4. Agregar dato.")
    print("5. Buscar")
    print("6. Salir")
    
    opcion = input("Elija su Opcion: ")

    if opcion == "1":
        for x, y in datos.items():
            print(f"{x}: {y}")
    elif opcion == "2":
        buscar = input("Que clave desea editar: ")
        if buscar in datos:
            datos[buscar] = input("Ingrese nuevo valor: ")
        else:
            print("Esta clave no esta en el diccionario")
    elif opcion == "3":
        eliminar = input("Que clave desea eliminar: ")
        if eliminar in datos:
            del datos[eliminar]
        else:
            print("Esta clave no esta en el diccionario")
    elif opcion == "4":    
        AgregarValor(clave, valor)
    elif opcion == "5":
        y = True
        while y:
            valor = input(f"Ingrese valor a buscar: ")
            for v in datos.values():
                if v == valor:
                    print("Si se encuentra.")
                    y = False
    elif opcion == "6":
        break
    else:
        print("Opcion no valida")

