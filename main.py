import random
import time
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

the_number= random.randint(1,100)

playing= True
user_turn= True
recommendation= 0
higher_limit = 100
lower_limit = 0

user_guess_list= []
AI_guess_list= []

while playing:
    while user_turn:
        AI_turn= False
        print("")
        user_guess= int(input("Intenta adivinar un número del 1 al 100: "))
        if user_guess != the_number:
            user_turn= False
            if user_guess < the_number:
                console.print ("[green]¡Súmale![/]", style= "bold")
                time.sleep(1)
                recommendation= 10
            if user_guess > the_number:
                console.print ("[green]¡Réstale![/]", style= "bold")
                time.sleep(1)
                recommendation= 5
            user_guess_list.append(user_guess)
            AI_turn= True
        elif user_guess == the_number:
            user_guess_list.append(user_guess)
            AI_guess_list.append("")
            print ("¡Adivinaste el número!")
            playing= False
            time.sleep(1)
            print("")
            console.print ("Presiona 1 para jugar de nuevo")
            console.print ("Presiona 2 para mostrar una lista de las suposiciones")
            print("")
            user_input= int(input("Escribe tu selección y presiona Enter " ))

            if user_input == 1:
                AI_guess_list.clear()
                user_guess_list.clear()
                the_number= random.randint(1,100)
                user_turn= True
                playing = True
            elif user_input == 2:
                print ("")
                table = Table(show_header=True, header_style="bold blue")
                table.add_column("[blue]Jugador[/]", justify="full")
                table.add_column("[blue]Computadora[/]")
                for i in range(len(user_guess_list)):
                    table.add_row(f"[green]{user_guess_list[i]}[/]",f"[green]{AI_guess_list[i]}[/]")
        
                console.print(table,justify="center")
                break 
    while AI_turn:
        if recommendation == 10:
            lower_limit= user_guess
            AI_guess= random.randint(lower_limit, higher_limit)
        elif recommendation == 5:
            higher_limit= user_guess
            AI_guess= random.randint(lower_limit, higher_limit)
        print ("La computadora está pensando...")
        time.sleep(1)
        print (AI_guess)
        time.sleep(1)
        if AI_guess != the_number:
            AI_turn= False
            if AI_guess < the_number:
                console.print ("[green]¡Súmale![/]", style= "bold")
                lower_limit = AI_guess
                time.sleep(1)
            if AI_guess > the_number:
                console.print ("[green]¡Réstale![/]", style= "bold")
                higher_limit= AI_guess
                time.sleep(1)
            AI_guess_list.append(AI_guess)
            user_turn= True
        elif AI_guess == the_number:
            AI_guess_list.append(AI_guess)
            user_guess_list.append("")
            print("¡La computadora adivinó el número!")
            playing= False
            time.sleep(1)
            print("")
            console.print ("Presiona 1 para jugar de nuevo")
            console.print ("Presiona 2 para mostrar una lista de las suposiciones")
            print("")
            user_input= int(input("Escribe tu selección y presiona Enter " ))

            if user_input == 1:
                AI_guess_list.clear()
                user_guess_list.clear()
                user_turn= True
                playing = True
            elif user_input == 2:
                print ("")
                table = Table(show_header=True, header_style="bold blue")
                table.add_column("[blue]Jugador[/]", justify="full")
                table.add_column("[blue]Computadora[/]")
                for i in range(len(user_guess_list)):
                    table.add_row(f"[green]{user_guess_list[i]}[/]",f"[green]{AI_guess_list[i]}[/]")
        
                console.print(table,justify="center")
                break
