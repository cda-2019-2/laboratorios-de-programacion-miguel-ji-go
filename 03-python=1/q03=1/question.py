##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
datos
col2=sorted([[row[0],row[1]] for row in datos])
letra=sorted(set([row[0] for row in datos]))
for i in letra:
 suma = 0
 for j in col2:
   letra=j[0]
   if i == letra:
    suma = suma + int(j[1])
 print(i + ',' + str(suma))

