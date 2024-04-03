cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))
precio_llanta = 80000 
total_pagar = 0
if cantidad_llantas < 5:
    total_pagar = cantidad_llantas * precio_llanta
else:
    total_pagar = cantidad_llantas * 70000  
print(f"Total a pagar por la compra de llantas: ${total_pagar}")
