import random

class Carta():

	def __init__(self,nombre,valor,palo):

		self.nombre= nombre
		self.palo= palo
		self.valor= valor
		self.vista=True

	def __repr__(self):

		if self.vista:

			return "{} de {}".format(self.nombre,self.palo)

		else:

			return "Carta"

class Baraja():

  def Mezclar(self, veces=1 ):

    random.shuffle(self.cartas)

    return print("Baraja mezclada")

  def Robar(self):

    return self.cartas.pop(0)

class BarajaStandar(Baraja):

	def __init__(self):
		
		self.cartas=[]

		palos=['Bastos','Copas','Espadas','Oros']

		valores={'Dos':2,
				 'Cuatro':4,
				 'Cinco':5,
				 'Seis':6,
				 'Siete':7,
				 'Jota':8,
				 'Caballo':9,
				 'Rey':10,
				 'Tres':11,
				 'As':12}


		for nombre in valores:
			for palo in palos:

				self.cartas.append(Carta(nombre,valores[nombre],palo))




