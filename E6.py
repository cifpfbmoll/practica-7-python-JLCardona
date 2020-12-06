from os import system
system("cls")

def estado(caracteres,nombres):
    for i in range (len (nombres)):
        if (nombres[i]==caracteres):
            return "El carácter está dentro de tu nombre : )"
nombres = input("Escribeme tu nombre : ")
caracteres = input("Dame un carácter : ")
print (estado (caracteres,nombres))