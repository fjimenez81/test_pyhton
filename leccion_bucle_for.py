print("Vamos a ver si tu email es correcto")
contador=0
tuemail=input("Introduce tu email: ")
for i in tuemail:
	if (i=="@" or i=="."):
		contador=contador+1
if contador==2:
	print("El email es correcto")
else:
	print("El email es incorrecto")

