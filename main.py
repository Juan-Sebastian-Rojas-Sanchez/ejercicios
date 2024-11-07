# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))  # El usuario ingresa un número

# Inicializamos una variable para  factorial
factorial = 1  # Comenzamos con 1

# Utilizamos un ciclo 'for' para sumar los primeros n números enteros
for i in range(1, n + 1):  # El rango va de 1 a n (inclusive)
    factorial = factorial*i  # calculamos factorial

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {factorial}")
