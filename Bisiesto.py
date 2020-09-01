def es_Bisiesto(año):

	

	if año%4==0 and not año%100==0:

		return "Es bisiesto"

	elif año%400==0:

		return "Es bisiesto"

	else:

		return "No es bisiesto"

print()
print(es_Bisiesto(int(input("Introduce un año para saber si es bisiesto: "))))