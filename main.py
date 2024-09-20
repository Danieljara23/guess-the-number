import random
import time
def jugar():
    random_number = random.randint(1, 101)
    playing = True
    print("¡Hola! Bienvenido a Guess the number.\nEl juego consiste adivinar el número aleatorio que la computadora generará entre 1 y 100 antes que ella.\nJugarán turno por turno y quien adivine antes, ganará. Aprovecha las pistas que te dará el juego y también ten en cuenta el número que la computadora escoge, así podrás adivinar el número secreto antes que ella ¡Buena suerte!")
    pass
    while playing:
            guess = int(input("Adivina el número secreto entre 1 y 100. Por favor ingresa un número..."))
            if guess == random_number:
                print("Ganaste!")
                break
            elif guess > random_number:
                print("El número secreto es más pequeño \n")
            elif guess < random_number:
                print("El número secreto es más grande \n")
            time.sleep(3)
            
            computadora= random.randint(1,101)
            print("la computadora escogió el número...", computadora)
            if computadora == random_number:
                print("La computadora ganó ")            
                break
            elif computadora > random_number:
                print("El número secreto es más pequeño que el de la computadora\n")
            elif computadora < random_number:
                print("El número secreto es más grande que el de la computadora\n")

while True:
    jugar()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    
    if jugar_de_nuevo.lower() != 's':
        print("¡Gracias por jugar!")
        break