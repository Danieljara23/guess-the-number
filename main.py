import random

def adivina_competencia():
    # La máquina genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    print("¡Bienvenido al juego Guess The Number!")
    print("He pensado un número entre 1 y 100. Tú y la máquina intentarán adivinarlo.")
    
    intentos_usuario = 0
    intentos_maquina = 0
    min_rango = 1
    max_rango = 100
    adivinado = False
    
    while not adivinado:
        # Turno del usuario
        intento_usuario = int(input("Tu turno, introduce tu intento: "))
        intentos_usuario += 1
        
        if intento_usuario < numero_secreto:
            print("El número es mayor.")
        elif intento_usuario > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos_usuario} intentos.")
            adivinado = True
            continue
        
        # Turno de la máquina
        intento_maquina = random.randint(min_rango, max_rango)
        intentos_maquina += 1
        print(f"La máquina intenta con el número: {intento_maquina}")
        
        if intento_maquina < numero_secreto:
            print("La máquina falló, su intento es menor.")
            min_rango = intento_maquina + 1
        elif intento_maquina > numero_secreto:
            print("La máquina falló, su intento es mayor.")
            max_rango = intento_maquina - 1
        else:
            print(f"¡La máquina ha adivinado el número en {intentos_maquina} intentos!")
            adivinado = True
    
    # Fin del juego
    if intentos_usuario < intentos_maquina:
        print(f"\n¡Ganaste! Lo lograste en {intentos_usuario} intentos contra {intentos_maquina} de la máquina.")
    elif intentos_usuario > intentos_maquina:
        print(f"¡La máquina ganó! \n Adivinó en {intentos_maquina} intentos, mientras que tú lo intentaste {intentos_usuario} veces.")
    else:
        print(f"\n¡Empate! Ambos adivinaron el número en {intentos_usuario} intentos.")

# Ejecutar el juego
adivina_competencia()