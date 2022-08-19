##El siguiente programa debe acceder a la libreria random
import random as altr
opcioncpu=["piedra","papel","tijeras"]

revancha=0
while revancha==0:
 aleatorio=altr.randint(0,2)
 eleccioncpu=opcioncpu[aleatorio]
 jugador=str(input("Bienvenido a piedra papel o tijeras, por favor escriba la opción que desea jugar: "))
 jugador=jugador.lower()
 while jugador != "piedra" and jugador != "papel" and jugador != "tijeras":
     jugador=str(input("Ingreso de opción inválida, por favor vuelva a intentarlo: "))
     jugador=jugador.lower()
    
 if eleccioncpu == "piedra":
     if jugador == "piedra":
        print("Empate.")
        revancha=0
     elif jugador == "papel":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 elif eleccioncpu == "papel":
     if jugador == "papel":
        print("Empate.")
        revancha=0
     elif jugador == "tijeras":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1
 else:
     if jugador == "tijeras":
        print("Empate.")
        revancha=0
     elif jugador == "piedra":
        print("La computadora eligió ",eleccioncpu," el jugador gana.")
        revancha=0
     else:
        print("La computadora eligió ",eleccioncpu," el jugador pierde, buena suerte para la próxima.")
        revancha=1



