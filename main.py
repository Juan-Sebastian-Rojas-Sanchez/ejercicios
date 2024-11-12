num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

match operacion:
    case '+':
        print("Resultado:", num1 + num2)
    case '-':
        print("Resultado:", num1 - num2)
    case '*':
        print("Resultado:", num1 * num2)
    case '/':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("No se puede dividir por cero.")
    case _:
        print("Operación no válida.")
