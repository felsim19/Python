'''milista = [1,2,3,4, "hola", 1.8, "aaa", "a", True, [10, 22, 75]]
print(milista[:2])

milista[1]=["Nuevo dató"]
print(milista)'''

midatos=[]
ndatos= int(input("numero de datos"))
for i in range(ndatos):
    nombre=str(input("Ingrese el nombre"))
    midatos.append(nombre)
print(midatos)

buscardato= input("digite el dato de buscar")

if buscardato in midatos:
    ind= midatos.index(buscardato)
    print(ind)
else:
    print("no esta")

buscardatoe= input("digite el dato de buscar")

if buscardatoe in midatos:
    ind= midatos.remove(buscardato)
    print(ind)
else:
    print("no esta")