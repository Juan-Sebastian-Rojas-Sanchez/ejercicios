# Solicitar calificación y si hizo tareas adicionales
calificacion = float(input("Ingrese la calificación del estudiante: "))
tareas_adicionales = input("¿El estudiante hizo tareas adicionales? (sí/no): ").lower()

# Calcular bonificación
if tareas_adicionales == "sí":
    calificacion_final = min(calificacion * 1.05, 100)
else:
    calificacion_final = calificacion

print(f"La calificación final es: {calificacion_final}")
