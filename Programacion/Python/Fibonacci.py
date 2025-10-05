a = 0
b = 1
c = 0

while c < 22:
    if c == 0:
        print(a,",", end="")
        c = a + b
        b = a
        a = c
    else:
        print(c, ",", end="")
        c = a + b
        b = a
        a = c