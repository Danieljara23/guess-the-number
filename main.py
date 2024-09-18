import random
from rich.console import Console
from rich.text import Text

# Inicializamos la consola de Rich para poder usar colores
console = Console()

# Genera un número aleatorio entre 1 y 100
random_number = random.randint(1, 100)

def jugar():
    playing = True
    turno_jugador = True  # Variable para alternar entre jugador y ordenador
    sucesos_jugador = []
    sucesos_ordenador = []

    console.print("¡Bienvenido al juego de adivinanza!", style="bold yellow")
    print("")
    console.print("Tendrás que adivinar un número entre 1 y 100, turnándote con el ordenador.", style="italic cyan")
    console.print("====================================================================")

    while playing:
        if turno_jugador:
            # Turno del jugador
            guess = int(input("\n[Jugador] Ingresa un número (entre 1 - 100): "))
            sucesos_jugador.append(guess)  # Guarda la suposición del jugador

            if guess == random_number:
                console.print("\n[bold green]¡Ganaste![/] Adivinaste el número. 🙌🙌🙌🙌")
                playing = False
            elif guess > random_number:
                console.print("\n[red]El número es menor. ¡Intenta de nuevo!🤵[/]")
            else:
                console.print("\n[red]El número es mayor. ¡Intenta de nuevo!🤵[/]")

        else:
            # Turno del ordenador
            guess_ordenador = random.randint(1, 100)
            sucesos_ordenador.append(guess_ordenador)  # Guarda la suposición del ordenador
            console.print(f"\n[Ordenador] El ordenador adivina: {guess_ordenador}", style="bold cyan")

            if guess_ordenador == random_number:
                console.print("\n[bold red]El ordenador ha adivinado el número. ¡El ordenador gana! 😭😭😭[/]")
                playing = False
            elif guess_ordenador > random_number:
                console.print("\n[blue]El número es menor (según el ordenador🤖).[/]")
            else:
                console.print("\n[blue]El número es mayor (según el ordenador🤖).[/]")

        # Alterna el turno entre jugador y ordenador
        turno_jugador = not turno_jugador

        console.print("====================================================================")

    # Al finalizar, muestra las suposiciones de ambos
    console.print(f"\n[green]Las suposiciones del jugador fueron:[/] {sucesos_jugador}")
    console.print("====================================================================")
    console.print(f"\n[cyan]Las suposiciones del ordenador fueron:[/] {sucesos_ordenador}")

# Función para preguntar si desea volver a jugar
def volver_a_jugar():
    while True:
        jugar()
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != "s":
            console.print("\n[bold magenta]Gracias por jugar. ¡Hasta luego![/]")
            break

volver_a_jugar()
