print("Bienvenido al programa ponga un mes del año y le dire cuantos dias tiene y el nombre del mes")
meses = ["Enero","Febrero", "marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre" , "Noviembre" , "Diciembre" ]
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    numero = int(input("Digite el numero recuerde que solo es de 1 a 12 ")) - 1
    if numero > 12:
        print("No hay mas de doce meses ponga un numero valido")
    elif numero < 0:
        print("No hay menos de doce meses ponga un numero valido")
    else:
        print(f"el mes es {meses[numero]}")
        print(f"y los dias de ese mes son de {dias[numero]}")
        break