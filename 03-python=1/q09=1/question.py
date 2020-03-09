##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
col5=[(row[4]) for row in datos]
col5
p= [(row.split(",")) for row in col5]
p= [j for row in p for j in row]
p= [row.split (":") for row in p]
clave=sorted(set([row[0] for row in p]))
clave

for i in clave:
 cuenta = 0
 for j in p:
   letra=j[0]
   if i == letra:
    cuenta= cuenta + 1
 print(i,cuenta,sep=',') 




