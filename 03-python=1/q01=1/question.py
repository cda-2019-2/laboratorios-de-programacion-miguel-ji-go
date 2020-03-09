##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]

suma = 0
for i in datos:
  suma = suma + int(i[1])
print(suma)


