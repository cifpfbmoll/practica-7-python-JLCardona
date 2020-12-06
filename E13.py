from os import system
system("cls")
from time import time

def forprimo(numero):
    
    resto = 1
    for i in range(numero):
        if ((i!=0) and (i!=1) and (numero%i==0)):
            resto = 0
    if (resto == 0):
        return False
    else:
        return True
def whileprimo(numero):
    
    resto = 1
    M = 1
    while(resto!=0):
        M += 1
        resto = numero%M
    if (M == numero):
        return True
    else:
        return False
numero = int (input ("Dame un número : "))
inicio = time()
print (forprimo (numero))
fin = time() - inicio
print ("Tu for tarda : %.10f segundos :)" %fin)
inicio = time()
print (whileprimo (numero))
fin = time() - inicio
print ("Tu while tarda : %.10f segundos :)" %fin)