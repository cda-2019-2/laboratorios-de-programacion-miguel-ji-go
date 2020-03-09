##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
col=[[row[1],row[3].split(',')] for row in datos]

lista= []
for i in col:
  for j in i[1]:
    b=i[0], j[0]
    lista.append(b)

letra= sorted(set([row[1]for row in lista]))

for i in letra:
  suma=0
  for j in lista:
    letra=j[1]
    if i==letra:
      suma= suma+int(j[0])
  print (i,str(suma),sep=',')

