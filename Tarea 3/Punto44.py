saldo_actual = float(input("Ingrese el saldo actual de la empresa: "))
capital_actual = float(input("Ingrese el capital actual de la empresa: "))

if saldo_actual < 0:
    monto_prestamo = 100000000 - saldo_actual
elif saldo_actual > 2000000000:
    monto_prestamo = 0
else:
    monto_prestamo = 200000000 - saldo_actual

equipo_computo = 50000000
mobiliario = 20000000
restante = (capital_actual - monto_prestamo) / 2
compra_insumos = restante
incentivos_personal = restante

print(f"Para el próximo año, la empresa destinará")
print(f"- ${equipo_computo} para equipo de cómputo")
print(f"- ${mobiliario} para mobiliario")
print(f"- ${compra_insumos} para la compra de insumos")
print(f"- ${incentivos_personal} para incentivos al personal")
print(f"Se pedirá un préstamo de ${monto_prestamo} al banco.")