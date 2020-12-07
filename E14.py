from os import system
system("cls")

def mesnombre(fecha):

    dia, mes, año = fecha[:2], fecha[3:5], fecha[-4:]
    mesA = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
    for k in mesA.items():
        if mes == k:
            mesB = mesA.get(k)
    print (dia," de ",mesB," de ",año)
fecha = input ("Dame una fecha en numero --> Dia/Mes/Año : ")
mesnombre(fecha)