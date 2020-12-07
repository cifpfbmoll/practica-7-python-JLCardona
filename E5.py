from os import system
system("cls")

def cambio(vocales,frase):
    lista = ["A","E","I","O","U"]
    for i in range (len (frase)):
        if frase[i] in lista:
            frase = frase[:i] + vocales + frase[(i+1):]
    return frase
frase = input("Escribeme una frase : ")
vocales = input("Dame una vocal : ")
print (cambio (vocales,frase))