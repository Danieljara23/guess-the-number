import random # Usado para elegir el número aleatorio
import time

def jugar_guess():
    # Genera un número aleatorio al inicio de la ronda
    random_num = random.randint(1, 100)
    jugando = True

    # Listas para almacenar los intentos
    int_jugador = []
    int_pc = []

    # Límites para la adivinanza de la computadora
    min_pc = 1
    max_pc = 100

    while jugando:
        # Turno del jugador
        print("Tu turno")
        user_num = int(input("Intenta adivinar el número: "))
        int_jugador.append(user_num)
        time.sleep(0.2) # Usado para poner tiempos entre líneas de texto y facilitar la lectura, se mide en segundos
        if user_num < random_num:
            print(f"{user_num} es menor que el número aleatorio, intenta de nuevo")
            print("-------------------------------------------------------------")
            min_pc = user_num + 1
            time.sleep(0.25)
        elif user_num > random_num:
            print(f"{user_num} es mayor que el número aleatorio, intenta de nuevo")
            print("-------------------------------------------------------------")
            max_pc = user_num - 1
            time.sleep(0.25)
        elif user_num == random_num:
            print("-------------------------------------------------------------")
            print(f"\n¡Felicidades! {user_num} es el número correcto\n")
            time.sleep(0.2)
            print(f"Tus intentos fueron: {int_jugador}")
            print(f"Los intentos del adversario fueron: {int_pc}\n")
            time.sleep(0.2)
            jugando = False
            jugar_de_nuevo()
            break

        time.sleep(0.5)

# Turno del ordenador
        pc_num = random.randint(min_pc, max_pc)
        int_pc.append(pc_num)
        print("Turno del adversario")
        print(f"El número del adversario es {pc_num}")
        time.sleep(0.2)
        if pc_num < random_num:
            print(f"{pc_num} es menor que el número aleatorio")
            print("-------------------------------------------------------------")
            # Aqui se hace un ajuste al límite del compu para que no elija números más bajos 
            min_pc = pc_num + 1
            time.sleep(0.35)
        elif pc_num > random_num:
            print(f"{pc_num} es mayor que el número aleatorio")
            print("-------------------------------------------------------------")
            # Y aquí para que no elija números más altos
            max_pc = pc_num - 1
            time.sleep(0.35)
        elif pc_num == random_num:
            print("-------------------------------------------------------------")
            print("¡Derrota! El adversario adivinó el número")
            time.sleep(0.15)
            print(f"El número correcto era {random_num}\n")
            time.sleep(0.2)
            print(f"Tus intentos fueron: {int_jugador}")
            print(f"Los intentos del adversario fueron: {int_pc}\n")
            time.sleep(0.2)
            jugando = False
            jugar_de_nuevo()
            break


# Función para jugar otra vez
def jugar_de_nuevo():
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        print("-------------------------------------------------------------")
        
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
