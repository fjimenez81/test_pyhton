def main():

	mensaje=input("Introduce un mensaje: ")

	key=int(input("Introduce una Key[1-26]: "))

	modo=input("Que desea hacer ,cifrar o descifrar [C/D]: ")

	if modo.lower().startswith("c"):

		modo="cifrar"

	elif modo.lower().startswith("d"):

		modo="descifrar"

	traduccion= codificar(mensaje,key,modo)

	if modo=="cifrar":

		print("El mensaje cifrado es: ",traduccion)

	elif modo=="descifrar":

		print("El mensaje descifrado es: ",traduccion)


def codificar(mensaje,key,modo):

	mensaje=mensaje.upper()

	traduccion=""

	letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

	for i in mensaje:

		if i in letras:

			num=letras.find(i)

			if modo=="cifrar":

				num+=key

			elif modo=="descifrar":

				num-=key

			if num>=len(letras):

				num-=len(letras)

			elif num<0:

				num+=len(letras)

			traduccion+=letras[num]

		else:

			traduccion+=i

	return traduccion



if __name__=="__main__":

	main()






