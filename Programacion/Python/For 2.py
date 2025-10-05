chs= input("Introduzca su correo electronico: ")
for ch in chs:
    if ch == "@":
        break
    print(ch, end="")
 