print("Press 'a', 'p' or 't' to play, there are two players, depending on the answers, the winner, or a draw will be defined.")

global variable_global


def checar_longitud(tirada):
  if len(tirada)!=1:
    return False
  else:
    return True

def checar_tirada(tirada):
  if(tirada!="a" and tirada!="p" and tirada!="t"):
    return False
  else:
    return True

def definir_ganador(tirada_ana,tirada_juan):
  if(tirada_ana=="p" and tirada_juan=="a"):
    print("Gana Ana")
  if(tirada_ana=="a" and tirada_juan=="p"):
    print("Gana Juan")
  if(tirada_ana=="a" and tirada_juan=="t"):
    print("Gana Ana")
  if(tirada_ana=="t" and tirada_juan=="a"):
    print("Gana Juan")
  if(tirada_ana=="t" and tirada_juan=="p"):
    print("Gana Ana")
  if(tirada_ana=="p" and tirada_juan=="t"):
    print("Gana Juan")
  if(tirada_ana==tirada_juan):
    print("Empate")

def jugar(tirada_ana,tirada_juan):
  if checar_longitud(tirada_ana)==True and checar_longitud(tirada_juan)==True:
    if checar_tirada(tirada_ana)==True and checar_tirada(tirada_juan)==True:
      definir_ganador(tirada_ana,tirada_juan)
    else:
      print("Tirada incorrecta")
  else:
    print("La longitud de la tirada debe ser 1")


while True:
	print("player 1:")
	ana=input()
	print("player 2:")
	juan=input()
	jugar(ana,juan)
	respuesta=input("Quieres volver a jugar? 1) Sí 2) No \n")
	if(respuesta=="2"):
		break