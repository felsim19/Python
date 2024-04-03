cantidad_camisas = int(input("Ingrese la cantidad de camisas. "))
precio_camisa = float(input("Ingrese el precio de las camisas "))
total_compra = cantidad_camisas * precio_camisa
if cantidad_camisas >= 3:
    descuento = total_compra * 0.20 
else:
    descuento = total_compra * 0.10

total_pagar = total_compra - descuento
print(f"Total a pagar por la compra de camisas: ${total_pagar}")
