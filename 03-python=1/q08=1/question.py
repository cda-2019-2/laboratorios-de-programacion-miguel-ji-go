##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
col1=[(row[0],row[1]) for row in datos] # separa las columnas 1ty 2
col1
grupo=sorted(set([row[1] for row in datos]))# agrupa y organiza los numeros de la columna 1 
grupo

for i in grupo:
 lista = []
 for j in datos:
   num=j[1]
   if i == num:
    lista.append(j[0])
 lista=sorted(set(lista))
 print((i,lista)) 

