##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
import pandas as pd
df = pd.read_csv("tbl1.tsv",sep = '\t')
df = df.sort_values(by=['_c4'])
df= df.groupby('_c0')['_c4'].apply(','.join).reset_index()
df.columns = ['_c0','lista']
print(df)

