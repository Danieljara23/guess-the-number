import random
from rich import print

# Inicializar variables
numero_secreto = random.randint(1, 100)
Lista_usuario = []
Lista_maquina = []
puntuacion_usuario = 0
puntuacion_maquina = 0

# Menú de entrada
while True:
    print("[bold cyan]---- Menú Principal ----[/bold cyan]")
    print("1. Iniciar juego")
    print("2. Ver puntuación")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Iniciar juego contra la máquina
        Play = True
        while Play:
            numero_secreto = random.randint(1, 100)
            Lista_usuario = []
            Lista_maquina = []
            while True:
                print("Adivina el número (entre 1 y 100): ")
                suposicion_usuario = int(input("Escribe un numero: "))
                Lista_usuario.append(suposicion_usuario)

                if suposicion_usuario == numero_secreto:
                    print("[bold green]¡Felicidades! Has adivinado el número secreto.[bold red]")
                    puntuacion_usuario += 1
                    break
                elif suposicion_usuario < numero_secreto:
                    print("[bold purple]El número secreto es mayor que tu suposición.[/bold purple]")
                else:
                    print("[bold purple]El número secreto es menor que tu suposición.[/bold purple]")

                # Turno de la máquina
                suposicion_maquina = random.randint(1, 100)
                Lista_maquina.append(suposicion_maquina)
                print(f"La máquina supone que el número secreto es {suposicion_maquina}.")

                if suposicion_maquina == numero_secreto:
                    print("La máquina ha adivinado el número secreto.")
                    puntuacion_maquina += 1
                    break

            # Preguntar al usuario si desea volver a jugar
            print("[bold green]¿Qué deseas hacer?[bold green]")
            print("1. Volver a jugar")
            print("2. Ir al menú principal")
            opcion_ninja = input("Seleccione una opción: ")

            if opcion_ninja == "1":
                # Volver a jugar
                continue
            elif opcion_ninja == "2":
                # Ir al menú principal
                play = False
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "2":
        # Ver puntuación
        print("Puntuación:")
        print(f"[bold dark_orange3]Usuario: {puntuacion_usuario} puntos [/bold dark_orange3]")
        print(f"[bold red3]Máquina: {puntuacion_maquina} puntos[/bold red3]")
        print("Intentos:")
        print(f"Usuario: {Lista_usuario}")
        print(f"Máquina: {Lista_maquina}")

    elif opcion == "3":
        # Salir
        print("Adiós!")
        break

    else:
        print("[bold red]Opción inválida. Intente nuevamente.[/bold red]")