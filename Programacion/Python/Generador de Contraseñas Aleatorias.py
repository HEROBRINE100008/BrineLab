from random import choice

def Nth(L):
    Qt = "abcdefghijklmnopqrstuvwxyz" #NNN
    for i in range(L):
        print(choice(Qt), end='')

def MyNuSy(L):
    Qt123 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?" #YYY
    for i in range(L):
        print(choice(Qt123), end='')

def MyNu(L):
    Qt12 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #YYN
    for i in range(L):
        print(choice(Qt12), end='')

def MySy(L):
    Qt13 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;':\",.<>?" #YNY
    for i in range(L):
        print(choice(Qt13), end='')
        
def My(L):
    Qt1= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #YNN
    for i in range(L):
        print(choice(Qt1), end='')
        
def NuSy(L):
    Qt23 = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?" #NYY
    for i in range(L):
        print(choice(Qt23), end='')
        
def Nu(L):
    Qt2 = "abcdefghijklmnopqrstuvwxyz0123456789" #NYN
    for i in range(L):
        print(choice(Qt2), end='')
        
def Sy(L):
    Qt3 = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;':\",.<>?" #NNY
    for i in range(L):
        print(choice(Qt3), end='')
        
Letras_minusculas = list("abcdefghijklmnopqrstuvwxyz")
Letras_mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Letras_numeros = list("0123456789")
Simbolos = list("!@#$%^&*()_+-=[]{}|;':\",.<>?")

Length = int(input("Tamaño de la contraseña: "))

Question1 = input("¿Incluir mayúsculas? (y/n): ")
Question2 = input("¿Incluir números? (y/n): ")
Question3 = input("¿Incluir símbolos? (y/n): ")

if Question1 == "y":
    if Question2 == "y":
        if Question3 == "y":
            MyNuSy(Length)
        if Question3 == "n":
            MyNu(Length)
    elif Question2 == "n":
        if Question3 == "y":
            MySy(Length)
        elif Question3 == "n":
            My(Length)
elif Question1 == "n":
    if Question2 == "y":
        if Question3 == "y":
            NuSy(Length)
        elif Question3 == "n":
            Nu(Length)
    elif Question2 == "n":
        if Question3 == "y":
            Sy(Length)
        elif Question3 == "n":
            Nth(Length)