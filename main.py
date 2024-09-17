import random

mysterious_number = random.randint(1, 100)

#esto genera el numero aleatorio que el juagdor tiene que descubrir]

#Aqui hace falta unos print que expliquen el juego

game = True

while game == True:
    
    user_number = int(input("Tu numero:   "))
    machine_number = random.randint(1, 100)
    
    print(f"Número de la IA:   {machine_number}")
    print("")
    
    if user_number == mysterious_number:
        print("Lo lograste!!")
        print("Felicidades")
        game = False
        break
    
    if user_number > mysterious_number:
        print("Pista: Te pasaste")
        
    if user_number < mysterious_number:
        print("Pista: Aún no llegas")
        
    if machine_number == mysterious_number:
        print("FALLASTEEEEE")
        print("La IA encontró el número primero que tu")
        print("Suerte la próxima")
        game = False
        break