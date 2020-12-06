from os import system
system("cls")

def pal(frase):
    for i in range (len (frase)):
        if frase[i] == " ":
            fraseA = frase.replace(frase[i],"")
    A = 0
    B = 0
    for i in reversed (range (len (fraseA))):
      if fraseA[i].lower() == fraseA[B].lower():
        A += 1
        B += 1
    if len (fraseA) == A:
      return "Tu frase es un palíndromo :)"
    else:
      return "Tu frase no es un palíndromo :("
frase = input ("Escribeme una frase : ")
print (pal (frase))
