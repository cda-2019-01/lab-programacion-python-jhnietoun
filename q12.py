##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
data_dict={}

for i in data:
    sentinela =False
    index = 0
    for itera, j in enumerate(i):
        if ':' in j and sentinela==False:
            sentinela=True
            index = itera
    var_let = i[3:index]
    valor = int(i[1])
    
    for x in var_let:
        if x in data_dict:
            data_dict[x]+=valor
        else:
            data_dict[x]=valor

label=sorted(data_dict)

for i in label:
    valor=data_dict[i]

    print ('%s,%d'% (i,int(valor)))