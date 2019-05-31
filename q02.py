##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
data= sorted ([row[0] for row in data])             #Crea una lista únicamente con los elementos de la primera fila

result = {}                                         #Crea un diccionario vacío denominado "result"
for item in data:                                   #Crea ciclo for para los items del diccionario
    if item in result:                              
        result[item] = result.get(item)+1           #Recorre la lista y va contando cada vez que encuentra la misma letra
    else:
        result[item] = 1
        
for letra,rep in result.items():                    #Se indica que las llaves se llamarán "letra" y los valores "rep"
    print(str(letra)+','+str(rep))                  # Imprime con el formato solicitado

    
    