print("Bienvenido")
SistemaNotas =[]
mayor = 1
menor = 11
total = 0
promedio = 0
for x in range(1, 5 + 1):
    nota = float(input("Digite la nota solo notas de 0 a 10 "))
    if (nota > 10):
        print("la nota no puede ser mayor de 10 error")
        break
    elif(nota < 0):
        print("la nota no puede ser menor de 0 error")
        break
    
    if (mayor < nota):
        mayor = nota
    if (menor > nota):
        menor = nota
    SistemaNotas.append(nota)
    total += nota
promedio = total / x

for j in SistemaNotas:
    print(j)

print(f"El promedio total del estudiante fue {promedio}")
print(f"La nota mas alta del estudiante es {mayor}")
print(f"La nota mas baja del estudiante es {menor}")