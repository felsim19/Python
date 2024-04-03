#//////////////////////////////////CICLO WHILE///////////////////////

'''Numero_Tabla = int(input("Ponga el numero de la tabla de multiplicar que quiere "))
Inicio_numero = int(input("Desde donde quiere que inicie a multiplicar "))
Final_numero = int(input("Donde quiere que pare "))
while Inicio_numero != Final_numero + 1:
    resultado = Numero_Tabla * Inicio_numero
    print(f"{Numero_Tabla} x {Inicio_numero} = {resultado}")
    Inicio_numero += 1'''
    

#/////////////////////////////////////////CICLO FOR/////////////////////////////////

Numero_T = int(input("Ponga el numero de la tabla de multiplicar que quiere "))
Inicio_n = int(input("Desde donde quiere que inicie a multiplicar "))
Final_n = int(input("Donde quiere que pare "))
for Inicio_n in range(Inicio_n, Final_n + 1):
    resultado = Numero_T * Inicio_n
    print(f"{Numero_T} * {Inicio_n} = {resultado}")