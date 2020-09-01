print("Vamos a verificar tu email")
email=input("Pon tu email: ")
arrobas=0
puntos=0
for i in range(len(email)):
	if email[i]=="@":
		arrobas=arrobas+1
	if email[i]==".":
		puntos=1
if arrobas==0 or puntos!=1:
	print("email incorrecto")
else:
	print("email correcto")	

