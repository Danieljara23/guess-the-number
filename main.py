print("Hola mundo")
import random

numero_random = numero_ordenador = random.randint(1, 100)

lista_jugador = []
lista_ordenador = []

def Jugador():
    numero_jugador = int(input("Por favor ingresa un número: "))
    lista_jugador.append(numero_jugador)
    return Validar(numero_jugador)

def Ordenador():
    numero_ordenador = random.randint(1, 100)
    lista_ordenador.append(numero_ordenador)
    print("Turno del ordenador: " + numero_ordenador.__str__()) 
    return Validar(numero_ordenador)

def Validar(num:int):
    if num == numero_random:
        return True
    elif num> numero_random:
        print("Te pasaste, el número es más pequeño.")

    else: 
        print("Te falta, el número que ingresaste es muy pequeño.") 
    return False

def MostrarListas():
    print("Lista Jugador: ")
    print(*lista_jugador, sep= ", ")

    print("Lista Ordenador: ")
    print(*lista_ordenador, sep= ", ")

def jugar():
    global numero_random
    numero_random = random.randint(1, 100) 
    print("Hola, comenzemos con este juego de adivinanza.")
    while True:
        if(Jugador()):
            print("Felicidades, adivinaste el número.")
            break

        if(Ordenador()):
            print("Lo siento, el ordenador adivinó el número.")
            break 
    MostrarListas()


while True:
    jugar()
    if(int(input("¿Deseas volver a jugar? 1:Si o 0:No ")) != 1):
        break




