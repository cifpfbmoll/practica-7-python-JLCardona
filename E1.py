from os import system
system("cls")

def texto(letras):
    print(letras.lower())
    print(letras.upper())
letras = input ("Escribeme un texto : ")
texto(letras)