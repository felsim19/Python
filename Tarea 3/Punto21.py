monto_compra = float(input("Ingrese el monto total de la compra de refacciones: "))
forma_pago = ""

if monto_compra > 500000:
    inversion_propia = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra * 0.15
    forma_pago = f"Inversión propia: ${inversion_propia}, Préstamo del banco: ${prestamo_banco}, Crédito del fabricante: ${credito_fabricante}"
else:
    inversion_propia = monto_compra * 0.70
    credito_fabricante = monto_compra * 0.30
    forma_pago = f"Inversión propia: ${inversion_propia}, Crédito del fabricante: ${credito_fabricante}"

print(f"Forma de pago: {forma_pago}")
