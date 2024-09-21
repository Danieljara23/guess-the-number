print("Hola mundo")

import random

running = True

randomnumber = random.randint(1, 10)

user_attempts = 0

computer_attepmts = 0

while True:

    while running: 
        guess = int(input("Enter your number. "))
        if guess == randomnumber:
            user_attempts += 1
            print("The player wins.")
            print(f"It took the player {user_attempts} attempt(s) to get the right answer.")
            running = False
        elif guess <= randomnumber:
            user_attempts += 1
            print(f"{guess} is  low.")
        else:
            user_attempts += 1
            print(f"{guess} is  high.")

        if not running:
                break

        pc_guess = random.randint(1, 10)
        print(pc_guess)
        if pc_guess == randomnumber:
            computer_attepmts += 1
            print("The computer wins.")
            print(f"It took the computer {computer_attepmts} attempts to get the right answer.")
            running = False
        elif pc_guess <= randomnumber:
            computer_attepmts += 1
            print(f"{pc_guess} is low.")
        else: 
            computer_attepmts += 1
            print(f"{pc_guess} is high.")

    while running == False:
        play_again = input("Do you wish to play again? (y/n): ").lower()
        
        if play_again == 'y':
            running = True
            break
        elif play_again == 'n':
            print("Thank you for playing, see you around!")
            exit()  
        
        else:
            print("Alright, funny guy, I gave you 2 options. Stick to them. Y or N. Lowercase.")