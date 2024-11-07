## Pedir una cadena de texto al usuario
cadena = input("Introduce una cadena de texto: ")

# Inicializar el contador de vocales en 0
contador_vocales = 0

# Recorrer cada letra de la cadena
for letra in cadena:
    # Comprobar si la letra es una vocal
    if letra.lower() in 'aeiou':  # Usamos .lower() para manejar mayúsculas y minúsculas
        contador_vocales += 1  # Aumentar el contador si es una vocal

# Mostrar el resultado
print(f"La cantidad de vocales en la cadena es: {contador_vocales}")