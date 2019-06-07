##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
for i in data:
    label = str(i[0])
    arreglo=[]
    for j in i:
        if ':' in j:
            elemento= j.split(':') 
            arreglo.append(int(elemento[1]))
            
    suma_elemento=sum(arreglo)
    print ('%s,%s'%(label,str(suma_elemento)))
