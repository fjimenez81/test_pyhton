print("Vamos a calcular un prestamo")
print()

dinero=float(input("Introduce el dinero que desees: "))

print()

interes=float(input("Introduce el interés del prestamo: "))

print()

años=int(input("Introduce los años para amortizar el prestamo: "))

print()

resultado=dinero*(1+interes/100)**años

print()

print("El prestamo de ",dinero,"euros ,al interés de",interes,"y en ",años,"para amortizar es:",resultado)