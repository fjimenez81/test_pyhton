import random

def obtenerNumeroSecreto(digitosNum):

	numeros= list(range(10))

	random.shuffle(numeros)

	numSecreto=""

	for i in range(digitosNum):

		numSecreto+=str(numeros[i])

	return numSecreto

def obtenerPistas(conjetura,numSecreto):

	if conjetura==numSecreto:

		return "¡Lo has adivinado!"

	pista=[]

	for i in range(len(conjetura)):

		if conjetura[i]==numSecreto[i]:

			pista.append("Fermi")

		elif conjetura in numSecreto:

			pista.append("Pico")

	if len(pista)==0:

		return "Panecillos"

	pista.sort()

	return "".join(pista)

def esSoloDigitos(num):

	# Devuelve True si el número se compone sólo de dígitos. De lo contrario False

	if num=="":
		return False

	for i in num:

		if i not in "0 1 2 3 4 5 6 7 8 9".split():
			return False

	return True

def jugarDeNuevo():
	
	print("¿Quieres jugar de nuevo? (si o no)")

	return input().lower().startswith("s")

digitosNum=3
MAXADIVINANZAS=10

print("Estoy pensando en numero de %s digitos.Intenta adivinar cual es." %(digitosNum))

print("Aqui algunas pistas:")
print("Cuando digo:        significa:")
print("  Pico               Un digito es correcto pero en posicion incorrecta")
print("  Fermi              Un digito es correcto y en la posicion correcta")
print(" Panecillos          Ninguno es correcto")

while True:

	numSecreto=obtenerNumeroSecreto(digitosNum)

	print("He pensado un numero.Tienes %s intentos para adivinarlo." %(MAXADIVINANZAS))

	numIntentos=1

	while numIntentos<=MAXADIVINANZAS:

		conjetura=""

		while len(conjetura)!=digitosNum or not esSoloDigitos(conjetura):

			print("Conjetura#%s"%numIntentos)

			conjetura=input()

		pista= obtenerPistas(conjetura,numSecreto)

		print(pista)

		numIntentos+=1

		if conjetura==numSecreto:

			break

		if numIntentos>MAXADIVINANZAS:

			print("Te has quedado sin intentos.La respuesta era %s" %(numSecreto))

	if not jugarDeNuevo():

		break
				
