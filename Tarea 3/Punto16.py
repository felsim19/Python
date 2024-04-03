inversion_inicial = float(input("Ingrese la cantidad inicial de la inversión en el banco: "))
intereses_generados = 0

if inversion_inicial > 0:
    intereses_generados = int(inversion_inicial * 0.04) 

saldo_final = int(inversion_inicial)
if intereses_generados > 70000: 
    saldo_final += intereses_generados

print(f"Los intereses generados son: ${intereses_generados}")
print(f"El saldo final de la inversión es: ${saldo_final}")
