import random

from functools import reduce

class Carta():

    def __init__(self,nombre,valor,palo,potenciador,valoresFinales,palo_id):

        self.nombre= nombre
        self.palo= palo
        self.valor= valor
        self.potenciador= potenciador
        self.valoresFinales=valoresFinales
        self.palo_id=palo_id
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

    def Robar(self,posicion):

        return self.cartas.pop(posicion)

    def AsignarPalo(self):

        pinta=self.cartas.pop(-1)
        self.cartas.append(pinta)

        return pinta

    def Cantar(self,listaJugador,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros):

        caballos=filter(lambda caballos: caballos.valoresFinales == 3, listaJugador)

        reyes=filter(lambda reyes: reyes.valoresFinales == 4,listaJugador)

                  
        for caballo in caballos:
            for rey in reyes:

                if caballo.palo_id==1 and caballo.palo_id==2 and caballo.palo_id==3 and caballo.palo_id==4:

                    return "TuteCaballos"

                elif rey.palo_id==1 and rey.palo_id==2 and rey.palo_id==3 and rey.palo_id==4:

                    return "TuteReyes"

                elif caballo and rey in listaJugador:

                    if idPalo==1:

                        if caballo.palo_id==1 and rey.palo_id==1 and parejaBastos==0:

                            return "40Bastos"

                                              
                        elif caballo.palo_id==2 and rey.palo_id==2 and parejaCopas==0:

                            return "20Copas"   

                                       
                        elif caballo.palo_id==3 and rey.palo_id==3 and parejaEspadas==0:

                            return "20Espadas"

                                                             
                        elif caballo.palo_id==4 and rey.palo_id==4 and parejaOros==0:

                            return "20Oros"

                    elif idPalo==2:

                        if caballo.palo_id==1 and rey.palo_id==1 and parejaBastos==0:

                            return "20Bastos"

                                              
                        elif caballo.palo_id==2 and rey.palo_id==2 and parejaCopas==0:

                            return "40Copas"   

                                       
                        elif caballo.palo_id==3 and rey.palo_id==3 and parejaEspadas==0:

                            return "20Espadas"

                                                             
                        elif caballo.palo_id==4 and rey.palo_id==4 and parejaOros==0:

                            return "20Oros"

                        

                    elif idPalo==3:

                        if caballo.palo_id==1 and rey.palo_id==1 and parejaBastos==0:

                            return "20Bastos"

                                              
                        elif caballo.palo_id==2 and rey.palo_id==2 and parejaCopas==0:

                            return "20Copas"   

                                       
                        elif caballo.palo_id==3 and rey.palo_id==3 and parejaEspadas==0:

                            return "40Espadas"

                                                             
                        elif caballo.palo_id==4 and rey.palo_id==4 and parejaOros==0:

                            return "20Oros"

                    elif idPalo==4:

                        if caballo.palo_id==1 and rey.palo_id==1 and parejaBastos==0:

                            return "20Bastos"

                                              
                        elif caballo.palo_id==2 and rey.palo_id==2 and parejaCopas==0:

                            return "20Copas"   

                                       
                        elif caballo.palo_id==3 and rey.palo_id==3 and parejaEspadas==0:

                            return "20Espadas"

                                                             
                        elif caballo.palo_id==4 and rey.palo_id==4 and parejaOros==0:

                            return "40Oros"

    def CuentaCartas(self):

        return len(self.cartas)

                    
                        
class BarajaStandar(Baraja):

    def __init__(self):
        
        self.cartas=[]

        palos={'Bastos':1,'Copas':2,'Espadas':3,'Oros':4}

        valores={'Dos':2,
                 'Cuatro':4,
                 'Cinco':5,
                 'Seis':6,
                 'Siete':7,
                 'Sota':8,
                 'Caballo':9,
                 'Rey':10,
                 'Tres':11,
                 'As':12}

        valoresFinales={'Dos':0,
                        'Cuatro':0,
                        'Cinco':0,
                        'Seis':0,
                        'Siete':0,
                        'Sota':2,
                        'Caballo':3,
                        'Rey':4,
                        'Tres':10,
                        'As':11}


        
  

        for nombre in valores:



            for palo in palos:

                potenciador= valores[nombre]*7

                palo_id= palos[palo]

                self.cartas.append(Carta(nombre,valores[nombre],palo,potenciador,valoresFinales[nombre],palo_id))


print()
baraja=BarajaStandar()
baraja.Mezclar()
cartaPalo=baraja.AsignarPalo()
idPalo=cartaPalo.palo_id
manoj1=baraja.cartas[0:6]
manoTino=baraja.cartas[6:12]
montonJ1=[]
montonTino=[]
parejaBastos=0
parejaCopas=0
parejaEspadas=0
parejaOros=0
turno=True
contador=baraja.CuentaCartas()
puntosj1=[]
puntosTino=[]
print()
print(contador)
print()

  

while True:

    if contador>12: 

        print("Estas son las cartas de jugador 1: {}".format(manoj1))
        print()
        print("Estas son las cartas de Tino: {}".format(manoTino))
        print()
        print("La partida pinta en: {}".format(cartaPalo.palo))
        print()

        

        if turno:

            while True:

                try:

                    posicionj1=int(input("Jugador 1 introduce un numero de 0 a 5: "))
                    cartaj1=manoj1[posicionj1]
                    break
                    
                except IndexError:

                    print("Te has equivocado de carta, intentalo de nuevo siempre de 0 a 5")

            
            print()    
            print("El jugador 1 ha echado: {}".format(cartaj1))
            print()
            print("Tino tiene que echar una carta del mismo palo y sino tiene , del mismo palo que pinta la partida")
            print()
            print()
            posicionTino=int(input("Tino introduce un numero de 0 a 5: "))
            cartaTino=manoTino[posicionTino]
            print()
            print("Tino ha echado: {}".format(cartaTino))
            print()
           
                      
        else:

            while True:

                try:

                    posicionTino=int(input("Tino introduce un numero de 0 a 5: "))
                    cartaTino=manoTino[posicionTino]
                    break
                    
                except IndexError:

                    print("Te has equivocado de carta, intentalo de nuevo siempre de 0 a 5")

            
            print()
            print("Tino ha echado: {}".format(cartaTino))
            print()
            print()
            print("Jugador 1 tiene que echar una carta del mismo palo y sino tiene , del mismo palo que pinta la partida")
            print()
            posicionj1=int(input("Jugador 1 introduce un numero de 0 a 5: "))
            cartaj1=manoj1[posicionj1]
            print()
            print("El jugador 1 ha echado: {}".format(cartaj1))    
            print()

            
            
        cartasMesa=[]    
        cartasMesa.append(cartaj1)
        cartasMesa.append(cartaTino)
        total=cartaj1.valoresFinales+cartaTino.valoresFinales
        print()
        print("En la mesa estan estas cartas: ",cartasMesa)
        print()
        print()

        if cartaj1==cartaPalo.palo and cartaTino==cartaPalo.palo:

            cartaj1.valor=cartaj1.potenciador

            cartaTino.valor= cartaTino.potenciador

        elif cartaj1.palo == cartaPalo.palo:

            cartaj1.valor=cartaj1.potenciador

        elif cartaTino.palo == cartaPalo.palo:

            cartaTino.valor= cartaTino.potenciador

        if cartaj1.valor > cartaTino.valor :

                print("Gana jugador 1!!")
                print()
                print()
                montonJ1+=cartasMesa
                puntosj1.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                cartaRobada=baraja.Robar(12)
                manoj1.append(cartaRobada)
                cartaRobada=baraja.Robar(12)
                manoTino.append(cartaRobada)
                cantaj1=baraja.Cantar(manoj1,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)
                print()

                if cantaj1=="40Bastos":

                    parejaBastos=1
                    puntosj1.append(40)

                elif cantaj1=="20Bastos":

                    parejaBastos=1
                    puntosj1.append(20)

                elif cantaj1=="40Copas":

                    parejaCopas=1
                    puntosj1.append(40)

                elif cantaj1=="20Copas":

                    parejaCopas=1
                    puntosj1.append(20)

                elif cantaj1=="40Espadas":

                    parejaEspadas=1
                    puntosj1.append(40)

                elif cantaj1=="20Espadas":

                    parejaEspadas=1
                    puntosj1.append(20)

                elif cantaj1=="40Oros":

                    parejaOros=1
                    puntosj1.append(40)

                elif cantaj1=="20Oros":

                    parejaOros=1
                    puntosj1.append(20)

                elif cantaj1=="TuteCaballos":

                    puntosj1.append(1000)
                    break

                elif cantaj1=="TuteReyes":

                    puntosj1.append(1000)
                    break

                print(cantaj1)
                print(contador)                    
                turno=True
                contador=contador-2

        elif cartaj1.valor==cartaTino.valor:

            if turno==True:

                print("Gana Jugador 1!!")
                print()
                print()
                montonJ1+=cartasMesa
                puntosj1.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                cartaRobada=baraja.Robar(12)
                manoj1.append(cartaRobada)
                cartaRobada=baraja.Robar(12)
                manoTino.append(cartaRobada)
                cantaj1=baraja.Cantar(manoj1,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

                if cantaj1=="40Bastos":

                    parejaBastos=1
                    puntosj1.append(40)

                elif cantaj1=="20Bastos":

                    parejaBastos=1
                    puntosj1.append(20)

                elif cantaj1=="40Copas":

                    parejaCopas=1
                    puntosj1.append(40)

                elif cantaj1=="20Copas":

                    parejaCopas=1
                    puntosj1.append(20)

                elif cantaj1=="40Espadas":

                    parejaEspadas=1
                    puntosj1.append(40)

                elif cantaj1=="20Espadas":

                    parejaEspadas=1
                    puntosj1.append(20)

                elif cantaj1=="40Oros":

                    parejaOros=1
                    puntosj1.append(40)

                elif cantaj1=="20Oros":

                    parejaOros=1
                    puntosj1.append(20)

                elif cantaj1=="TuteCaballos":

                    puntosj1.append(1000)
                    break

                elif cantaj1=="TuteReyes":

                    puntosj1.append(1000)
                    break

                print()
                print(cantaj1)
                print(contador)
                print()
                turno=True
                contador=contador-2
                

            else:

                print("Gana Tino!!")
                print()
                print()
                montonTino+=cartasMesa
                puntosTino.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                cartaRobada=baraja.Robar(12)
                manoj1.append(cartaRobada)
                cartaRobada=baraja.Robar(12)
                manoTino.append(cartaRobada)
                cantaTino=baraja.Cantar(manoTino,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

                if cantaTino=="40Bastos":

                    parejaBastos=1
                    puntosTino.append(40)

                elif cantaTino=="20Bastos":

                    parejaBastos=1
                    puntosTino.append(20)

                elif cantaTino=="40Copas":

                    parejaCopas=1
                    puntosTino.append(40)

                elif cantaTino=="20Copas":

                    parejaCopas=1
                    puntosTino.append(20)

                elif cantaTino=="40Espadas":

                    parejaEspadas=1
                    puntosTino.append(40)

                elif cantaTino=="20Espadas":

                    parejaEspadas=1
                    puntosTino.append(20)

                elif cantaTino=="40Oros":

                    parejaOros=1
                    puntosTino.append(40)

                elif cantaTino=="20Oros":

                    parejaOros=1
                    puntosTino.append(20)

                elif cantaTino=="TuteCaballos":

                    puntosTino.append(1000)
                    break

                elif cantaTino=="TuteReyes":

                    puntosTino.append(1000)
                    break

                print()
                print(cantaTino)
                print(contador)
                print()
                turno=False
                contador=contador-2

                
            
        else:

            print("Gana Tino!!")
            print()
            print()
            montonTino+=cartasMesa
            puntosTino.append(total)
            manoj1.remove(cartaj1)
            manoTino.remove(cartaTino)
            cartaRobada=baraja.Robar(12)
            manoj1.append(cartaRobada)
            cartaRobada=baraja.Robar(12)
            manoTino.append(cartaRobada)
            cantaTino=baraja.Cantar(manoTino,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

            if cantaTino=="40Bastos":

                parejaBastos=1
                puntosTino.append(40)

            elif cantaTino=="20Bastos":

                parejaBastos=1
                puntosTino.append(20)

            elif cantaTino=="40Copas":

                parejaCopas=1
                puntosTino.append(40)

            elif cantaTino=="20Copas":

                parejaCopas=1
                puntosTino.append(20)

            elif cantaTino=="40Espadas":

                parejaEspadas=1
                puntosTino.append(40)

            elif cantaTino=="20Espadas":

                parejaEspadas=1
                puntosTino.append(20)

            elif cantaTino=="40Oros":

                parejaOros=1
                puntosTino.append(40)

            elif cantaTino=="20Oros":

                parejaOros=1
                puntosTino.append(20)

            elif cantaTino=="TuteCaballos":

                puntosTino.append(1000)
                break

            elif cantaTino=="TuteReyes":

                puntosTino.append(1000)
                break

            print()
            print(cantaTino)
            print(contador)
            print()
            turno=False
            contador=contador-2

    elif contador>0 and contador<13:

        print("Estas son las cartas de jugador 1: {}".format(manoj1))
        print()
        print("Estas son las cartas de Tino: {}".format(manoTino))
        print()
        print("La partida pinta en: {}".format(cartaPalo.palo))
        print()

        

        if turno:

            posicionj1=int(input("Jugador 1 introduce un numero de 0 a 5: "))
            cartaj1=manoj1[posicionj1]
            print()
            print("El jugador 1 ha echado: {}".format(cartaj1))
            print()
            print("Tino tiene que echar una carta del mismo palo y sino tiene , del mismo palo que pinta la partida")
            print()
            print()
            posicionTino=int(input("Tino introduce un numero de 0 a 5: "))
            cartaTino=manoTino[posicionTino]
            print()
            print("Tino ha echado: {}".format(cartaTino))
            print()
            
            

        else:

            posicionTino=int(input("Tino introduce un numero de 0 a 5: "))
            cartaTino=manoTino[posicionTino]
            print()
            print("Tino ha echado: {}".format(cartaTino))
            print()
            print()
            print("Jugador 1 tiene que echar una carta del mismo palo y sino tiene , del mismo palo que pinta la partida")
            print()
            posicionj1=int(input("Jugador 1 introduce un numero de 0 a 5: "))
            cartaj1=manoj1[posicionj1]
            print()
            print("El jugador 1 ha echado: {}".format(cartaj1))    
            print()
            
        cartasMesa=[]    
        cartasMesa.append(cartaj1)
        cartasMesa.append(cartaTino)
        total=cartaj1.valoresFinales+cartaTino.valoresFinales
        print()
        print("En la mesa estan estas cartas: ",cartasMesa)
        print()
        print()

        if cartaj1==cartaPalo.palo and cartaTino==cartaPalo.palo:

            cartaj1.valor=cartaj1.potenciador

            cartaTino.valor= cartaTino.potenciador

        elif cartaj1.palo == cartaPalo.palo:

            cartaj1.valor=cartaj1.potenciador

        elif cartaTino.palo == cartaPalo.palo:

            cartaTino.valor= cartaTino.potenciador

        if cartaj1.valor > cartaTino.valor :

                print("Gana jugador 1!!")
                print()
                print()
                montonJ1+=cartasMesa
                puntosj1.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                #cartaRobada=baraja.Robar(12)
                #manoj1.append(cartaRobada)
                #cartaRobada=baraja.Robar(12)
                #manoTino.append(cartaRobada)
                cantaj1=baraja.Cantar(manoj1,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)
                print()

                if cantaj1=="40Bastos":

                    parejaBastos=1
                    puntosj1.append(40)

                elif cantaj1=="20Bastos":

                    parejaBastos=1
                    puntosj1.append(20)

                elif cantaj1=="40Copas":

                    parejaCopas=1
                    puntosj1.append(40)

                elif cantaj1=="20Copas":

                    parejaCopas=1
                    puntosj1.append(20)

                elif cantaj1=="40Espadas":

                    parejaEspadas=1
                    puntosj1.append(40)

                elif cantaj1=="20Espadas":

                    parejaEspadas=1
                    puntosj1.append(20)

                elif cantaj1=="40Oros":

                    parejaOros=1
                    puntosj1.append(40)

                elif cantaj1=="20Oros":

                    parejaOros=1
                    puntosj1.append(20)

                elif cantaj1=="TuteCaballos":

                    puntosj1.append(1000)
                    break

                elif cantaj1=="TuteReyes":

                    puntosj1.append(1000)
                    break

                print(cantaj1)
                print()
                turno=True
                contador=contador-2

        elif cartaj1.valor==cartaTino.valor:

            if turno==True:

                print("Gana Jugador 1!!")
                print()
                print()
                montonJ1+=cartasMesa
                puntosj1.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                #cartaRobada=baraja.Robar(12)
                #manoj1.append(cartaRobada)
                #cartaRobada=baraja.Robar(12)
                #manoTino.append(cartaRobada)
                cantaj1=baraja.Cantar(manoj1,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

                if cantaj1=="40Bastos":

                    parejaBastos=1
                    puntosj1.append(40)

                elif cantaj1=="20Bastos":

                    parejaBastos=1
                    puntosj1.append(20)

                elif cantaj1=="40Copas":

                    parejaCopas=1
                    puntosj1.append(40)

                elif cantaj1=="20Copas":

                    parejaCopas=1
                    puntosj1.append(20)

                elif cantaj1=="40Espadas":

                    parejaEspadas=1
                    puntosj1.append(40)

                elif cantaj1=="20Espadas":

                    parejaEspadas=1
                    puntosj1.append(20)

                elif cantaj1=="40Oros":

                    parejaOros=1
                    puntosj1.append(40)

                elif cantaj1=="20Oros":

                    parejaOros=1
                    puntosj1.append(20)

                elif cantaj1=="TuteCaballos":

                    puntosj1.append(1000)
                    break

                elif cantaj1=="TuteReyes":

                    puntosj1.append(1000)
                    break

                print()
                print(cantaj1)
                print()
                print()
                turno=True
                contador=contador-2
                

            else:

                print("Gana Tino!!")
                print()
                print()
                montonTino+=cartasMesa
                puntosTino.append(total)
                manoj1.remove(cartaj1)
                manoTino.remove(cartaTino)
                #cartaRobada=baraja.Robar(12)
                #manoj1.append(cartaRobada)
                #cartaRobada=baraja.Robar(12)
                #manoTino.append(cartaRobada)
                cantaTino=baraja.Cantar(manoTino,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

                if cantaTino=="40Bastos":

                    parejaBastos=1
                    puntosTino.append(40)

                elif cantaTino=="20Bastos":

                    parejaBastos=1
                    puntosTino.append(20)

                elif cantaTino=="40Copas":

                    parejaCopas=1
                    puntosTino.append(40)

                elif cantaTino=="20Copas":

                    parejaCopas=1
                    puntosTino.append(20)

                elif cantaTino=="40Espadas":

                    parejaEspadas=1
                    puntosTino.append(40)

                elif cantaTino=="20Espadas":

                    parejaEspadas=1
                    puntosTino.append(20)

                elif cantaTino=="40Oros":

                    parejaOros=1
                    puntosTino.append(40)

                elif cantaTino=="20Oros":

                    parejaOros=1
                    puntosTino.append(20)

                elif cantaTino=="TuteCaballos":

                    puntosTino.append(1000)
                    break

                elif cantaTino=="TuteReyes":

                    puntosTino.append(1000)
                    break

                print()
                print(cantaTino)
                print()
                print()
                turno=False
                contador=contador-2

                
            
        else:

            print("Gana Tino!!")
            print()
            print()
            montonTino+=cartasMesa
            puntosTino.append(total)
            manoj1.remove(cartaj1)
            manoTino.remove(cartaTino)
            #cartaRobada=baraja.Robar(12)
            #manoj1.append(cartaRobada)
            #cartaRobada=baraja.Robar(12)
            #manoTino.append(cartaRobada)
            cantaTino=baraja.Cantar(manoTino,idPalo,parejaBastos,parejaCopas,parejaEspadas,parejaOros)

            if cantaTino=="40Bastos":

                parejaBastos=1
                puntosTino.append(40)

            elif cantaTino=="20Bastos":

                parejaBastos=1
                puntosTino.append(20)

            elif cantaTino=="40Copas":

                parejaCopas=1
                puntosTino.append(40)

            elif cantaTino=="20Copas":

                parejaCopas=1
                puntosTino.append(20)

            elif cantaTino=="40Espadas":

                parejaEspadas=1
                puntosTino.append(40)

            elif cantaTino=="20Espadas":

                parejaEspadas=1
                puntosTino.append(20)

            elif cantaTino=="40Oros":

                parejaOros=1
                puntosTino.append(40)

            elif cantaTino=="20Oros":

                parejaOros=1
                puntosTino.append(20)

            elif cantaTino=="TuteCaballos":

                puntosTino.append(1000)
                break

            elif cantaTino=="TuteReyes":

                puntosTino.append(1000)
                break

            print()
            print(cantaTino)
            print()
            print()
            turno=False
            contador=contador-2



       
    else:

        if turno==True:

            puntosj1.append(10)
            print()
            print("La ronda terminó!!")
            print()
            print("El Jugador 1 se lleva las DIEZ DE MONTE!!!")

            break

        else:

            puntosTino.append(10)
            print()
            print("La ronda terminó!!")
            print()
            print("Tino se lleva las DIEZ DE MONTE!!!")

            break


print()        
print()
print("Este es el montón de Jugador 1: ",montonJ1)
print()
print("Este es el montón de Tino: ",montonTino)
print()

totalPuntosj1=reduce(lambda x,y: x+y, puntosj1)

print("La puntuación final de Jugador 1 es: {} Puntos.".format(totalPuntosj1))

print()

totalPuntosTino=reduce(lambda x,y: x+y, puntosTino)

print("La puntuación final de Tino es: {} Puntos.".format(totalPuntosTino))

if totalPuntosj1>totalPuntosTino:

    print()
    print("La partida la ha ganado Jugador 1!!!!")

else:

    print()
    print("La partida la ha ganado Tino!!!!")