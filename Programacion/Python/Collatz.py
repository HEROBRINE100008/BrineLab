c0 = int(input("Introduce un número: "))
pasos = 0
while c0 != 1:
    if c0 % 2 != 0:
        c0 = 3 * c0 + 1
        pasos += 1
        print(round(c0))
    else:
        c0 /= 2
        pasos += 1
        print(round(c0))
print("pasos = ", pasos )