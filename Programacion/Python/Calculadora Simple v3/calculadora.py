#Suma

def suma(a,b):
   return a + b

#Resta

def resta(a,b):
    return a - b

#Multiplicación

def multiplicación(a,b):
    return a * b

#División

def división(a,b):
    if a != 0 and b != 0:
        return a / b
    else:
        print("No es posible dividir por 0")
    
if __name__ == "__main__":
    v1 = int(input("Dame el primer valor: "))
    v2 = int(input("Dame el segundo valor: "))
    print(suma(v1,v2))
    print(resta(v1,v2))
    print(multiplicación(v1,v2))
    print(división(v1,v2))
    