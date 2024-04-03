notas = []
print("Bienvenido estas son las notas\na, b, c, d, e")
n = str(input("Digite las notas en este sola linea con comas  "))
listan = n.split(',')
print(listan)
notasu = sorted(set(listan))
print(notasu)

for nota in notasu:
    cantidad = listan.count(nota)
    notas.append(cantidad)

print("Notas únicas tocadas:")
print(" ".join(notasu))
print("Cantidad de veces tocadas:")
print(" ".join(map(str, notas)))


