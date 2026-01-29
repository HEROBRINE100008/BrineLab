def answer():
    try:
        if question == "real":
            print("O NOOOOOOOO FAAAKEEEEEEER")

        elif question == "faker":
            print("O NOOOOOOOO RIAAAAAALLL")
    except:
        print("Escribe real o faker tarupido")
while True:
    question = input("Real or Faker: ").lower()

    answer()
