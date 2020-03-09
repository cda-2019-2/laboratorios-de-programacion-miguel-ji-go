##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
col2= sorted([[row[0],row[1]] for row in datos])
letra= sorted(set([row[0] for row in datos]))
letra

for i in letra:
 lista = []
 for j in col2:
   letra=j[0]
   if i == letra:
    lista.append(j[1])
 print(i + "," + max(lista) + "," + min(lista))

