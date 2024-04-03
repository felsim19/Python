#////////////////////////CICLO WHILE//////////////

'''Numero_x = int(input("Digite un número donde va a iniciar el rango: "))
Numero_y = int(input("Digite un número donde va a terminar el rango: "))

print(f"El rango menor es {Numero_x} y el rango mayor es {Numero_y}")

num = Numero_x
while num <= Numero_y:
    if num < 2:
        es_primo = False
    else:
        es_primo = True
        i = 2
        while i <= num**0.5:
            if num % i == 0:
                es_primo = False
                break
            i += 1

    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
    
    num += 1'''

#//////////////////////////////CICLO FOR//////////////////////////

Numero_x = int(input("Digite un número donde va a iniciar el rango: "))
Numero_y = int(input("Digite un número donde va a terminar el rango: "))

print(f"El rango menor es {Numero_x} y el rango mayor es {Numero_y}")

for i in range(Numero_x, Numero_y + 1):
    if i < 2:
        es_primo = False
    else:
        es_primo = True
        for x in range(2,int(i**0.5) + 1):
            if i % x == 0:
                es_primo = False
                break 

    if es_primo:
        print(f"{i} es un número primo.")
    else:
        print(f"{i} no es un número primo.")
