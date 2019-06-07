##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
arreglo=[]
data_dic={}

for i in data:
    sentinela=False
    for j in i:
        if ':' in j and sentinela==False:
            sentinela=True
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
    v_max= max(elemento)
    v_min= min(elemento)
    print ('%s,%s,%s' %(str(i),str(v_max),str(v_min)))  
