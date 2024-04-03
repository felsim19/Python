precio_compra = int(input("Digite el valor de su compra"))
if precio_compra >= 500000:
    descuento = precio_compra * 0.20  
else:
    descuento = 0

total_pagar = precio_compra - descuento
print(f"El total a pagar con el descuento aplicado es: ${total_pagar}")
