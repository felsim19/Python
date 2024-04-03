#////////////////////////////////CICLO WHILE/////////////////////////////////////

'''print("Bienvenido coloque el numero que quiere factorizar")
numero = int(input("Ingrese el numero "))
Contador = numero - 1
resultado = numero * Contador
resultadox = 0
print(f"el numero es {numero} entonces empieza en el numero {Contador} y el resultado {resultado}")
while Contador > 1:
    Contador -= 1
    resultadox += int(resultado * Contador)
    print(f"el numero es {numero} entonces empieza en el numero {Contador} y el resultado {resultadox}")'''

    
#///////////////////////////////////////////CICLO FOR/////////////////////////////////
    
print("Bienvenido coloque el numero que quiere factorizar")
numero = int(input("Ingrese el numero "))
for x in range(1,numero):
    numero *= x
    print(f"el numero es {numero}") 
