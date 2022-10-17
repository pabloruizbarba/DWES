puntos=0
print("¿Cuántos Oscar ha ganado 'El retorno del Rey'?")
print("a) 12")
print("b) 11")
print("c) 13")
respuesta=input("Tu respuesta es (a/b/c): ")
if respuesta=="11" or respuesta.lower()=="b":
    print("¡Has acertado!")
    puntos = puntos + 10
else:
    print("Has fallado")
    puntos = puntos - 5
print("¿Cuántos años tiene Jack Nicholson?")
print("a) 85")
print("b) 86")
print("c) 87")
respuesta=input("Tu respuesta es (a/b/c): ")
if respuesta=="85" or respuesta.lower()=="a":
    print("¡Has acertado!")
    puntos = puntos + 10
else:
    print("Has fallado")
    puntos = puntos - 5
print("¿Como se llama actualmente la capital de Kazajistán?")
print("a) Akmola")
print("b) Astaná")
print("c) Nursultán")
respuesta=input("Tu respuesta es (a/b/c): ")
if respuesta=="Nursultán" or respuesta.lower()=="c":
    print("¡Has acertado!")
    puntos = puntos + 10
else:
    print("Has fallado")
    puntos = puntos - 5
print("Tu puntuación final es: ",puntos)