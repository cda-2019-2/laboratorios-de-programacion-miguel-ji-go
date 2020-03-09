##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]

col1=[row[0] for row in datos]
col1=sorted(col1)
diccionario={}
for letra in col1:
    if letra in diccionario:
        diccionario[letra]=diccionario[letra]+1
    else:
        diccionario[letra]=1
for i in diccionario:
    print(i + ',' + str(diccionario[i])) 

