edad = int(input("Ingresa la edad: "))
if 0 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
else:
    print("Anciano")
