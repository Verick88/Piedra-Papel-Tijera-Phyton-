import random

movimientos = ["piedra", "papel", "tijera"]

puntos_usuario = 0
puntos_ia = 0

while puntos_usuario < 3 and puntos_ia < 3:

    movimiento_ia = random.choice(movimientos)
    movimiento_usuario = input("Introduce tu movimiento (PIEDRA/PAPEL/TIJERA): ")

    if movimiento_usuario.lower() not in movimientos:
        print ("EL MOVIMIENTO NO ESTA PERMITIDO")
        quit()

    print (f"HAS SACADO {movimiento_usuario}")
    print (f"EL ORDENADOR HA SACADO {movimiento_ia}")

    if movimiento_usuario.lower() == "piedra":
        if movimiento_ia == "piedra":
            print("EMPATE")
        elif movimiento_ia == "papel":
            print ("HAS PERDIDO")
            puntos_ia += 1
        elif movimiento_ia == "tijera":
            print ("HAS GANADO")
            puntos_usuario +=1
    elif movimiento_usuario.lower() == "papel":
        if movimiento_ia == "piedra":
            print("HAS GANADO")
            puntos_usuario +=1
        elif movimiento_ia == "papel":
            print ("EMPATE")
        elif movimiento_ia == "tijera":
            print ("HAS PERDIDO")
            puntos_ia +=1
    elif movimiento_usuario.lower() == "tijera":
        if movimiento_ia == "piedra":
            print("HAS PERDIDO")
            puntos_ia +=1
        elif movimiento_ia == "papel":
            print ("HAS GANADO")
            puntos_usuario+=1
        elif movimiento_ia == "tijera":
            print ("EMPATE")

    print (f"MARCADOR: {puntos_usuario} - {puntos_ia}" )

if puntos_usuario > puntos_ia:
    print (f"Enhorabuena! Has ganado a la inteligencia artificial con un magnifico resultado de: {puntos_usuario} - {puntos_ia}")
else: 
    print (f"Lo siento! Has perdido contra la inteligencia artificial con un desastroso resultado de: {puntos_usuario} - {puntos_ia}")