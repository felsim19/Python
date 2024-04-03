
total_compra = int(input("Digite el valor el producto sin descuento "))
descuento = total_compra * 0.15
total_pagar = total_compra - descuento
print(f"El descuento del producto es ${descuento}")
print(f"El cliente deberá pagar ${total_pagar} finalmente por su compra.")
