##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
dict_data = {'A':[],'B':[],'C':[],'D':[],'E':[]}

for i in data:
    label = i[0] 
    dict_data[label].append(i[1])

key=['A','B','C','D','E']

for i in key:
    x=dict_data [i] 
    v_max= max(x)
    v_min= min(x)
    print ('%s,%s,%s' %(str(i),str(v_max),str(v_min)))   







