#Este es el juego de adivinar el numero
import random

intentosRealizados=0

print("¡Hola! , ¿como te llamas?")
miNombre=input()

numero= random.randint(1,20)
print("Bueno,",miNombre,"estoy pensando en un numero entre 1 y 20, intenta adivinarlo!")

while intentosRealizados<6:
	print("Mete un numero: ")
	estimacion=int(input())

	intentosRealizados=intentosRealizados+1

	if estimacion<numero:
		print("La estimacion es muy baja")

	if estimacion>numero:
		print("La estimacion es muy alta")

	if estimacion==numero:
		break

if estimacion==numero:
	intentosRealizados=str(intentosRealizados)
	print("Buen trabajo!",miNombre, "lo has acertado en :",intentosRealizados,"intentos")

if estimacion!= numero:
	numero=str(numero)
	print("Pues no. El numero que estaba pensando era: ",numero)	

		 		





