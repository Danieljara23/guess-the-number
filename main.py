import random

# Genera un número aleatorio entre 1 y 100
random_number = random.randint(1, 100)

def jugar():

    playing = True
    turno_jugador = True  # Variable para alternar entre jugador y ordenador
    sucesos_jugador = []
    sucesos_ordenador = []

    while playing:
        if turno_jugador:
            
            # Turno del jugador
            
            guess = int(input("Ingresa el número: "))
            sucesos_jugador.append(guess)  # Guarda la suposición del jugador
            if guess == random_number:
                print("¡Ganaste! Adivinaste el número.")
                print("")
                playing = False
            elif guess > random_number:
                print("El número debe ser menor.")
                print("")
            elif guess < random_number:
                print("El número debe ser mayor.")
                print("")
        else:
            
            # Turno del ordenador
            
            guess_ordenador = random.randint(1, 100)
            sucesos_ordenador.append(guess_ordenador)  # Guarda la suposición del ordenador
            print(f"El ordenador adivina: {guess_ordenador}")
            print("")
            if guess_ordenador == random_number:
                print("El ordenador ha adivinado el número. ¡El ordenador gana!")
                print("")
                playing = False
            elif guess_ordenador > random_number:
                print("El número debe ser menor (según el ordenador).")
                print("")
            elif guess_ordenador < random_number:
                print("El número debe ser mayor (según el ordenador).")
                print("")
        
        # Alterna el turno entre jugador y ordenador
        turno_jugador = not turno_jugador

    # Al finalizar, muestra las suposiciones de ambos
    print(f"Las suposiciones del jugador fueron: {sucesos_jugador}")
    print("====================================================================")
    print(f"Las suposiciones del ordenador fueron: {sucesos_ordenador}")

# Funcion para preguntar si desea volver a jugar

def volver_a_jugar():
    while True:
        jugar()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

volver_a_jugar()