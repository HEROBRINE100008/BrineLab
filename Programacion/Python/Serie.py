Serie = int(input("Elige una opción 1. 2. 3. "))
if Serie == 1:
    Contador = 1
    while Contador < 8:
        print(Contador, ", ", end="")
        Contador += 1
elif Serie == 2:
    Contador = 1
    while Contador < 16:
        print(Contador, ", ", end="")
        Contador += 2
elif Serie == 3:
    Contador =1
    while Contador < 32:
        print(Contador, ", ", end="")
        Contador += 3
else:
    print("Opción no válida.")