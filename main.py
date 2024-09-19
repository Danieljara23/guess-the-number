import random
import time
from rich.console import Console

# Crear instancia de consola
console = Console()

# Función del juego
def jugar_adivina_el_numero():
    # La bienvenida
    console.print("¡Bienvenido a Adivina el Número!", style="bold underline cyan on black")
    console.print("Instrucciones:", style="bold underline magenta")
    console.print("1. El juego consiste en adivinar un número secreto entre 1 y 100.", style="bold yellow")
    console.print("2. Puedes elegir jugar contra la computadora o contra un amigo.", style="bold yellow")
    console.print("3. Después de 15 intentos, recibirás pistas avanzadas (si el número es par o impar).", style="bold yellow")
    console.print("4. Si deseas rendirte en cualquier momento, presiona 'r'.", style="bold yellow")
    console.print("¡Buena suerte!\n", style="bold green on black")
    
    # Elegir el modo de juego
    console.print("Elige el modo de juego: '1' para jugar contra la computadora, '2' para jugar con un amigo:", style="bold white on blue")
    modo = input()  # Usamos input() normal sin estilo
    
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
            console.print(f"Jugador {jugador}, adivina el número (entre 1 y 100 o presiona 'r' para rendirte):", style="bold blue on black")
            suposicion = input().lower()  # Usamos input() sin estilo
            if suposicion == 'r':
                console.print(f"Jugador {jugador} se ha rendido. ¡Fin del juego!", style="bold white on red")
                exit()  # Termina el programa
            try:
                suposicion = int(suposicion)
                if 1 <= suposicion <= 100:
                    no_valido = False
                else:
                    console.print("Por favor ingresa un número entre 1 y 100.", style="bold red on black")
            except ValueError:
                console.print("Entrada inválida. Debes ingresar un número.", style="bold red on black")
        return suposicion

    # Ciclo del juego
    while True:
        intentos += 1
        
        if modo == '1':
            if jugador_actual == 1:
                # Computadora adivina
                suposicion = random.randint(1, 100)
                console.print(f"Jugador 1 (Computadora) adivina: {suposicion}", style="bold white on green")
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
                console.print(f"¡Jugador 1 gana en {intentos} intentos!", style="bold underline white on gold")
                if modo == '1':
                    console.print("La computadora te ganó, ¡qué mal!", style="bold underline white on red")
                    console.print("Computadora: \"¡No eres rival para mí!\"", style="bold underline red on black")
                else:
                    console.print("¡Jugador 1 se burla de ti!", style="bold underline black on white")
            else:
                console.print(f"¡Jugador 2 gana en {intentos} intentos!", style="bold underline white on blue")
                console.print("Jugador 2: \"¡Te he vencido!\"", style="bold underline red on black")
            
            console.print(f"El juego duró {round(tiempo_total, 2)} segundos.", style="bold black on cyan")
            console.print(f"Suposiciones del Jugador 1: {suposiciones_jugador1}", style="bold yellow on black")
            console.print(f"Suposiciones del Jugador 2: {suposiciones_jugador2}", style="bold yellow on black")
            
            # Preguntar si quiere jugar otra vez
            console.print("¿Quieres jugar otra vez? (s/n):", style="bold white on magenta")
            jugar_otra_vez = input().lower()  # Usamos input() sin estilo
            if jugar_otra_vez == 's':
                jugar_adivina_el_numero()
            else:
                console.print("¡Gracias por jugar!", style="bold green on black")
                break

        # Dar pistas
        else:
            if suposicion < numero_secreto:
                console.print(f"Jugador {jugador_actual}, el número secreto es mayor que {suposicion}.", style="bold blue on black")
            else:
                console.print(f"Jugador {jugador_actual}, el número secreto es menor que {suposicion}.", style="bold red on black")

            # Pistas después de 15 intentos
            if intentos > 15:
                if numero_secreto % 2 == 0:
                    console.print(f"Pista: El número secreto es par.", style="bold underline black on white")
                else:
                    console.print(f"Pista: El número secreto es impar.", style="bold underline black on white")
                    
        # Cambiar de jugador
        jugador_actual = 2 if jugador_actual == 1 else 1

# Iniciar el juego
jugar_adivina_el_numero()
