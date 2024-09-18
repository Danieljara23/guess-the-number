import random

def adivina_competencia():
    # La máquina genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    print("¡Bienvenido al juego Guess The Number!")
    print("He pensado un número entre 1 y 100. Tú y la máquina intentarán adivinarlo.")
    print("----------------------------------------------")
    
    intentos_maquina = 0
    intentos_usuario = 0
    min_rango = 1
    max_rango = 100
    adivinado = False
    
    while not adivinado:
        # Turno del usuario
        intento_usuario = int(input("Tu turno, introduce tu intento: "))
        intento_usuario += 1
        
        if intento_usuario < numero_secreto:
            print("El número que intentas adivinar es mayor.")
            print("-------------------------")

        elif intento_usuario > numero_secreto:
            print("El número que intentas adivinar es menor.")
            print("-------------------------")
            
        else:
            print(f"¡Felicidades! Adivinaste el número.")
            adivinado = True
            continue
        
        # Turno de la máquina
        intento_maquina = random.randint(min_rango, max_rango)
        intento_maquina += 1
        print("-------------------------")
        print(f"La máquina intenta con el número: {intento_maquina}")
        
        if intento_maquina < numero_secreto:
            print("La máquina falló, su número es menor.")
            min_rango = intento_maquina + 1
            print("-------------------------")
        elif intento_maquina > numero_secreto:
            print("La máquina falló, su número es mayor.")
            max_rango = intento_maquina - 1
            print("-------------------------")
        else:
            print(f"¡La máquina ha adivinado el número primero que tu!")
            adivinado = True
            break

# Ejecutar el juego
adivina_competencia()