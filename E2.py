from os import system
system("cls")

def NomApe(lista):
    completo = lista[0]
    for i in range(1,len(lista)):
        completo += " " + lista[i]
    return completo
lista = []
nom = input("Dame tu nombre : ")
lista.append(nom)
ape1 = input("Dame tu 1er apellido : ")
lista.append(ape1)
ape2 = input("Dame tu 2o apellido : ")
lista.append(ape2)
print (NomApe (lista))