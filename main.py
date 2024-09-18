import random  # Importa el módulo random

def explain_game():
    # Explica las reglas del juego
    print("¡Bienvenido al juego de adivinanza!")
    print("Debes adivinar un número entre 1 y 100.")
    print("La IA también intentará adivinar el número.")
    print("¡Buena suerte!\n")

def play_game():
    num_random = random.randint(1, 100)  # Genera un número aleatorio
    game = True
    intentos_user = []  # Creamos un vector para las suposiciones del usuario
    intentos_ia = []  # Creamos un vector para las suposiciones de la IA

    while game:
        num_usuario = int(input("Tu número: "))  
        num_ia = random.randint(1, 100)  

        intentos_user.append(num_usuario)  # Se guarda la suposición del usuario
        intentos_ia.append(num_ia)  # Se guarda la suposición de la IA

        print(f"Número de la IA: {num_ia}\n")

        if num_usuario == num_random:
            print("¡Lo lograste!")
            print("Felicidades\n")
            print(f"Tus suposiciones: {intentos_user}")
            print(f"Suposiciones de la IA: {intentos_ia}\n")
            game = False
        elif num_usuario > num_random:
            print("Pista: El número es menor")
        else:
            print("Pista: El número es mayor")

        if num_ia == num_random:
            print("¡Fallaste!")
            print("La IA encontró el número primero que tú\n")
            print(f"Tus suposiciones: {intentos_user}")
            print(f"Suposiciones de la IA: {intentos_ia}\n")
            game = False

    return jugar_de_nuevo()

def jugar_de_nuevo():
    # Función para jugar de nuevo
    print("¿Deseas jugar de nuevo?")
    print("1. Sí")
    print("2. No")
    decision = int(input("..."))
    if decision == 1:
        return True
    else:
        print("Gracias por jugar")
        return False

if __name__ == "__main__":
    explain_game()
    while play_game():
        pass
