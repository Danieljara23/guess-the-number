import random
import time

random_number = random.randint(1, 100)
playing = True
print(input("¡Hola! Bienvenido a Guess the number.\nEl juego consiste adivinar el número aleatorio que la computadora generará entre 1 y 100 antes que ella.\nJugarán turno por turno y quien adivine antes, ganará. Aprovecha las pistas que te dará el juego y también ten en cuenta el número que la computadora escoge, así podrás adivinar el número secreto antes que ella ¡Buena suerte!"))

while playing:
    guess = int(input("Adivina el número secreto entre 1 y 100. Por favor ingresa un número..."))
    if guess == random_number:
        print("Ganaste!")
        playing = False
    elif guess > random_number:
        print("El número secreto es más pequeño \n")
    elif guess < random_number:
        print("El número secreto es más grande \n")
    time.sleep(3)
    
    computadora= random.randint(1,100)
    print("la computadora escogió el número...", computadora)
    if computadora == random_number:
        print("La computadora ganó ")
        
        playing = False
    elif computadora > random_number:
        print("El número secreto es más pequeño que el de la computadora\n")
    elif computadora < random_number:
        print("El número secreto es más grande que el de la computadora\n")