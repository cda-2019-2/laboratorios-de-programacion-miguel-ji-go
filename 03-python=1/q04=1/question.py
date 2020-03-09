##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  >>> Escriba su codigo a partir de este punto <<<
datos=open('data.csv','r').readlines()
datos=[row.split('\t') for row in datos]
fechas= [row[2] for row in datos]
fechas
mes=[row.split('-')for row in fechas]
mes= sorted([row[1]for row in mes])
mes

diccionario={}

for mes in mes:
    if mes in diccionario:
        diccionario[mes]=diccionario[mes]+1
    else:
        diccionario[mes]=1

for i in diccionario:
    print(i + ',' + str(diccionario[i]))


