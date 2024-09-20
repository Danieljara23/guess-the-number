print("Hola mundo")

import random
running = True
randomnumber = random.randint(1, 10)
user_attempts = 0
computer_attepmts = 0
while running: 
    guess = int(input("Enter your number. "))
    if guess == randomnumber:
        user_attempts += 1
        print("The player wins.")
        print("It took the player", user_attempts, "attempt(s) to get the right answer.")
        running = False
    elif guess <= randomnumber:
        user_attempts += 1
        print(guess, "is low.")
    else:
         user_attempts += 1
         print(guess, "is high.")
    pc_guess = random.randint(1, 10)
    print(pc_guess)
    if pc_guess == randomnumber:
        computer_attepmts += 1
        print("The computer wins.")
        print("It took the computer", computer_attepmts, "attempt(s) to get the right answer.")
        running = False
    elif pc_guess <= randomnumber:
        computer_attepmts += 1
        print(pc_guess, "is low.")
    else: 
        computer_attepmts += 1
        print(pc_guess, "is high.")