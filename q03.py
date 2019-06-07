##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
dic_data = {'A':0,'B':0,'C':0,'D':0,'E':0}

for i in data:
	label=i[0]
	dic_data[label] += int(i[1])

result=['A','B','C','D','E']
for i in range (len(result)):
    label=result [i]
    value=dic_data[label]
    print ('%s,%s' %(str(label),str(value)))
