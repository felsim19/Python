horas_trabajadas = int(input("Ingrese el número de horas trabajadas en la semana: "))
pago_por_hora = 16  
if horas_trabajadas <= 40:
    salario_semanal = horas_trabajadas * pago_por_hora
else:
    horas_extra = horas_trabajadas - 40
    salario_semanal = (40 * pago_por_hora) + (horas_extra * 20)  

print(f"el obrero trabajo {horas_extra} de horas extras ")
print(f"El salario semanal del obrero es: ${salario_semanal}")
