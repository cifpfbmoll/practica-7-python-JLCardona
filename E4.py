from os import system
system("cls")

def sustitucion(frase):
    for i in range (len (frase)):
        if frase[i] == " ":
            frase = frase[:i] +"*"+ frase[(i+1):]
    return frase
frase = input("Escribeme una frase : ")
print (sustitucion (frase))