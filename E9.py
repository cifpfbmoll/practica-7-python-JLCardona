from os import system
system("cls")

def rima(palabraA,palabraB):
    if palabraA[-3:] == palabraB[-3:]:
        print ("Tus palabras ",palabraA," y ",palabraB," sí riman :)")
    elif palabraA[-2:] == palabraB[-2:]:
        print("Tus palabras ",palabraA," y ",palabraB," riman medianamente :/")
    else:
        print("Tus palabras ",palabraA," y ",palabraB," no riman nada :(")
palabraA = input("Escribeme una palabra : ")
palabraB = input("Ahora escribeme otra palabra : ")
rima (palabraA,palabraB)