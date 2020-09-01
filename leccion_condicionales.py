print("Programa de becas")
distancia=int(input("Introduce la distancia hasta la universidad: "))
hermanos=int(input("Introduce el numero de hermanos en la familia: "))
salario=int(input("Introduce el salario familiar anual: "))
if distancia>40 and hermanos>2 and salario<=20000:
	print("Tienes derecho a beca")
else:
	print("No Tienes derecho a beca")