total_compra = float(input("Ingrese el total de la compra en el supermercado: "))
descuento = 0
numero_escogido = int(input("Ingrese el número escogido al azar: "))
if numero_escogido < 74:
    descuento = total_compra * 0.15 
else:
    descuento = total_compra * 0.20 

print(f"Descuento: ${descuento}")
