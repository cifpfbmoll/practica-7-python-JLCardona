from os import system
system("cls")

def PalCapi(palabranumero):
    A = 0
    B = 0
    for ind in reversed (range (0, len(palabranumero))):
      if palabranumero[ind].lower() == palabranumero[B].lower():
        A += 1
        B += 1
    if len (palabranumero) == A:
      return "Tu palabra o numero es palindromo :)"
    else:
      return "Tu palabra o numero no es palindromo :("
palabranumero = input ("Escribeme una palabra o número : ")
print(PalCapi(palabranumero))