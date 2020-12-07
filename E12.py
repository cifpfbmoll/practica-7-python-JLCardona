from os import system
system("cls")

def contador(frase):
    letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    puntuacion = [".","·",":",",",";","-","_"]
    palabra = 0
    for i in range (len (frase)):
        if frase[i]==" " and (frase[i-1] in puntuacion or frase[i-1] in letra):
            palabra += 1
    if len (frase)!=0:
        palabra += 1  
    return palabra
frase = input ("Escribeme una frase : ")
print ("Tu frase esta formada por ",contador(frase)," palabras :)")