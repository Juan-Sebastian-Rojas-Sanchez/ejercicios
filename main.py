temp = float(input("Ingresa la temperatura: "))
escala = input("Ingresa la escala (C para Celsius, F para Fahrenheit): ")

match escala:
    case 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"Temperatura en Fahrenheit: {fahrenheit}")
    case 'F':
        celsius = (temp - 32) * 5/9
        print(f"Temperatura en Celsius: {celsius}")
    case _:
        print("Escala no válida.")
