import random

def jugar():
    while True:
        random_number = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
        print("He generado un número entre 1 y 100. ¡Intenten adivinarlo!")

        # Inicializa listas para registrar suposiciones
        suposiciones_jugador = []
        suposiciones_computador = []

        jugando = True
        while jugando:
            # Turno del jugador
            player = int(input("Ingresa un número: "))
            suposiciones_jugador.append(player)  # Guarda la suposición del jugador

            if player == random_number:
                print("¡Ganaste! TESOOOOO El número era:", random_number)
                jugando = False
            elif player < random_number:
                print("Tu número es menor.")
            else:
                print("Tu número es mayor.")

            # Turno del computador
            if jugando:  # Solo si el jugador no adivinó
                player_computador = random.randint(1, 100)
                suposiciones_computador.append(player_computador)  # Guarda la suposición del computador
                print(f"El computador adivina el numero: {player_computador}")

                if player_computador == random_number:
                    print(f"El computador ganó.CRACK-MAQUINA El número era: {random_number}")
                    jugando = False
                elif player_computador < random_number:
                    print("La suposición del computador es menor.")
                else:
                    print("La suposición del computador es mayor.")

        # Muestra las suposiciones de ambos
        print("\nSuposiciones del jugador:", suposiciones_jugador)
        print("Suposiciones del computador:", suposiciones_computador)

        # Pregunta si el usuario quiere jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if _name_ == "_main_":
    jugar()