from os import system
system("cls")

def contador(frase):
    a=0
    e=0
    i=0
    o=0
    u=0
    for k in range (len (frase)):
        if (frase[k]=="a"):
            a+=1
        if (frase[k]=="e"):
            e+=1
        if (frase[k]=="i"):
            i+=1
        if (frase[k]=="o"):
            o+=1
        if (frase[k]=="u"):
            u+=1
    print ("a=",a,"e=",e,"i=",i,"o=",o,"u=",u)
frase = input("Escribeme una frase : ")
contador(frase)