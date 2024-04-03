print("Bienvenido")
curso = int(input("Bienevenido digite su grado "))
materia1 = str(input("Digite su materia numero uno "))
nota1M1 = float(input("Digite su nota "))
nota2M1 = float(input("Digite su nota "))
nota3M1 = float(input("Digite su nota "))
nota4M1 = float(input("Digite su nota "))
notaFM1 = (nota1M1 + nota2M1 + nota3M1 + nota4M1) / 4

if notaFM1 > 0 and notaFM1< 1:
    print("Su promedio es D")
elif notaFM1 < 2.9:
    print("Su promedio es I")
elif notaFM1 < 3.8:
    print("Su promedio es A")
elif notaFM1 < 4.6:
    print("Su promedio es S")
elif notaFM1 < 5.0:
    print("Su promedio es E")

materia2 = str(input("Digite su materia numero dos "))
nota1M2 = float(input("Digite su nota "))
nota2M2 = float(input("Digite su nota "))
nota3M2 = float(input("Digite su nota "))
nota4M2 = float(input("Digite su nota "))
notaFM2 = (nota1M2 + nota2M2 + nota3M2 + nota4M2) / 4

if notaFM2 > 0 and notaFM2< 1:
    print("Su promedio es D")
elif notaFM2 < 2.9:
    print("Su promedio es I")
elif notaFM2 < 3.8:
    print("Su promedio es A")
elif notaFM2 < 4.6:
    print("Su promedio es S")
elif notaFM2 < 5.0:
    print("Su promedio es E")

materia3 = str(input("Digite su materia numero tres "))
nota1M3 = float(input("Digite su nota "))
nota2M3 = float(input("Digite su nota "))
nota3M3 = float(input("Digite su nota "))
nota4M3 = float(input("Digite su nota "))
notaFM3 = (nota1M3 + nota2M3 + nota3M3 + nota4M3) / 4

if notaFM3 > 0 and notaFM3< 1:
    print("Su promedio es D")
elif notaFM3 < 2.9:
    print("Su promedio es I")
elif notaFM3 < 3.8:
    print("Su promedio es A")
elif notaFM3 < 4.6:
    print("Su promedio es S")
elif notaFM3 < 5.0:
    print("Su promedio es E")

materia4 = str(input("Digite su materia numero cuatro "))
nota1M4 = float(input("Digite su nota "))
nota2M4 = float(input("Digite su nota "))
nota3M4 = float(input("Digite su nota "))
nota4M4 = float(input("Digite su nota "))
notaFM4 = (nota1M4 + nota2M4 + nota3M4 + nota4M4) / 4

if notaFM4 > 0 and notaFM4< 1:
    print("Su promedio es D")
elif notaFM4 < 2.9:
    print("Su promedio es I")
elif notaFM4 < 3.8:
    print("Su promedio es A")
elif notaFM4 < 4.6:
    print("Su promedio es S")
elif notaFM4 < 5.0:
    print("Su promedio es E")

PromedioFinal = (notaFM1 + notaFM2 + notaFM3 + notaFM4)/4

if PromedioFinal >= 3.5:
    curso += 1
    if curso > 11:
        print("Felicidades ustes se ha graduado")
    else:
        print(f"Felicidades usted a sido promovido a el curso {curso}")
else:
    print("Usted no ha sido promovido")