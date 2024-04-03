print("Bienvenido este programa le dira si necesita un prestamo")
saldo = int(input("ponga su sueldo actual"))

if saldo < 0 :
    print("su saldo esta negativo")
    saldo = 10000
    print("usted quedo con un saldo de ", str(saldo))
    equipo_computo = 5000
    print("usted para el equipo de computo dejo ", str(equipo_computo))
    mobilirario = 2000
    print("usted para el mobilario dejo ", str(mobilirario))
    sobrante = saldo - equipo_computo - mobilirario
    Compra_insumos = int(sobrante/2)
    print("usted para la compra de insumo dejo ", str(Compra_insumos))
    Incentivos_presonal = int(sobrante/2)
    print("usted para el incentivo personal dejo ", str(Incentivos_presonal))
elif saldo < 20000:
    print("su saldo esta postivo")
    saldo = 20000
    print("usted quedo con un saldo de ", str(saldo))
    equipo_computo = 5000
    print("usted para el equipo de computo dejo ", str(equipo_computo))
    mobilirario = 2000
    print("usted para el mobilario dejo ", str(mobilirario))
    sobrante = saldo - equipo_computo - mobilirario
    Compra_insumos = int(sobrante/2)
    print("usted para la compra de insumo dejo ", str(Compra_insumos))
    Incentivos_presonal = int(sobrante/2)
    print("usted para el incentivo personal dejo ", str(Incentivos_presonal))
elif saldo > 20000:
    print("su saldo esta positivo no necesita ningun prestamo")
    print("usted quedo con un saldo de ", str(saldo))
    equipo_computo = 5000
    print("usted para el equipo de computo dejo ", str(equipo_computo))
    mobilirario = 2000
    print("usted para el mobilario dejo ", str(mobilirario))
    sobrante = saldo - equipo_computo - mobilirario
    Compra_insumos = int(sobrante/2)
    print("usted para la compra de insumo dejo ", str(Compra_insumos))
    Incentivos_presonal = int(sobrante/2)
    print("usted para el incentivo personal dejo ", str(Incentivos_presonal))