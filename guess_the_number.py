import random

def jugar():
    print("¡Bienvenido al juego de adivinanza! Trata de adivinar el número antes que la máquina.")
    
    while True:
        random_number = random.randint(1, 100)  
        print("\nHe generado un número entre 1 y 100. ¡Intenten adivinarlo!")

        
        suposiciones_jugador = []
        suposiciones_computador = []

        
        rango_min = 1
        rango_max = 100

        jugando = True
        while jugando:
            
            try:
                player = int(input("\nIngresa un número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            suposiciones_jugador.append(player)  

            if player == random_number:
                print("¡Ganaste! El número era:", random_number)
                jugando = False
            elif player < random_number:
                print("Tu número es menor.")
            else:
                print("Tu número es mayor.")

            
            if jugando:  
                player_computador = random.randint(rango_min, rango_max)
                suposiciones_computador.append(player_computador)  
                print(f"El computador adivina: {player_computador}")

                if player_computador == random_number:
                    print(f"El computador ganó. El número era: {random_number}")
                    jugando = False
                elif player_computador < random_number:
                    print("La suposición del computador es menor.")
                    rango_min = player_computador + 1  
                else:
                    print("La suposición del computador es mayor.")
                    rango_max = player_computador - 1  

        
        print("\nSuposiciones del jugador:", suposiciones_jugador)
        print("Suposiciones del computador:", suposiciones_computador)

        
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    jugar()