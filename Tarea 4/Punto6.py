#////////////////////////////////////////CICLO WHILE////////////////////////7

'''Cantidad= int(input("Cuanto digitos desea digitar"))
conador = 1
menor = 9000
mayor = 0
while conador != Cantidad:
    numero = int(input("Ingrese el numero "))
    if menor > numero:
        menor = numero
    if mayor < numero:
        mayor = numero
    conador += 1
print(f"el numero menor es {menor}")
print(f"el numero mayor es {mayor}")'''

#////////////////////////////////////CICLO FORD//////////////////////////

Cantidad = int(input("Cuanto digitos desea digitar "))
men = 9000
may = 0
for i in range(1,Cantidad + 1,1):
    numero = int(input("Ingrese el numero "))
    if men > numero:
        men = numero
    if may < numero:
        may = numero
print(f"el numero menor es {men}")
print(f"el numero mayor es {may}")
        

