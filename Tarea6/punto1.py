print("Bienvenido en este aplicacion los estudiantes podran gestionar notas de su materia")
Nombre = str(input("Por favor ingrese su nombre "))
materia = str(input("Ingrese el nombre de la materia "))
promedio = 0
accumulatoNote = 0
mensaje = ""


def accumulatolNote(UserNote, UserAvarerage):
    global accumulatoNote, promedio
    nota = UserNote
    prom = UserAvarerage
    if promedio + prom <= 100:
        accumulatoNote += nota * prom
        promedio += prom
    else:
        print("El pocentaje evaluado no puede ser mayor a 100")
        accumulatoNote += 0
        promedio += 0 

    
def FinalNote():
    global accumulatoNote, promedio
    final = round(accumulatoNote,2)/100
    return final

def resultado (x):
    global mensaje
    if (x > 3.5):
        mensaje = "Aprobado"
    else:
        mensaje = "No aprovado "
    

def validarp(promedio):
    global x, Nombre, materia, mensaje
    print(f"el promedio es {promedio}")
    if promedio > 100:
        print("El pocentaje evaluado no puede ser mayor a 100")
    elif(promedio == 100):
        print("Usted a tenido el 100 de su porcentaje")
        print(f"el estudiante {Nombre} curso la materia {materia} y obutvo {x} resultado en {mensaje}")
        return False
    return True

def validarQ(UserQuetion):
    global  x, Nombre, materia, mensaje
    if UserQuetion == "n":
        print(f"el estudiante {Nombre} curso la materia {materia} y obutvo {x} resultado en {mensaje}")
        return False
    return True

while True:
    UserNote = float(input("Ingrese la nota "))
    UserAvarerage = int(input("Ingrese el porcentaje "))
    accumulatolNote(UserNote, UserAvarerage)
    x = FinalNote()
    resultado(x)
    if not validarp(promedio):
        break
    UserQuetion = str(input("falta añadir notas? s/n"))
    if not validarQ(UserQuetion):
        break
    







