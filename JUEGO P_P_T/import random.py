import random
import time

OPCIONES = ["piedra", "papel", "tijera"]

REGLAS = (
    ("piedra", "tijera"),
    ("papel", "piedra"),
    ("tijera", "papel")
)

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige piedra, papel o tijera: ").strip().lower()

        if opcion.isnumeric():
            print("No se permiten numeros.")
            continue

        if opcion in OPCIONES:
            return opcion
        else:
            print("Opcion no valida.")

def obtener_opcion_computadora():
    print("La computadora esta eligiendo...")
    time.sleep(1)
    return random.choice(OPCIONES)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    elif (usuario, computadora) in REGLAS:
        return "usuario"
    else:
        return "computadora"

def preguntar_reinicio():
    while True:
        respuesta = input("Desea jugar otra vez? (s/n): ").strip().lower()

        if respuesta.isnumeric():
            print("No se permiten numeros.")
            continue

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Debe ingresar solo 's' o 'n'.")

def jugar():
    print("===================================")
    print(" Juego Piedra, Papel o Tijera ")
    print("===================================")
    time.sleep(1)

    while True:
        puntos_usuario = 0
        puntos_computadora = 0
        empates = 0
        ronda = 1
        MAX_RONDAS = 3

        while ronda <= MAX_RONDAS:
            print("\nRonda", ronda)
            usuario = obtener_opcion_usuario()
            computadora = obtener_opcion_computadora()

            print("La computadora eligio:", computadora)
            time.sleep(1)

            resultado = determinar_ganador(usuario, computadora)

            if resultado == "usuario":
                puntos_usuario += 1
                print("Gana el usuario")
            elif resultado == "computadora":
                puntos_computadora += 1
                print("Gana la computadora")
            else:
                empates += 1
                print("Empate")

            ronda += 1
            time.sleep(1)

        print("\n===== Resultados Finales =====")
        print("Puntos usuario:", puntos_usuario)
        print("Puntos computadora:", puntos_computadora)
        print("Empates:", empates)

        if puntos_usuario > puntos_computadora:
            print("Ganador final: Usuario")
        elif puntos_computadora > puntos_usuario:
            print("Ganador final: Computadora")
        else:
            print("Resultado final: Empate")

        time.sleep(1)

        if not preguntar_reinicio():
            print("Fin del juego.")
            break

# Inicio del programa
jugar()