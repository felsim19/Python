superficie_terreno = float(input("Ingrese la superficie del terreno en metros cuadrados: "))
metros_cuadrados_pino = 10
metros_cuadrados_oyamel = 15
metros_cuadrados_cedro = 18
arboles_por_hectarea = 10000 / (metros_cuadrados_pino + metros_cuadrados_oyamel + metros_cuadrados_cedro)

if superficie_terreno > 1000000:
    arboles_pino = 0.7 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_oyamel = 0.2 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_cedro = 0.1 * (superficie_terreno / 10000) * arboles_por_hectarea
else:
    arboles_pino = 0.5 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_oyamel = 0.3 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_cedro = 0.2 * (superficie_terreno / 10000) * arboles_por_hectarea

print(f"Número de pinos a sembrar: {arboles_pino}")
print(f"Número de oyameles a sembrar: {arboles_oyamel}")
print(f"Número de cedros a sembrar: {arboles_cedro}")
