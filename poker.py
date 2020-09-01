
import random

#vamos a preguntar cuantos jugadores juegan

def num_participantes():

	
	while True:

		print("¿Cuantos jugadores vais a jugar? (De 2 a 9)", "\n")

		participantes = int(input())

		print("\n")

		if participantes > 1 and participantes < 10:

			print("Sois",participantes,"para jugar al poker", "\n")

			break

		else:

			print("El numero no es correcto", "\n")

	return participantes

	

#Vamos a repartir a cada jugador 2 cartas de la baraja


jugadores=num_participantes()

BARAJA = "ASp 2p 3p 4p 5p 6p 7p 8p 9p 10p Jp Qp Kp ASc 2c 3c 4c 5c 6c 7c 8c 9c 10c Jc Qc Kc ASt 2t 3t 4t 5t 6t 7t 8t 9t 10t Jt Qt Kt ASd 2d 3d 4d 5d 6d 7d 8d 9d 10d Jd Qd Kd".split()

def elegirCarta(BARAJA):

	mano= random.sample(BARAJA,2)


	return mano


if jugadores == 2:


	manoJ1=elegirCarta(BARAJA)
	print("Jugador 1:", manoJ1)
	for cartas in manoJ1:
		manoJ1.remove(cartas)

	print(BARAJA)
		

	

	

	print("Jugador 2:", elegirCarta(BARAJA))

	

	'''[carta5=random.choice(BARAJA)
	BARAJA.remove(carta5)

	carta6=random.choice(BARAJA)
	BARAJA.remove(carta6)

	carta7=random.choice(BARAJA)
	BARAJA.remove(carta7)

	carta8=random.choice(BARAJA)
	BARAJA.remove(carta8)

	print("Vemos el flop")
	input()
	print(carta6,carta7,carta8)

	carta9=random.choice(BARAJA)
	BARAJA.remove(carta9)

	carta10=random.choice(BARAJA)
	BARAJA.remove(carta10)

	print("Vemos la siguiente carta")
	input()
	print(carta10)

	carta11=random.choice(BARAJA)
	BARAJA.remove(carta11)

	carta12=random.choice(BARAJA)
	BARAJA.remove(carta12)

	print("Vemos la siguiente carta")
	input()
	print(carta12)]'''




elif jugadores == 3:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)

	carta7=random.choice(BARAJA)
	BARAJA.remove(carta7)

	carta8=random.choice(BARAJA)
	BARAJA.remove(carta8)

	carta9=random.choice(BARAJA)
	BARAJA.remove(carta9)

	carta10=random.choice(BARAJA)
	BARAJA.remove(carta10)

	print("Vemos el flop")
	input()
	print(carta8,carta9,carta10)

	carta11=random.choice(BARAJA)
	BARAJA.remove(carta11)

	carta12=random.choice(BARAJA)
	BARAJA.remove(carta12)

	print("Vemos la siguiente carta")
	input()
	print(carta12)

	carta13=random.choice(BARAJA)
	BARAJA.remove(carta13)

	carta14=random.choice(BARAJA)
	BARAJA.remove(carta14)

	print("Vemos la siguiente carta")
	input()
	print(carta14)

elif jugadores == 4:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)

	carta9=random.choice(BARAJA)
	BARAJA.remove(carta9)

	carta10=random.choice(BARAJA)
	BARAJA.remove(carta10)

	carta11=random.choice(BARAJA)
	BARAJA.remove(carta11)

	carta12=random.choice(BARAJA)
	BARAJA.remove(carta12)

	print("Vemos el flop")
	input()
	print(carta10,carta11,carta12)

	carta13=random.choice(BARAJA)
	BARAJA.remove(carta13)

	carta14=random.choice(BARAJA)
	BARAJA.remove(carta14)

	print("Vemos la siguiente carta")
	input()
	print(carta14)

	carta15=random.choice(BARAJA)
	BARAJA.remove(carta15)

	carta16=random.choice(BARAJA)
	BARAJA.remove(carta16)

	print("Vemos la siguiente carta")
	input()
	print(carta16)

	

elif jugadores == 5:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)
	carta9= random.choice(BARAJA)
	BARAJA.remove(carta9)
	carta10 = random.choice(BARAJA)
	BARAJA.remove(carta10)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)
	print("Jugador 5:", carta9,carta10)

	carta11=random.choice(BARAJA)
	BARAJA.remove(carta11)

	carta12=random.choice(BARAJA)
	BARAJA.remove(carta12)

	carta13=random.choice(BARAJA)
	BARAJA.remove(carta13)

	carta14=random.choice(BARAJA)
	BARAJA.remove(carta14)

	print("Vemos el flop")
	input()
	print(carta12,carta13,carta14)

	carta15=random.choice(BARAJA)
	BARAJA.remove(carta15)

	carta16=random.choice(BARAJA)
	BARAJA.remove(carta16)

	print("Vemos la siguiente carta")
	input()
	print(carta16)

	carta17=random.choice(BARAJA)
	BARAJA.remove(carta17)

	carta18=random.choice(BARAJA)
	BARAJA.remove(carta18)

	print("Vemos la siguiente carta")
	input()
	print(carta18)

	

elif jugadores == 6:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)
	carta9= random.choice(BARAJA)
	BARAJA.remove(carta9)
	carta10 = random.choice(BARAJA)
	BARAJA.remove(carta10)
	carta11= random.choice(BARAJA)
	BARAJA.remove(carta11)
	carta12 = random.choice(BARAJA)
	BARAJA.remove(carta12)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)
	print("Jugador 5:", carta9,carta10)
	print("Jugador 6:", carta11,carta12)

	carta13=random.choice(BARAJA)
	BARAJA.remove(carta13)

	carta14=random.choice(BARAJA)
	BARAJA.remove(carta14)

	carta15=random.choice(BARAJA)
	BARAJA.remove(carta15)

	carta16=random.choice(BARAJA)
	BARAJA.remove(carta16)

	print("Vemos el flop")
	input()
	print(carta14,carta15,carta16)

	carta17=random.choice(BARAJA)
	BARAJA.remove(carta17)

	carta18=random.choice(BARAJA)
	BARAJA.remove(carta18)

	print("Vemos la siguiente carta")
	input()
	print(carta18)

	carta19=random.choice(BARAJA)
	BARAJA.remove(carta19)

	carta20=random.choice(BARAJA)
	BARAJA.remove(carta20)

	print("Vemos la siguiente carta")
	input()
	print(carta20)

	

elif jugadores == 7:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)
	carta9= random.choice(BARAJA)
	BARAJA.remove(carta9)
	carta10 = random.choice(BARAJA)
	BARAJA.remove(carta10)
	carta11= random.choice(BARAJA)
	BARAJA.remove(carta11)
	carta12 = random.choice(BARAJA)
	BARAJA.remove(carta12)
	carta13= random.choice(BARAJA)
	BARAJA.remove(carta13)
	carta14 = random.choice(BARAJA)
	BARAJA.remove(carta14)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)
	print("Jugador 5:", carta9,carta10)
	print("Jugador 6:", carta11,carta12)
	print("Jugador 7:", carta13,carta14)

	carta15=random.choice(BARAJA)
	BARAJA.remove(carta15)

	carta16=random.choice(BARAJA)
	BARAJA.remove(carta16)

	carta17=random.choice(BARAJA)
	BARAJA.remove(carta17)

	carta18=random.choice(BARAJA)
	BARAJA.remove(carta18)

	print("Vemos el flop")
	input()
	print(carta16,carta17,carta18)

	carta19=random.choice(BARAJA)
	BARAJA.remove(carta19)

	carta20=random.choice(BARAJA)
	BARAJA.remove(carta20)

	print("Vemos la siguiente carta")
	input()
	print(carta20)

	carta21=random.choice(BARAJA)
	BARAJA.remove(carta21)

	carta22=random.choice(BARAJA)
	BARAJA.remove(carta22)

	print("Vemos la siguiente carta")
	input()
	print(carta22)

	

elif jugadores == 8:

	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)
	carta9= random.choice(BARAJA)
	BARAJA.remove(carta9)
	carta10 = random.choice(BARAJA)
	BARAJA.remove(carta10)
	carta11= random.choice(BARAJA)
	BARAJA.remove(carta11)
	carta12 = random.choice(BARAJA)
	BARAJA.remove(carta12)
	carta13= random.choice(BARAJA)
	BARAJA.remove(carta13)
	carta14 = random.choice(BARAJA)
	BARAJA.remove(carta14)
	carta15= random.choice(BARAJA)
	BARAJA.remove(carta15)
	carta16 = random.choice(BARAJA)
	BARAJA.remove(carta16)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)
	print("Jugador 5:", carta9,carta10)
	print("Jugador 6:", carta11,carta12)
	print("Jugador 7:", carta13,carta14)
	print("Jugador 8:", carta15,carta16)

	carta17=random.choice(BARAJA)
	BARAJA.remove(carta17)

	carta18=random.choice(BARAJA)
	BARAJA.remove(carta18)

	carta19=random.choice(BARAJA)
	BARAJA.remove(carta19)

	carta20=random.choice(BARAJA)
	BARAJA.remove(carta20)

	print("Vemos el flop")
	input()
	print(carta18,carta19,carta20)

	carta21=random.choice(BARAJA)
	BARAJA.remove(carta21)

	carta22=random.choice(BARAJA)
	BARAJA.remove(carta22)

	print("Vemos la siguiente carta")
	input()
	print(carta22)

	carta23=random.choice(BARAJA)
	BARAJA.remove(carta23)

	carta24=random.choice(BARAJA)
	BARAJA.remove(carta24)

	print("Vemos la siguiente carta")
	input()
	print(carta24)

	

else:

	
	carta1= random.choice(BARAJA)
	BARAJA.remove(carta1)
	carta2 = random.choice(BARAJA)
	BARAJA.remove(carta2)
	carta3= random.choice(BARAJA)
	BARAJA.remove(carta3)
	carta4 = random.choice(BARAJA)
	BARAJA.remove(carta4)
	carta5= random.choice(BARAJA)
	BARAJA.remove(carta5)
	carta6 = random.choice(BARAJA)
	BARAJA.remove(carta6)
	carta7= random.choice(BARAJA)
	BARAJA.remove(carta7)
	carta8 = random.choice(BARAJA)
	BARAJA.remove(carta8)
	carta9= random.choice(BARAJA)
	BARAJA.remove(carta9)
	carta10 = random.choice(BARAJA)
	BARAJA.remove(carta10)
	carta11= random.choice(BARAJA)
	BARAJA.remove(carta11)
	carta12 = random.choice(BARAJA)
	BARAJA.remove(carta12)
	carta13= random.choice(BARAJA)
	BARAJA.remove(carta13)
	carta14 = random.choice(BARAJA)
	BARAJA.remove(carta14)
	carta15= random.choice(BARAJA)
	BARAJA.remove(carta15)
	carta16 = random.choice(BARAJA)
	BARAJA.remove(carta16)
	carta17= random.choice(BARAJA)
	BARAJA.remove(carta17)
	carta18 = random.choice(BARAJA)
	BARAJA.remove(carta18)

	print("Jugador 1:", carta1,carta2)
	print("Jugador 2:", carta3,carta4)
	print("Jugador 3:", carta5,carta6)
	print("Jugador 4:", carta7,carta8)
	print("Jugador 5:", carta9,carta10)
	print("Jugador 6:", carta11,carta12)
	print("Jugador 7:", carta13,carta14)
	print("Jugador 8:", carta15,carta16)
	print("Jugador 9:", carta17,carta18)

	carta19=random.choice(BARAJA)
	BARAJA.remove(carta19)

	carta20=random.choice(BARAJA)
	BARAJA.remove(carta20)

	carta21=random.choice(BARAJA)
	BARAJA.remove(carta21)

	carta22=random.choice(BARAJA)
	BARAJA.remove(carta22)

	print("Vemos el flop")
	input()
	print(carta20,carta21,carta22)

	carta23=random.choice(BARAJA)
	BARAJA.remove(carta23)

	carta24=random.choice(BARAJA)
	BARAJA.remove(carta24)

	print("Vemos la siguiente carta")
	input()
	print(carta24)

	carta25=random.choice(BARAJA)
	BARAJA.remove(carta25)

	carta26=random.choice(BARAJA)
	BARAJA.remove(carta26)

	print("Vemos la siguiente carta")
	input()
	print(carta26)

	














	













