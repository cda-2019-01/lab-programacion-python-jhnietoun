##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data = open('data.csv', 'r'). readlines()           #Lee el archivo
data = [row[0:-1] for row in data]                  #Elimina los retornos del carro   
data = [x.replace('\t', ',') for x in data]         #Reemplaza los separador "\t" por ","
data = [row.split(',') for row in data]             #Separa los elementos de las listas por ","
data= ([row[2] for row in data])                    #Crea una lista únicamente con los elementos de la tercera columna
mes= [i[5:7] for i in data]                         #Extrae el mes
mes = sorted (mes)                                  #Organiza los registros ascendentemente por mes

result = {}                                         #Crea un diccionario vacío denominado "result"
for item in mes:                                    #Crea ciclo for para los items del diccionario
    if item in result:                              
        result[item] = result.get(item)+1           #Recorre la lista y va contando cada vez que encuentra el mismo mes
    else:
        result[item] = 1
        
for mes,rep in result.items():                      #Se indica que las llaves se llamarán "mes" y los valores "rep"
    print (str(mes)+','+str(rep))                   # Imprime con el formato solicitado

