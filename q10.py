##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
arreglo=[]
data_dic={}

for i in data:
    for j in i:
        if ':' in j:
            elemento= j.split(':') 
            arreglo.append(elemento)

for i in arreglo:
    label = i[0]
    value = i[1]
    if label not in data_dic:
        data_dic[label]=[value]
    else: 
        data_dic[label].append(value)
        
result=sorted(data_dic)

for i in result:
    elemento=data_dic[i]
    data_len= len(elemento)
    print ('%s,%s'%(str(i),str(data_len)))