print("Vamos a validar contraseña")
clave=input("Introduce tu contraseña: ")
contador=0
for i in range(len(clave)): 
	if clave[i]==" ":
		contador=1
if len(clave)<8 or contador>0:
	print("contraseña erronea")
else:
	print("contraseña correcta")