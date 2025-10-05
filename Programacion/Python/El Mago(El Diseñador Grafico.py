secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
UserNumber = int(input("¿Cuál es el número secreto?"))
print(UserNumber)
if UserNumber == 777:
    print("¡Bien hecho, muggle! Eres libre ahora.")

else:
    while UserNumber == 777:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        UserNumber = input("¿Cuál es el número secreto?")
    