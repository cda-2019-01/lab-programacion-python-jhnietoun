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
data= [[row[0], row[1]] for row in data]            #Selecciona únicamente las dos primeras columnas del archivo
data= sorted ([row for row in data])                #Organiza la información ascendentemente  

subtotal=[]                                         #Se crea lalista vacía "subtotal"
sumaA=0                                             #Se crea una variable con valor inicial 0 para almacenar el valor de la suma de cada resgitro
sumaB=0
sumaC=0
sumaD=0
sumaE=0
for i in range(len(data)):                          #Crea el ciclo for para que recorra la extensión de la nueva lista data de 2 columnas
    if(data[i][0]=='A'):                            #Busca que la letra de la priemra columna sea "A"
        sumaA=sumaA+int(data[i][1])                 #Almacena en la variable sumaA el acumulado de los valores sumados de los resgistros con letra A
    elif(data[i][0]=='B'):                          #Busca que la letra de la priemra columna sea "B"
        sumaB=sumaB+int(data[i][1])                 #Almacena en la variable sumaB el acumulado de los valores sumados de los resgistros con letra B
    elif(data[i][0]=='C'):                          #Busca que la letra de la priemra columna sea "C"
        sumaC=sumaC+int(data[i][1])                 #Almacena en la variable sumaC el acumulado de los valores sumados de los resgistros con letra C
    elif(data[i][0]=='D'):                          #Busca que la letra de la priemra columna sea "D"
        sumaD=sumaD+int(data[i][1])                 #Almacena en la variable sumaD el acumulado de los valores sumados de los resgistros con letra D
    elif(data[i][0]=='E'):                          #Busca que la letra de la priemra columna sea "E"
        sumaE=sumaE+int(data[i][1])                 #Almacena en la variable sumaE el acumulado de los valores sumados de los resgistros con letra E
subtotal.append(['A',sumaA])                        #Adiciona a la lista subtotal el cálculo realizado
subtotal.append(['B',sumaB])
subtotal.append(['C',sumaC])
subtotal.append(['D',sumaD])
subtotal.append(['E',sumaE])

result = dict(subtotal)                             #Se transforma la lista "subtotal" en el diccionario "result"

for letra,suma in result.items():                   #Se indica que las llaves se llamarán "letra" y los valores "suma"
    print(str(letra)+','+str(suma))                 #Imprime con el formato solicitado


