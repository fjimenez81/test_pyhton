import random

print("¡Adivina la palabra secreta!")


OCASIONES=["0","1","2","3","4","5","6"]

palabras = "hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra".split() 

def obtener_palabra(ListaPalabras):

	indiceDePalabras= random.randint(0,len(ListaPalabras)-1)

	return ListaPalabras[indiceDePalabras]


def mostrar_tablero(OCASIONES,LetraIncorrecta,LetraCorrecta,palabraSecreta):

	print(OCASIONES[len(LetraIncorrecta)])
	print()

	print("Letras Incorrectas:", end="")

	for letra in LetraIncorrecta:

		print(letra,end="")

		print()

	espaciosVacios=	"_" * len(palabraSecreta)

	for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas

		if palabraSecreta[i] in LetraCorrecta:

			espaciosVacios= espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

	for letra in espaciosVacios: # mostrar la palabra secreta con espacios entre cada letra

		print(letra, end=" ")

	print()


def obtener_intento(letrasProbadas):

	# Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa
	

	while True:

		print("Adivina una letra")

		intento=input()

		intento=intento.lower()

		if len(intento)!= 1:

			print("Introduce una letra")

		elif intento in letrasProbadas:
		
			print("Ya has probado esa letra, prueva otra")

		elif intento not in "abcdefghijklmnñopqrstuvwxyz":

			print("Ingresa un LETRA")

		else:

			return intento


def jugarDeNuevo():# esta funcion es para jugar de nuevo

	print("¿Quiers jugar de nuevo? (si o no)")

	return input().lower().startswith("s")

#EMPEZAMOS EL PROGRAMA

LetraIncorrecta=""

LetraCorrecta=""

palabraSecreta= obtener_palabra(palabras)

juegoTerminado=False

while True:

	mostrar_tablero(OCASIONES,LetraIncorrecta,LetraCorrecta,palabraSecreta)

	intento= obtener_intento(LetraIncorrecta+LetraCorrecta)

	if intento in palabraSecreta:

		LetraCorrecta=LetraCorrecta+intento

		encontradasTodasLetras=True

		for i in range(len(palabraSecreta)):

			if palabraSecreta[i] not in LetraCorrecta:

				encontradasTodasLetras=False

			break

		if encontradasTodasLetras:

			print("Has encontrado la palabra secreta!", palabraSecreta,"¡Has ganado!")

			juegoTerminado= True


	else:

		LetraIncorrecta = LetraIncorrecta+intento

		if len(LetraIncorrecta) == len(OCASIONES)-1:

			mostrar_tablero(OCASIONES,LetraIncorrecta,LetraCorrecta,palabraSecreta)

			print("Te has quedado sin intentos.Despues de: ",str(len(LetraIncorrecta)),"fallos y de: ",str(len(LetraCorrecta)),"aciertos.La palabra secreta era: ",palabraSecreta)


			juegoTerminado=True

	if juegoTerminado:

		if jugarDeNuevo():

			LetraIncorrecta=""

			LetraCorrecta=""

			juegoTerminado=False

			palabraSecreta= obtener_palabra(palabras)

		else:

			break




















