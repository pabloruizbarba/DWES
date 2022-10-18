import random

print("Bienvenido a Piedra, Papel, Tijera")
empate=0
def fpiedra(empate):   
    print("Piedra, papel, tijera...")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    respuesta=int(input("Elije una opción (1/2/3): "))
    maquina=random.randint(1,3)
    if respuesta == 1:
        print("Jugador: Piedra")
    if respuesta == 2:
        print("Jugador: Papel")
    if respuesta == 3:
        print("Jugador: Tijera")
    if maquina == 1:
        print("Máquina: Piedra")
    if maquina == 2:
        print("Máquina: Papel")
    if maquina == 3:
        print("Máquina: Tijera")

    if (respuesta == 1) and (maquina == 3):
        print ("Piedra gana a tijeras")
        empate=empate+1
    elif (respuesta == 3) and (maquina == 1):
        print ("Piedra gana a tijeras")
        empate=empate-1
    elif (respuesta == 2) and (maquina == 1):
        print ("Papel gana a piedra")
        empate=empate+1
    elif (respuesta == 1) and (maquina == 2):
        print ("Papel gana a piedra") 
        empate=empate-1
    elif (respuesta == 3) and (maquina == 2):
        print ("Tijera gana a papel")
        empate=empate+1
    elif (respuesta == 2) and (maquina == 3):
        print ("Tijera gana a papel") 
        empate=empate-1 
    else:
        print("Empate!")
    print("")
    print("")
    return empate

for i in range(0,5):
    empate=fpiedra(empate)
if empate>0:
    print("Eres el campeón")
elif empate<0:
    print("La máquina es la campeona")
else:
    print("Has empatado contra la máquina")
    while empate==0:
        empate=fpiedra(empate)
    if empate>0:
        print("Eres el campeón")
    elif empate<0:
        print("La máquina es la campeona")