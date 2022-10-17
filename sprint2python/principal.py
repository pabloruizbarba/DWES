from factorial import func_factorial

num = int(input("Introduzca un número positivo: "))
if num < 0:
    print("Ese número es negativo, no es válido.")
else:
    print("El factorial de ",num," es: ",func_factorial(num))