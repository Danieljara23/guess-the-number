import random

def jugar_guess():
    # Genera un número aleatorio al inicio de la ronda
    random_num = random.randint(1, 100)
    jugando = True

    # Listas para almacenar los intentos
    int_jugador = []
    int_pc = []

    while jugando:
        # Turno del jugador
        print("\nTu turno")
        user_num = int(input("Intenta adivinar el número: "))
        int_jugador.append(user_num)
        if user_num < random_num:
            print(f"{user_num} es menor que el número aleatorio, intenta de nuevo\n")
        elif user_num > random_num:
            print(f"{user_num} es mayor que el número aleatorio, intenta de nuevo\n")
        elif user_num == random_num:
            print(f"¡Felicidades! {user_num} es el número correcto\n")
            print(f"Tus intentos fueron: {int_jugador}")
            print(f"Los intentos del adversario fueron: {int_pc}")
            jugando = False
            jugar_de_nuevo()

        # Turno del ordenador
        pc_num = random.randint(1, 100)
        int_pc.append(pc_num)
        print("Turno del adversario")
        print(f"El número del adversario es {pc_num}")
        if pc_num < random_num:
            print(f"{pc_num} es menor que el número aleatorio\n")
        elif pc_num > random_num:
            print(f"{pc_num} es mayor que el número aleatorio\n")
        elif pc_num == random_num:
            print("¡Derrota! El adversario adivinó el número")
            print(f"El número correcto era {random_num}\n")
            print(f"Tus intentos fueron: {int_jugador}")
            print(f"Los intentos del adversario fueron: {int_pc}")
            jugando = False
            jugar_de_nuevo()

# Función para jugar otra vez
def jugar_de_nuevo():
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        
        if respuesta == 'si':
            jugar_guess()
        elif respuesta == 'no':
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Respuesta inválida. Por favor, responde con 'sí' o 'no'. Inténtalo de nuevo.") 
            #  La función se repite hasta que se elige la opcion correcta

# Se inicia la partida
jugar_guess()
