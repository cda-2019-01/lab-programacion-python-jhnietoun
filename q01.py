##
## Imprima la suma de la segunda columna.
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
for i in data:                                      #Se crea ciclo for
    total = sum(float(i[1]) for i in data)          #Almacena la suma la segunda fila del archivo en la variable "total"
print (total)                                       #Imprime la variable total