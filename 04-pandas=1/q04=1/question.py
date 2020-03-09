##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
import pandas as pd
df=pd.read_csv('tbl1.tsv', sep='\t')
r=df['_c4'].str.upper()
r=sorted(r.unique())
print(r)

