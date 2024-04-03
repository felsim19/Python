#/////////////////////////////////CICLO WHILE/////////////////////////////////

'''print("bienvenido")
x = 1
capacidad = int(input("digite para cuantas personas va a hacer el programa"))
while(x <= capacidad):
    nombre = str(input("Digite su nombre"))
    tipo = int(input("Digite su tipo"))
    descuento = 0
    if tipo == 1:
        print("se le descuenta el 5%")
        descuento = 0.05
    elif tipo == 2:
        print("se le descuenta el 8%")
        descuento = 0.08
    elif tipo == 3:
        print("se le descuenta el 12%")
        descuento = 0.12
    elif tipo == 4:
        print("se le descuenta el 15%")
        descuento = 0.15
    else:
        print("ese dato es un error vuelve a intartalo nuevamente")
        break
    cantidadhojas= int(input("Cuantas hojas compro"))
    preciohojas = int(input("el valor de las hojas es"))
    valorsubFinal = (cantidadhojas * preciohojas)
    valorFinal =  int(valorsubFinal - (valorsubFinal* descuento))
    print(f"El nombre del usuario es {nombre}")
    print(f"El tipo del usuario es {tipo}")
    print(f"La cantiad de hojas del usuario es {cantidadhojas}")
    print(f"El valor de las hojas es {valorFinal}")'''

#/////////////////////////////CICLO FOR///////////////////

print("bienvenido")
capacidad = int(input("digite para cuantas personas va a hacer el programa"))
for x in range(1, capacidad +1):
    nombre = str(input("Digite su nombre"))
    tipo = int(input("Digite su tipo"))
    descuento = 0
    if tipo == 1:
        print("se le descuenta el 5%")
        descuento = 0.05
    elif tipo == 2:
        print("se le descuenta el 8%")
        descuento = 0.08
    elif tipo == 3:
        print("se le descuenta el 12%")
        descuento = 0.12
    elif tipo == 4:
        print("se le descuenta el 15%")
        descuento = 0.15
    else:
        print("ese dato es un error vuelve a intartalo nuevamente")
        break
    cantidadhojas= int(input("Cuantas hojas compro"))
    preciohojas = int(input("el valor de las hojas es"))
    valorsubFinal = (cantidadhojas * preciohojas)
    valorFinal =  int(valorsubFinal - (valorsubFinal* descuento))
    print(f"El nombre del usuario es {nombre}")
    print(f"El tipo del usuario es {tipo}")
    print(f"La cantiad de hojas del usuario es {cantidadhojas}")
    print(f"El valor de las hojas es {valorFinal}")