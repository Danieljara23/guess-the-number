import random

playing=True
numero=random.randint(1,100)
intentos_usuario = []
intentos_computadora = []
turno=True

while playing:
    if turno == True:
        intento_User=int(input("Es tu turno, adivina un número entre 1 y 100: "))
        intentos_usuario.append(intento_User)
        if intento_User > 100 or intento_User < 1:
            print("El número debe estar entre 1 y 100")
        elif intento_User ==  numero:
            print(f"¡Lo has adivinado! El número era {numero}")
            print(f"Intentos del usuario: {intentos_usuario}")
            print(f"Intentos del computador: {intentos_computadora}")
            playing=False
        elif  intento_User < numero:
            print("Es mayor")
        else:
            print("Es menor")
        turno= False
    else:
      print("Es mi turno")
      intento_Comp=random.randint(1,100)
      print(f"Elijo el número: {intento_Comp}")
      intentos_computadora.append(intento_Comp)
      if intento_Comp ==  numero:
        print(f"¡Lo he adivinado! El número era {numero}")
        print(f"Intentos del usuario: {intentos_usuario}")
        print(f"Intentos del computador: {intentos_computadora}")
        playing=False
      elif intento_Comp  < numero:
        print("Es mayor")
      else:
        print("Es menor")
    
    turno=True

    




    