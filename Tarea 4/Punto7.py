#///////////////////////////////////// CICLO WHILE////////////////////

'''numero_Estrellas = int(input("Digite el numero de estrellas que desea "))
contador = 0
estrellas = ""
while contador != numero_Estrellas:
    estrellas += "*"
    contador += 1
    print(estrellas)'''

#///////////////////////////////////CICLO FORD///////////////////////////


numero_E = int(input("Digite el numero de estrellas que desea "))
estrellas = ""
for x in range(1, numero_E +1):
    estrellas += "*"
    print(estrellas)