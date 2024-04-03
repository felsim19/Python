print("Bienvenido usuario, este programa es para calcular tu salario")

salario_basico = int(input("Digite su salario basico mensual: "))
hora_extra_diurna = int(input("Digite las horas extras diurnas: "))
hora_extra_nocturna = int(input("Digite las horas extras nocturnas: "))
hora_extra_festivas = int(input("Digite las horas extras festivas: "))
hora_extra_dominicales = int(input("Digite las horas extras dominicales: "))
descuento_dias = int(input("Digite los días que no trabajó: "))

hora_normal = salario_basico / 30 / 8
promedio_diurna = round((hora_normal * 1.25) * hora_extra_diurna)
promedio_nocturna = round((hora_normal * 1.35) * hora_extra_nocturna)
promedio_festivas = round((hora_normal * 1.75) * hora_extra_festivas)
promedio_dominicales = round((hora_normal * 2) * hora_extra_dominicales)
promedio_descuento = round(descuento_dias * 8 * hora_normal)

salario_subtotal = round(salario_basico + promedio_diurna + promedio_nocturna + promedio_festivas + promedio_dominicales - promedio_descuento)
descuento_salud = round(salario_subtotal * 0.04)
descuento_pension = round(salario_subtotal * 0.04)
salario_total = salario_subtotal - descuento_salud - descuento_pension

print("Su Salario es de", salario_basico)
print("Sus horas extras diurnas salen por", promedio_diurna)
print("Sus horas extras nocturnas salen por", promedio_nocturna)
print("Sus horas extras festivas salen por", promedio_festivas)
print("Sus horas extras dominicales salen por", promedio_dominicales)
print("Se descuenta por haber faltado", promedio_descuento)
print("Su Salario subtotal con extras es de", salario_subtotal)
print("Se descuenta de salud", descuento_salud)
print("Se descuenta de pensión", descuento_pension)
print("Su salario total es de", salario_total)
