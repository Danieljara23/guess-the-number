#juego Samuel Aguirre-Jeronimo Tobon

import random
import time



while True:
    print("Elige un modo de juego para adivinar un número del 1 al 100: ")
    print("Presiona 1 para jugar contra la máquina")
    print("Presiona 2 para jugar solo")
    print("Presiona 3 para jugar con otra persona")
    print("Preciona 0 para salir del juego")
    
    intentos = 1

    user_input = int(input())  
    
    tiempo_inicio =  time.time()


    jugando = True
#modo de juego 1 jugador vs maquina

    if user_input == 1:

        min_range = 1
        max_range = 100

        random_number = random.randint(1,100+1) 

        while jugando:
            
            number_user= int(input("trata de adivinar el numero: "))
            intentos += 1

            maquina_num= random.randint(min_range,max_range)

            print(f"el numero de la maquina es: {maquina_num}")

#programacion de las condiciones de victoria y pistas del jugador (modo1)
            if number_user == random_number:
                    print(f"¡Has ganado, enhorabuena!, el numero era {random_number}.")
                    print('')

                    tiempo_final =  time.time()

                    tiempo_total = tiempo_final - tiempo_inicio

                    print(f"El tiempo total que tomaste fue {tiempo_total} segundos.")

                    print(f"El número de intentos que tomaste fue {intentos}.")

                    print('')
                    break

            elif number_user>random_number:
                    print("el numero del usuario es mayor al que tiene que adivinar")
        
            elif number_user<random_number:
                    print("el numero del usuario es menor al que tiene que adivinar")

            else :
                    print("Ha ocurrido un error")

#programacion de las condiciones de victoria y pistas para la maquina(modo1)

            if maquina_num==random_number:
                    print("has perdido,la maquina ha adivinado el numero")
                    print('')
                    jugando=False

            elif maquina_num<random_number:
                    print("el numero de la maquina es menor al que tiene que adivinar")
                    min_range=maquina_num

            elif maquina_num>random_number:
                    print("el numero de la maquina es mayor al que tiene que adivinar")
                    max_range=maquina_num

 #modo de juego 2 jugando solo
            
            elif user_input==2:

                    random_number= random.randint(1,100+1)

                    number_user= int(input("trata de adivinar el numero: "))


    elif user_input == 2:
        random_number = random.randint(1, 100) 

        while jugando:
            
            number_user = int(input("Trata de adivinar el número: "))
            intentos += 1
            #programcion de condiciones de victoria y pistas para el jugador (modo2)
            if number_user == random_number:
                print("¡Has ganado, enhorabuena!")
                print('')

                tiempo_final =  time.time()
                tiempo_total = tiempo_final - tiempo_inicio
                
                print(f"El tiempo total que tomaste fue {tiempo_total} segundos.")
                print(f"El número de intentos que tomaste fue {intentos}.")
                print('')
                jugando = False

            elif number_user > random_number:
                print("El numero del usuario es mayor al que tiene que adivinar")

            elif number_user < random_number:
                print("El numero del usuario es menor al que tiene que adivinar")

#modo 3 pvp
    elif user_input == 3:
        random_number = random.randint(1, 100) 

        while jugando:
            
            number_user1 = int(input("Jugador1: Trata de adivinar el número: "))

            number_user2 = int(input("Jugador2: Trata de adivinar el número: "))
            intentos += 1

            #programacion jugador 1

            if number_user1 == random_number:
                print("Jugador1: ¡Has ganado, enhorabuena!")
                print('')

                tiempo_final =  time.time()
                tiempo_total = tiempo_final - tiempo_inicio

                print(f"El tiempo total que tomaste fue {tiempo_total} segundos.")

                print(f"El número de intentos que tomaste fue {intentos}.")
                print('')
                jugando = False

            elif number_user1 > random_number:
                print("Jugador1: El numero del usuario es mayor al que tiene que adivinar")

            elif number_user1 < random_number:
                print("Jugador1: El numero del usuario es menor al que tiene que adivinar")

            #programacion jugador 2    
            
            if number_user2 == random_number:
                print("Jugador2:¡Has ganado, enhorabuena!")
                print('')

                tiempo_final =  time.time()
                tiempo_total = tiempo_final - tiempo_inicio

                print(f"El tiempo total que tomaste fue {tiempo_total} segundos.")

                print(f"El número de intentos que tomaste fue {intentos}.")
                print('')
                jugando = False
            elif number_user2 > random_number:
                print("Jugador2: El numero del usuario es mayor al que tiene que adivinar")

            elif number_user2 < random_number:
                print("Jugador2: El numero del usuario es menor al que tiene que adivinar")

        #🤫 programcion del secreto
    elif user_input == 4:

        print("Felicidades has encontrado un secreto no muy secreto,")
        print("Espero que tengas un exelente dia y gracias por probar nuestro juego")

        print("""
    .../((###############%%%%%%%###%%%%%%%%%%%%%%%%##((((/(###(#(#((((//**,,        
    ,,#####%%%%%%%%%%%%%%#####%%%&&&@&&&&&&&&&&@&&%%###////############(((//**,.    
    *%%%%%%%%%%%%%%%%######%#%%%%&&&&&&@&@@@@@@@@@@@&&%#((#%%%%%%#%%%#####(((//*,,. 
    %###%%&&%%%#%%%##(((((((((#((##%#%%&&&&@&@@@@@@@@@&&%%#(###((####%%%##//#(((//*,
    (/((#####%%%%%%%(**////////////(((##%%%&&&@@@@@&@@&&&%##%######(%%%%%##((((((((/
    (/###%#%###((((((//***********//((###%%%&&&&@@@&&@&&&%##%%%%#%#%%%%%%%####(((##(
    (####(//*,.....,,,***********//((##%%%%%&&&&&&&@@@@&&&&&&%%&&%&&%%%%%%%%####((##
    ###(*,.... ..      ..,***////(((###%%%&&&&&&&&&&&&&&&%#(*****/(#%%%%%%%%######%#
    ##(*.,........,.     .,///////(((####%%%%%%%&%%%%&&&&&#*,,,,****(#%%%%%########%
    #(*,,.      .  .,..  ,*/////////(((((####%%%%%%%%%%%%%&&%((@,,*(#%%%%%%*,..../(%
    #(*/*             .,**//////***///(((((###############%%%&#*,,,(#%%##%#*.,...*/%
    /*..*.         ,**////////*****///((((########((#########%%%/,,/#/%&#((((/*,,,/% 
    **********///////////////*****///((((#########(###########%%%(/(*/%&&&#(((*,,,*%
    ,**//////////////////////*****////((((#####################%&&&&@@@&&%#((((*,*/%
    **///////////////////((((**,*********/((####################&&&&@@@@@@@&#(#(,,(%
    /////////////////////((((((/*,,,,,.. .,/((####((#####///((#%&&&&&@@@@@@@&%%#//(#
    //////////////////////((((#####(//*,.. .*((((((((##(***/(#%&&&&&&&@@@@@@&&%#(/**
    ///////*****/**/////////((((#######(*,,,*/(((((((##(((##%%&&&&&&&&&@@@@@&&%%#(//
    //*///*/**************/////((((######(**//(((((((#####%%%&&&&&&&&&&@@@&&&&&%%#(((
    ***********************////////(((####(///(((((((####%%&&&&&&&&&&@@@&&&&&%%#////
    ***************************//////((((((((((((((((###%%&&&&&&&&&&&@@@@@&&&%%###((
    ***************************/////////((###((((((####%%&&&&&&&&&&&&&&&&&&&&%%##%%%
    ********************************/////(((#####((###%%%&&&&&&&&&&&&@@@@@&&&%%###((
    /*******************************///////(((##(((###%%%%%&&&&&&&&@@@@@&&&&%(((((((
    ************************************////(((((((#####%%%%%&&&&&&&&&&&&&&#(//(###(
    /************************************/////(///((####%%%%%%%&&&&&&&&%#(//##//****
    **************************,**********///////////((((###%%%%%%%%%%%##((((/****((
    ***********************,,,,,,,,,,,,******/////////((((((#%%%%%#####((#/((((**,,*
    *********************,,,,..,,...,,,,,,******/////////((((#%%###(((((/(((((/((***
    /*********/////******,,,,..,......,,,,,*******///////((((#%###((#((((////(///(((
    *******///////////***,,,,,,,,......,,,,**(/***/////((((((%%##(((((((((//(((#(##%
    ,,***/////////(//////***,*,*,,,.....,,,******//////((((#%%##(((((((((((((((((#%%
    ,,,,,**////((((((#((((///*/*//*/*,.,,,,,*****////////#%%#####((((#(#######(//(##
    ,.,,...,***/////(########%%%#########%%%%%%%%%%####((##%%%%%%%%%%%%&&&&&&&%%%%%%
    ,,,....,,,,,,*****/(%%&&&&&%%%###(//#((####(((((((/**(((#%%%&&&%%%&&&&&&&&&&&&&&
    ,.....,....,,,****,,/#%&&&&@@&&#****//((//##%%%&&#,,,,*(#%%%%%%%%%%%%#(#&&&&&&%#
    ,............,,,**,,,,/#%&&&@@&%(,*///*//(#&&&&&(,...,/%&%((((###(((//%(#%(#/(,*
    ,.............,,,,*,***/#%&&&@@&#,*/////((((((//**,,./&&&&%#/,*(///(%&&%##*//...
    """)
        print("si algo esto es un gato sacando la lengua...")
        print('')

    #terminacion de bucle de juego
    elif user_input == 0:

        print("¡Gracias por jugar! Hasta luego.")
        jugando = False

        break
    #mesaje en caso de comando incorrecto   
    else:
        print("comando incorrecto")
        print("intenta de nuevo")

        break   