from os import system
system("cls")

def eliminacion(frase):
    
    for i in range (len (frase)):
        if frase[i] == " ":
            frases = frase.replace(frase[i],"")
    return frases
frase = input ("Escribeme una frase : ")
print (eliminacion(frase))