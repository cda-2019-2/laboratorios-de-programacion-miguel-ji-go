##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
import pandas as pd
df1 = pd.read_csv("tbl0.tsv",sep = '\t')
df2 = pd.read_csv("tbl2.tsv",sep = '\t')
df= pd.merge(df1,df2)
r=df.groupby('_c1')['_c5b'].sum()
print(r)



