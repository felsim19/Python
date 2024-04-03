Usuarios=[]
while True:
    print("1.Insertar usuario en la lista ")
    print("2.Consultar usuarios ")
    print("3.Buscar usuario en lista ")
    print("4.Modificar usuario en la lista ")
    print("5.Eliminar usuario en la lista ")
    print("6.salir")
    opcion = int(input("Digite el numero "))
    if opcion == 1:
        Insertar= str(input("Ingrese el usuario "))
        Usuarios.append(Insertar)
    elif opcion == 2:
        print(Usuarios)
    elif opcion == 3:
        Buscar_Usario= str(input("Ingrese el usuario que esta buscando "))
        if Buscar_Usario in Usuarios:
            ind = Usuarios.index(Buscar_Usario)
            print(f"Si exite y esta en la posicion {ind}")
        else:
            print("Este usuario no existe")
    elif opcion == 4:
        indice = int(input("Digite el indice que quiere modificar "))
        nuevo = str(input("digite el nombre que quiere que quede en esa posicion "))
        Usuarios [indice]= nuevo 
    elif opcion == 5:
        Buscar_Usario= str(input("Ingrese el usuario que quiere elimiar "))
        if Buscar_Usario in Usuarios:
            ind = Usuarios.index(Buscar_Usario)
            eliminar = Usuarios.remove(Buscar_Usario)
            print("Felicidades haz eliminado al usuario")
        else:
             print("Este usuario no existe")
    elif opcion == 6:
        print("Usted a salido del programa buena tarde")
        break
    else:
        print("Ese valor no existe")

