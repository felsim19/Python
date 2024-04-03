puntos_imeca1 = int(input("Sume los puntos del primer dia")) 
puntos_imeca2 = int(input("Sume los puntos del primer dia")) 
puntos_imeca3 = int(input("Sume los puntos del primer dia")) 
puntos_imeca4 = int(input("Sume los puntos del primer dia")) 
puntos_imeca5 = int(input("Sume los puntos del primer dia")) 
promedio_puntos_imeca = (puntos_imeca1 + puntos_imeca2 + puntos_imeca3 + puntos_imeca4 + puntos_imeca5)/5

if promedio_puntos_imeca > 170:
    sancion = True
    multa = 0.5 
else:
    sancion = False
    multa = 0

print(f"Promedio de puntos IMECA: {promedio_puntos_imeca}")
if sancion:
    print("Se detiene la producción por una semana y se aplica una multa del 50% de las ganancias diarias.")
    print(f"Multa a pagar: {multa}")
else:
    print("No se aplica sanción ni multa.")
