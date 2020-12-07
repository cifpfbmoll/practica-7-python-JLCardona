from os import system
system("cls")

def leer(frase):
    for i in range (len (frase)):
        print (frase[i])
frase = input ("Escribeme una frase : ")
leer(frase)