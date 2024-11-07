# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializamos una variable para la suma
suma = 0

# Utilizamos un ciclo 'for' para sumar los primeros n números enteros
for i in range(1, n + 1):  # El rango va de 1 a n (inclusive)
    suma += i  # Sumar el valor de i a la variable suma

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")