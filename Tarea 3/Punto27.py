ingresos = float(input("Ingrese sus ingresos mensuales: "))
costo_casa = float(input("Ingrese el costo de la casa: "))
if ingresos < 8000:
    enganche = costo_casa * 0.15
    pagos_mensuales = costo_casa * 0.85 / (10*12)  
else:
    enganche = costo_casa * 0.30
    pagos_mensuales = costo_casa * 0.70 / (7*12)  
print(f"Enganche a pagar: ${enganche}")
print(f"Pagos mensuales a pagar: ${pagos_mensuales}")
