##
##  Programación en Bash
##  ===========================================================================
##
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
##
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original.
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivos=$(ls *.csv)
for file in ${Archivos[*]}; do 
    if [ -f 1.csv ]; then
        cat $file | sed '/^[[:space:]]*$/d' | nl | sed 's/[[:space:]]//g' | sed "s/\([0-9]\)\([A-Z]\)/"${file}\,"\1,\2,/g" >>1.csv
    else
        cat $file | sed '/^[[:space:]]*$/d' | nl | sed 's/[[:space:]]//g' | sed "s/\([0-9]\)\([A-Z]\)/"${file}\,"\1,\2,/g" >1.csv
    fi
done
filename=1.csv
while read -r line; do 
    m=$(echo $line | awk '{print NF}' FS=",")
    i=4
    for ((i; i<=m; i++)); do 
        VAR1="$(echo $line | cut -d"," -f1)",""
        VAR2="$(echo $line | cut -d"," -f2)",""
        VAR3="$(echo $line | cut -d"," -f3)",""
        VAR4=$(echo $line | cut -d"," -f$i)
        VAR5="$VAR1$VAR2$VAR3$VAR4"
        echo "$VAR5"
    done
done <$filename
rm 1.csv