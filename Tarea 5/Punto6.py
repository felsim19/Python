print("bienvenido este programa declarara dos lista y la tercecra sera automatica")
lista1 = []
lista2 = []
lista3 = []
for z in range(1,6):
    numeros_Lista1 = int(input("Digite los numeros de la lista uno "))
    lista1.append(numeros_Lista1)
    numeros_Lista2 = int(input("Digite los numeros de la lista dos "))
    lista2.append(numeros_Lista2)
    numeros_Lista3 = numeros_Lista1 + numeros_Lista2
    lista3.append(numeros_Lista3)
print("la lista uno tiene los numeros")
for a in lista1:
    print(a)
print("la lista dos tiene los numeros")
for b in lista2:
    print(b)
print("la lista tres tiene los numeros")
for c in lista3:
    print(c)

