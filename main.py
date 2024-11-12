# Solicitar el número de materias cursadas
materias = int(input("Ingrese el número de materias cursadas: "))
creditos_totales = 0

for i in range(materias):
    puntaje = float(input(f"Ingrese el puntaje de la materia {i+1}: "))
    if puntaje >= 60:
        creditos_totales += 3

print(f"El número total de créditos es: {creditos_totales}")
