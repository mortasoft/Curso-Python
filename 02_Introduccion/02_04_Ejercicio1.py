
porcentaje_tareas = 0.25
porcentaje_quices = 0.25
porcentaje_examen_final = 0.50

"""
tarea1 = input("Digite la tarea 1: ")
tarea2 = input("Digite la tarea 2: ")
tarea3 = input("Digite la tarea 3: ")
quiz1 = input("Digite la tarea 1: ")
quiz2 = input("Digite la tarea 2: ")
examenFinal = input("Digite la tarea 3: ")
"""

tarea1 = 100
tarea2 = 80
tarea3 = 70
quiz1 = 80
quiz2 = 70
examenFinal = 85

notaFinal = ((tarea1+tarea2+tarea3)/3 * porcentaje_tareas) + ((quiz1+quiz2)/2 * porcentaje_quices) + (examenFinal* porcentaje_examen_final)

print(f"Su nota final es: {notaFinal:.2f}")