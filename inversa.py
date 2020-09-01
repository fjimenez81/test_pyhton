def inversa(x):

	cont=""

	for i in x:

		cont=i+cont

	return cont

print(inversa(input("Ingresa algo para darlo la vuelta: ")))