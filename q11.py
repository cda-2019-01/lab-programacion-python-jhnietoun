##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","


for i in data:
    label=i[0]
    arreglo=[]
    cont=0
    sentinela=False
    for itera,j in enumerate(i):
        if ':' in j:
            elemento= j.split(':') 
            arreglo.append(elemento)
            if sentinela ==False:
                cont=itera 
                sentinela=True
    letras=i[3:cont]
    long_let=len(letras)
    long_tri=len(arreglo)
    
    print ('%s,%s,%s'%(str(label),str(long_let),str(long_tri)))