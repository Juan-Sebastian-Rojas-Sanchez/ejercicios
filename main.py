# Solicitar distancia y velocidad
distancia = float(input("Ingrese la distancia a recorrer en km: "))
velocidad = float(input("Ingrese la velocidad promedio en km/h: "))

# Calcular tiempo en horas y minutos
tiempo_horas = distancia // velocidad
tiempo_minutos = (distancia % velocidad) * 60 / velocidad

if velocidad > 120:
    print("Advertencia: La velocidad es mayor a 120 km/h.")

print(f"El tiempo de viaje es aproximadamente {int(tiempo_horas)} horas y {int(tiempo_minutos)} minutos.")
