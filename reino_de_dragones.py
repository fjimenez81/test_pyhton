import random
import time

def mostrarIntroducion():

	print('''Estas en la tierra de los dragones,
frente a ti dos cuevas.Una pertenece al
dragon amigable que compatirá un tesoro
contigo la otra pertenece al dragon malo 
y en cuanto te vea te devorará''')

def elegirCueva():
	cueva=""

	while (cueva!="1" and cueva!="2"):
		print("¿A que cueva quieres entrar?A la 1 o a la 2")
		cueva=str(input())

	return cueva
	
def explorarCueva(cuevaElegida):
	print("Te aproximas a la cueva...")
	time.sleep(2)
	print("Es oscura y espeluznante...")
	time.sleep(2)
	print("Aparece un dragon frente a ti , abre sus fauces y ...")
	time.sleep(2)

	cuevaAmigable=random.randint(1,2)

	oro=0

	if cuevaElegida==str(cuevaAmigable):

		print("Toma un tesoro!!")

		cofre=random.randint(50,200)

		oro+=cofre

		print("Has conseguido: ", oro ,"monedas de oro")

		

	else:
		print("El dragon te comió!!")

		print("Te han quitado todos los tesoros")

		
jugarDeNuevo="si"


while (jugarDeNuevo=="si" or jugarDeNuevo=="s"):

	mostrarIntroducion()

	numeroDeCueva= elegirCueva()

	explorarCueva(numeroDeCueva)

	print("¿Quieres jugar de nuevo? (si o no)")

	jugarDeNuevo=input()












					


