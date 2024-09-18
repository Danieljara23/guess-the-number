import random
import time

# Función del juego
def jugar_adivina_el_numero():
    # La bienvenida
    print("¡Bienvenido a Adivina el Número!")
    print("Instrucciones:")
    print("1. El juego consiste en adivinar un número secreto entre 1 y 100.")
    print("2. Puedes elegir jugar contra la computadora o contra un amigo.")
    print("3. Después de 15 intentos, recibirás pistas avanzadas (si el número es par o impar).")
    print("4. Si deseas rendirte en cualquier momento, presiona 'r'.")
    print("¡Buena suerte!\n")
    
    # Elegir el modo de juego
    modo = input("Elige el modo de juego: '1' para jugar contra la computadora, '2' para jugar con un amigo: ")
    
    # Generar número secreto
    numero_secreto = random.randint(1, 100)
    intentos = 0
    suposiciones_jugador1 = []
    suposiciones_jugador2 = []
    jugador_actual = 1
    
    inicio_tiempo = time.time()  # Iniciar el tiempo
    
    # Función para realizar una jugada
    def turno_jugador(jugador):
        no_valido = True
        while no_valido:
            suposicion = input(f"Jugador {jugador}, adivina el número (entre 1 y 100 o presiona 'r' para rendirte): ").lower()
            if suposicion == 'r':
                print(f"Jugador {jugador} se ha rendido. ¡Fin del juego!")
                exit()  # Termina el programa
            try:
                suposicion = int(suposicion)
                if 1 <= suposicion <= 100:
                    no_valido = False
                else:
                    print("Por favor ingresa un número entre 1 y 100.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")
        return suposicion

    # Ciclo del juego
    while True:
        intentos += 1
        
        if modo == '1':
            if jugador_actual == 1:
                # Computadora adivina
                suposicion = random.randint(1, 100)
                print(f"Jugador 1 (Computadora) adivina: {suposicion}")
                suposiciones_jugador1.append(suposicion)
            else:
                # Persona adivina
                suposicion = turno_jugador(2)
                suposiciones_jugador2.append(suposicion)
        else:
            if jugador_actual == 1:
                suposicion = turno_jugador(1)
                suposiciones_jugador1.append(suposicion)
            else:
                suposicion = turno_jugador(2)
                suposiciones_jugador2.append(suposicion)

        # Comparar la suposición con el número secreto
        if suposicion == numero_secreto:
            final_tiempo = time.time()  # Fin del temporizador
            tiempo_total = final_tiempo - inicio_tiempo
            
            if jugador_actual == 1:
                print(f"¡Jugador 1 gana en {intentos} intentos!")
                if modo == '1':
                    print("La computadora te ganó, ¡qué mal!")
                    print("Computadora: \"¡No eres rival para mí!\"")
                else:
                    print("¡Jugador 1 se burla de ti!")
            else:
                print(f"¡Jugador 2 gana en {intentos} intentos!")
                print("Jugador 2: \"¡Te he vencido!\"")
            
            print(f"El juego duró {round(tiempo_total, 2)} segundos.")
            print(f"Suposiciones del Jugador 1: {suposiciones_jugador1}")
            print(f"Suposiciones del Jugador 2: {suposiciones_jugador2}")
            
            # Preguntar si quiere jugar otra vez
            jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
            if jugar_otra_vez == 's':
                jugar_adivina_el_numero()
            else:
                print("¡Gracias por jugar!")
                break

        # Dar pistas
        else:
            if suposicion < numero_secreto:
                print(f"Jugador {jugador_actual}, el número secreto es mayor que {suposicion}.")
            else:
                print(f"Jugador {jugador_actual}, el número secreto es menor que {suposicion}.")

            # Pistas después de 15 intentos
            if intentos > 15:
                if numero_secreto % 2 == 0:
                    print(f"Pista: El número secreto es par.")
                else:
                    print(f"Pista: El número secreto es impar.")
                    
        # Cambiar de jugador
        jugador_actual = 2 if jugador_actual == 1 else 1

# Iniciar el juego
jugar_adivina_el_numero()
