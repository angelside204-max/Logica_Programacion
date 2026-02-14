import random

print("Bienvenido al juego Piedra, Papel o Tijera")

usuario = input("Elige piedra, papel o tijera: ").lower()

opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

print("La computadora eligió:", computadora)

if usuario not in opciones:
    print("Opción no válida")
else:
    if usuario == computadora:
        print("Empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("Ganaste")
    else:
        print("Perdiste")
