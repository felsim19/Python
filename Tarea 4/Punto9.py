#//////////////////////////////CICLO WHILE/////////////////////////////////

'''numero_x = int(input("Coloque cual tabla va ejecutar "))
numero_Y = int(input("Coloque hasta que numero va a ir "))
contador = 0
while contador != numero_Y:
    contador += 1
    multiplicacion = contador * numero_x
    print(f"el numero es {numero_x} y el numero con el que se va multiplicar es {contador} y el resultado es {multiplicacion}")'''


#///////////////////////////////////////CICLO FORD/////////////////////////////

x = int(input("Coloque cual tabla va ejecutar "))
Y = int(input("Coloque hasta que numero va a ir "))
for i in range(1,Y + 1):
    multiplicar = x*i
    print(f"{x} x {i} = {multiplicar}")
    