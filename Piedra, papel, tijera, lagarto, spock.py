##Piedra, papel, tijera, lagarto, spock
import random as altr
opcioncpu=["piedra","papel","tijeras","lagarto","spock"]
revancha=0

while revancha==0:
 aleatorio=altr.randint(0,4)
 eleccioncpu=opcioncpu[aleatorio]
 jugador=str(input("Bienvenido a piedra papel o tijeras, por favor escriba la opción que desea jugar: "))
 jugador=jugador.lower()
 while jugador != "piedra" and jugador != "papel" and jugador != "tijeras" and jugador != "lagarto" and jugador != "spock":
     jugador=str(input("Ingreso de opción inválida, por favor vuelva a intentarlo: "))
     jugador=jugador.lower()
    
 if eleccioncpu == "piedra":
     if jugador == "piedra":
        print("Empate.")
        revancha=0
     elif jugador == "papel" or jugador == "spock":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 elif eleccioncpu == "papel":
     if jugador == "papel":
        print("Empate.")
        revancha=0
     elif jugador == "tijeras" or jugador == "lagarto":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 elif eleccioncpu == "tijeras":
     if jugador == "tijeras":
        print("Empate.")
        revancha=0
     elif jugador == "piedra" or jugador == "spock":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 elif eleccioncpu == "lagarto":
     if jugador == "lagarto":
        print("Empate.")
        revancha=0
     elif jugador == "piedra" or jugador == "tijeras":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 elif eleccioncpu == "spock":
     if jugador == "spock":
        print("Empate.")
        revancha=0
     elif jugador == "lagarto" or jugador == "papel":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1