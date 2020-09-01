print("Vamos a verificar tu email")


def filtro(elem):
	return(elem == "@")

email = input("Introduce tu email: ")
f_email =list(filter(filtro,email))

if (len(f_email))==1:
	f_email= True
else:
	f_email=False	

puntos=0
for i in range(len(email)):
	if email[i]==".":
		puntos=1

if  puntos!=1 or f_email==False:
	print("email incorrecto")
else:
	print("email correcto")