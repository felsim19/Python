numeros = []

while(True):
    print("1.Añadir numero a la lista")
    print("2.Añadir numero de la lista en un pocision")
    print("3.Longitu de la lista")
    print("4.Eliminar el ultimo numero")
    print("5.Eliminar un numero")
    print("6.Contar numero")
    print("7.Pocision de un numero")
    print("8.Mostrar numeros")
    print("9.salir")

    opcion = int(input("Seleccione alguna opcion "))

    if(opcion == 1):
        AgregarNumero = int(input("Digite el numero que va a agregar "))
        numeros.append(AgregarNumero)
        print("El numero ha sido agregado correctamente")
    elif(opcion == 2):
        pocision = int(input("Digite la pocision en la que va a añadir el numero")) - 1
        AgregarNumero = int(input("Digite el numero que va a agregar "))
        if (0 <= pocision <= len(numeros)):
            numeros[pocision] = AgregarNumero
            print("la pocision esta en la lista y ya se agrego el cambio")
        else:
            print("El indice de la pocision esta incorrecto")
    elif(opcion == 3):
        print(f"La longuitud de la lista es de {len(numeros)}") 
    elif(opcion == 4):
        if len(numeros) > 0:
            ultimonumero = numeros[-1]
            numeros.remove(ultimonumero)
            print("Se ha eliminadoel numero de la ultima posicion")  
        else:
            print("La lista esta vacia")
    elif(opcion == 5):
        if(len(numeros) > 0):
            ind = int(input("Digite el numero de la pocision que va a borrar")) - 1
            if (0 <= ind < len(numeros)):
                numeros.pop(ind)
                print("Esa posicion ya a sido borradada satisfactoriamente")
            else: 
                print("Esa posicion ya existe")
        else:
            print("La lista esta vacia")
    elif(opcion == 6):
        Numero = int(input("Digite el numero que desea contar"))
        contador = 0
        for i in range(0, len(numeros)):
            if numeros[i] == Numero:
                contador += 1
        if (contador == 0):
            print("Este numero no se encuentra en la lista")
        else:
            print(f"El numero se encontro y esta en la lista {contador}")
    elif(opcion == 7):
        buscarN = int(input("Digite el numero de la pocision que va a buscar"))
        if buscarN in numeros:
            ind = numeros.index(buscarN) + 1
            print(f"Este numero existe y esta en la posicion {ind}")
        else:
            print("Este numero no esta en la lista")
    elif(opcion == 8):
        print(numeros)
    elif(opcion == 9):
        print("Usted a salido del programa")
        break
    else:
        print("Ingrese un numero valido")


   
