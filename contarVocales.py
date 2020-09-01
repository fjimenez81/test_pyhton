
def contarVocales(cadena):

	cont=0

	vocales="aeiou"

	for x in vocales:

		for i in cadena:

			if  i==x:

				cont+=1

	return cont,"Vocales tiene la frase"

print(contarVocales(input("Ingrese una frase: ")))