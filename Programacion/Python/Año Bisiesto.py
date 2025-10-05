while True:
	year = int(input("Introduce un año o digite 0 para salir: "))
	if year == 0:
			print("Saliendo del programa.")
			break
	if year < 1582:
                print("No esta dentro del período del calendario Gregoriano")
	else:
		if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
			print("Año Bisiesto")
		else:
			print("Año Común")