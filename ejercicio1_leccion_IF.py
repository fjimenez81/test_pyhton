print("Devuelveme el numero mayor")
numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))
def devuelveMax(n1,n2):
	if n1>n2:
		print("El primer numero es el mayor: ",n1)
	elif n1<n2:
		print("El segundo numero es el mayor: ",n2)
	else:
		print("Son iguales")
	 
devuelveMax(numero1,numero2)	