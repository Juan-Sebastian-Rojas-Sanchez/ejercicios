import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número (entre 1 y 10): "))

if intento == numero_secreto:
    print("¡Correcto!")
elif intento < numero_secreto:
    print("El número es mayor.")
else:
    print("El número es menor.")
