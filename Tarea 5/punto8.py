print("Bienvenido este programa dara la informacion de temperatura")
temperatura_maxima = []
temperatura_minima = []
temperatura_media = []
dia = 1
menor = 100

for i in range(1,6):
    temp_max = int(input(f"Ponga la temperatura maxima del dia {dia} "))
    temperatura_maxima.append(temp_max)
    temp_men = int(input(f"Ponga la temperatura minima del dia {dia} "))
    temperatura_minima.append(temp_men)
    temp_med = float((temp_max + temp_men) / 2)
    temperatura_media.append(temp_med)
    dia += 1

dia = 1

for z in temperatura_media:
    print(f"la temperatura media del dia {dia} es de {z}")
    dia += 1

for i in range(len(temperatura_minima)):
    if temperatura_minima[i] < menor:
        menor = temperatura_minima[i]

print(f"el dia de menor temperatura fue el {menor}")

usuarios_temperatura = int(input("Digite su temperatura "))

if usuarios_temperatura in temperatura_maxima:
    dias_coincidentes = [i + 1 for i in range(len(temperatura_maxima)) if temperatura_maxima[i] == usuarios_temperatura]
    
    if len(dias_coincidentes) == 1:
        print(f"La temperatura máxima coincide con el día {dias_coincidentes[0]}")
    else:
        print(f"La temperatura máxima coincide con los días {', '.join(map(str, dias_coincidentes))}")
else:
    print("Ningún día ha coincidido con esta temperatura máxima.")
    



