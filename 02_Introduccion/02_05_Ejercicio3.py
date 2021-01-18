# Planteo del problema
velocidad_inicial_km = 70
velocidad_final_km = velocidad_inicial_km/3
tiempo = 6

# Conversion de unidades
velocidad_inicial_ms = velocidad_inicial_km/3.6
velocidad_final_ms = velocidad_inicial_ms/3

# Calculo de la distancia
distancia = (velocidad_inicial_ms+velocidad_final_ms)/2 * tiempo
print(f"La distancia recorrida fue: {distancia:.2f}m" )

# Calculo de la aceleracion
aceleracion = (velocidad_inicial_ms+velocidad_final_ms)/tiempo
print(f"La aceleracion fue de : {aceleracion:.2f}m/s" )