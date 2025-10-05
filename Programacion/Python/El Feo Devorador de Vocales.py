palabra_sin_vocales = ""
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()
for letter in user_word:
    if letter.lower() not in "aeiou":
        palabra_sin_vocales += letter + "\n"
        continue
print(palabra_sin_vocales)