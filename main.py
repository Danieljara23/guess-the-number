import random
import time
from rich import print
from rich.console import Console
from rich.text import Text

console = Console()

def jugar():
    random_number = random.randint(1, 101)
    playing = True

    console.print("[bold blue]¡Hola! Bienvenido a [bold yellow]Guess the number[/bold yellow].[/bold blue]")
    console.print("""
[green]El juego consiste en adivinar el número aleatorio que la computadora generará entre 1 y 100 antes que ella.
Jugarán turno por turno y quien adivine antes, ganará.[/green]
[purple]Aprovecha las pistas que te dará el juego y también ten en cuenta el número que la computadora escoge, así podrás adivinar el número secreto antes que ella.[/purple]
[cyan]¡Buena suerte![/cyan]
""")

    while playing:
        # Adivinanza del jugador
        guess = int(input("Adivina el número secreto entre 1 y 100. Por favor ingresa un número: "))
        
        if guess == random_number:
            console.print("[bold green]¡Ganaste![/bold green] :tada:")
            break
        elif guess > random_number:
            console.print("[yellow]El número secreto es más pequeño[/yellow] :arrow_down_small:\n")
        elif guess < random_number:
            console.print("[yellow]El número secreto es más grande[/yellow] :arrow_up_small:\n")
        
        # Pausa para dar tiempo entre turnos
        time.sleep(2)
        
        # Adivinanza de la computadora
        computadora = random.randint(1, 101)
        console.print(f"[blue]La computadora escogió el número... [bold red]{computadora}[/bold red][/blue]")

        if computadora == random_number:
            console.print("[bold red]La computadora ganó[/bold red] :robot:")
            break
        elif computadora > random_number:
            console.print("[yellow]El número secreto es más pequeño que el de la computadora[/yellow]\n")
        elif computadora < random_number:
            console.print("[yellow]El número secreto es más grande que el de la computadora[/yellow]\n")

# Bucle para repetir el juego
while True:
    jugar()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")

    if jugar_de_nuevo.lower() != 's':
        console.print("[bold green]¡Gracias por jugar![/bold green] :smiley:")
        break
