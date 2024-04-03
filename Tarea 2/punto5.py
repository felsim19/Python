print("Bienvenido usuario, este programa determinara el total de la colegiatura")
print("solo hay 2 tipos de estudiantes alumnos de profesional y alumno de preparatoria")
tipo_estudiante = int(input("Marque 0 para estudiante profesional o  marque 1 para estudiante de preparatoria "))
promedio = float(input("Coloque su promedio de 0 a 10 "))

if tipo_estudiante == 0:
    if promedio >= 9.5 and promedio <= 10:
        print("Felicidades usted podra cursar 55 unidades y tendra un descuento del 20%")
        unidades = 55
        valorUnidades = 300
        subtotal= (unidades/5) * valorUnidades
        descuento = subtotal *0.20
        total = subtotal - descuento
        print("Su total a pagar es de ", str(total))
    else:
        print("Felicidades usted podra cursar 55 unidades y no tiene descuento")
        unidades = 55
        valorUnidades = 300
        total= (unidades/5) * valorUnidades
        print("Su total a pagar es de ", str(total))  
elif tipo_estudiante == 1:
    Materias_reprobadas = int(input("cuantas materias reprobo?"))
    if promedio >= 9.5 and promedio <= 10:
        print("Felicidades usted podra cursar 55 unidades y tendra un descuento del 25%")
        unidades = 55
        valorUnidades = 180
        subtotal= (unidades/5) * valorUnidades
        descuento = subtotal *0.25
        total = subtotal - descuento
        print("Su total a pagar es de ", str(total))
    elif promedio >= 9:
        print("Felicidades usted podra cursar 50 unidades y tendra un descuento del 10%")
        unidades = 50
        valorUnidades = 180
        subtotal= (unidades/5) * valorUnidades
        descuento = subtotal *0.10
        total = subtotal - descuento
        print("Su total a pagar es de ", str(total))
    elif promedio > 7:
        print("Felicidades usted podra cursar 50 unidades y no tendra descuento")
        unidades = 50
        valorUnidades = 180
        total= (unidades/5) * valorUnidades
        print("Su total a pagar es de ", str(total))
    else :
        print("usted saco menos de 7")
        if Materias_reprobadas <= 3:
            print("usted podra cursar 45 unidades y no tendra descuento")
            unidades = 45
            valorUnidades = 180
            total= (unidades/5) * valorUnidades
            print("Su total a pagar es de ", str(total))
        else:
            print("usted podra cursar 40 unidades y no tendra descuento")
            unidades = 50
            valorUnidades = 180
            total= (unidades/5) * valorUnidades
            print("Su total a pagar es de ", str(total))
        
else:
    print("Lo siento no hay mas opciones")