# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    members_of_user = input(f"Agrega a {member} a la lista: ")
    beatles.append(members_of_user)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-2]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista