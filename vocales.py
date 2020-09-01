print("¡Soy el mostruo de las letras pero lo que mas me gustan son las vocales!")


lista_vocales=["a","e","i","o","u"]
vocales=lista_vocales
lista_numeros=["1","2","3","4","5","6","7","8","9","0"]
numeros=lista_numeros


def juego_letras():

	letra=str.lower(input("¡Dame una letra por favor!: "))


	if letra in vocales:

		print("JAJAJAJJAJA!!! ¡Muchas gracias me encantan las vocales!")

	elif letra in numeros:

		print("AAAARRRRRGGGHHHH!!!!¡No me gustan los numeros!")

	else:

		print("PSE! PSE! Vale pero me podias haber dado una vocal")


jugarDeNuevo="si"

while (jugarDeNuevo=="si" or jugarDeNuevo=="s"):

	juego_letras()

	print("¿Quieres darme otra? (si o no)")

	jugarDeNuevo=str.lower(input())

print("¡Hasta otra!¡Me vas ha matar de hambre!")
