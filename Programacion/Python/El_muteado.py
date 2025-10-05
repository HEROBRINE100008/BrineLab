Galleton = 0
seDesmutea = False

while seDesmutea == False:
    Galleton += 1
    print("*Sonido de Galleton* PO!")
    seDesmutea = input("te va a demutea? (si/no): ").strip().lower() == "si"
    if seDesmutea == False:
        print("A po' tu vas a seguir muteado, chequea ahora")
if Galleton == 1:
    print(f"Te demuteate en el primer {Galleton}, Good booooyy!")
else:
    print(f"Te desmuteaste a los {Galleton} Galletones, Leon!.")
