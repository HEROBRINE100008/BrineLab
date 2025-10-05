fnam = input("¿Me puedes dar tu nombre por favor? ") 
lnam = input("¿Me puedes dar tu apellido por favor? ")
if lnam == "no" or "No" or "NO" or "nO":
    print("Gracias. ")
    print("\nTu nombre es " + fnam + ".")
else:
    print("Gracias. ")
    print("\nTu nombre es " + fnam + " " + lnam + ".")