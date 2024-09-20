import random

def jugar():
    while True:
        random_number = random.randint(1, 100)  
        print("He generado un número entre 1 y 100. ¡Intenten adivinarlo!")

        
        suposiciones_jugador = []
        suposiciones_computador = []

        jugando = True
        while jugando:
        
            player = int(input("Ingresa un número: "))
            suposiciones_jugador.append(player)  

            if player == random_number:
                print("¡Ganaste! El número era:", random_number)
                jugando = False
            elif player < random_number:
                print("Tu número es menor.")
            else:
                print("Tu número es mayor.")

            
            if jugando:  
                player_computador = random.randint(1, 100)
                suposiciones_computador.append(player_computador)  
                print(f"El computador adivina el numero: {player_computador}")

                if player_computador == random_number:
                    print(f"El computador ganó. El número era: {random_number}")
                    jugando = False
                elif player_computador < random_number:
                    print("La suposición del computador es menor.")
                else:
                    print("La suposición del computador es mayor.")

        
        print("\nSuposiciones del jugador:", suposiciones_jugador)
        print("Suposiciones del computador:", suposiciones_computador)

    
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    jugar()