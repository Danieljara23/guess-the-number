print("Hola mundo")
import random

def game():
    # Generar el número secreto entre 1 y 100
    numero_secreto = random.randint(1, 100)

    jugador_adivino = False
    ordenador_adivino = False

    print("¡Bienvenido al juego de adivinanza!")
    
    # Bucle del juego
    while not jugador_adivino and not ordenador_adivino:
        # Turno del jugador
        try:
            jugador_intento = int(input("Adivina el número (entre 1 y 100): "))
            if jugador_intento < 1 or jugador_intento > 100:
                print("El número debe estar entre 1 y 100.")
                continue
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Comparar la entrada del jugador con el número secreto
        if jugador_intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            jugador_adivino = True
        elif jugador_intento < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        # Si el jugador adivinó correctamente, termina el juego
        if jugador_adivino:
            break

        # Turno del ordenador
        ordenador_intento = random.randint(1, 100)
        print(f"El ordenador adivina: {ordenador_intento}")

        # Comparar el intento del ordenador con el número secreto
        if ordenador_intento == numero_secreto:
            print("¡El ordenador adivinó correctamente!")
            ordenador_adivino = True
        elif ordenador_intento < numero_secreto:
            print("El número secreto es mayor que la suposición del ordenador.")
        else:
            print("El número secreto es menor que la suposición del ordenador.")

# Ejecutar el juego
if __name__ == "__main__":
    game()
