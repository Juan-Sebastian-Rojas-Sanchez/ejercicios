# Solicitar salario bruto y país de residencia
salario_bruto = float(input("Ingrese su salario bruto: "))
pais = input("Ingrese su país de residencia (País A, País B, País C): ")

# Aplicar impuestos según el país
if pais == "País A":
    impuesto = 0.20
elif pais == "País B":
    impuesto = 0.15
elif pais == "País C":
    impuesto = 0.10
else:
    impuesto = 0.25

salario_neto = salario_bruto * (1 - impuesto)
print(f"Su salario neto es: {salario_neto}")
