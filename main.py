import random 

random_number = random.randint(1, 50)

playing = True

while playing:
    guess = int(input("Ingresa el número"))
    if guess == random_number:
        print("Ganaste!")
        playing = False
    elif guess > random_number:
        print("El número debe ser menos")
    elif guess < random_number:
        print("El número debe ser mayor")
    
    if playing: 
        computer_guess = random.randint(1, 50)
        print(f"La computadora adivina: {computer_guess}")
        
        if computer_guess == random_number:
            print(f"La computadora ha ganado. El número era {random_number}.")
            playing = False
        elif computer_guess > random_number:
            print("El número debe ser menor que la suposición de la computadora.")
        elif computer_guess < random_number:
            print("El número debe ser mayor que la suposición de la computadora.")