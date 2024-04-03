salario_mensual = float(input("Ingrese su salario mensual: "))
porcentaje_deposito = float(input("Ingrese el porcentaje de su salario a depositar en el SAR: "))
deposito_mensual = salario_mensual * (porcentaje_deposito / 100)
salario_despues_deposito = salario_mensual - deposito_mensual
print(f"Depósito mensual en el SAR: ${deposito_mensual}")
print(f"Salario mensual después del depósito en el SAR: ${salario_despues_deposito}")
