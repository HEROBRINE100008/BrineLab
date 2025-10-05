palabra_sin_vocales = ""
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()
for letter in user_word:
    if letter.lower() not in "aeiou":
        continue
    palabra_sin_vocales += letter
return palabra_sin_vocales
print(palabra_sin_vocales)