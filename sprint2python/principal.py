from factorial import func_factorial
from factorial2 import func_factorial2


print("Calculadora de Factoriales")
print("a) Con recursividad.")
print("b) Sin recursividad.")
op=input("Elija una opción (a/b): ")

if op.lower() == "a":
    num = int(input("Introduzca un número positivo: "))
    if num < 0:
        print("Ese número es negativo, no es válido.")
    else:
        print("El factorial de ",num," es: ",func_factorial(num))
elif op.lower() == "b":
    num = int(input("Introduzca un número positivo: "))
    if num < 0:
        print("Ese número es negativo, no es válido.")
    else:
        print("El factorial de ",num," es: ",func_factorial2(num))
else:
    print("Opción incorrecta")