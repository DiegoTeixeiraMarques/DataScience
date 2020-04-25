import random
import math

# Algoritmo K-means

pessoa1 = ['Maria', 1, 1]
pessoa2 = ['João', 9.4, 6.4]
pessoa3 = ['José', 2.5, 2.1]
pessoa4 = ['Antonio', 8, 7.7]
pessoa5 = ['Francisco', 0.5, 2.2]
pessoa6 = ['Xico', 7.9, 8.4]
pessoa7 = ['Mari', 7, 7]
pessoa8 = ['Zé', 2.8, 0.8]
pessoa9 = ['Jo', 1.2, 3]
pessoa10 = ['Wilton', 7.8, 6.1]
#pessoa11 = ['Outro', 'Sem pelo', 'mamifero']
#pessoa12 = ['Outro2', 'Com pelo', 'mamifero']

dataSetProc = []
dataSet = []
xLista = []
yLista = []
centroid1 = [0, 0]
centroid2 = [0, 0]

def criarDataSet():
    dataSet.append([pessoa1, 0])
    dataSet.append([pessoa2, 0])
    dataSet.append([pessoa3, 0])
    dataSet.append([pessoa4, 0])
    dataSet.append([pessoa5, 0])
    dataSet.append([pessoa6, 0])
    dataSet.append([pessoa7, 0])
    dataSet.append([pessoa8, 0])
    dataSet.append([pessoa9, 0])
    dataSet.append([pessoa10, 0])
    #dataSet.append([pessoa11, 0])
    #dataSet.append([pessoa12, 0])

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    #l.sort()
    return l

def atribuirRotulos(dataSet, xLista, yLista):

    # Separa os atributos em duas listas para posteriormente atriburi os rotulos
    for i in range(len(dataSet)):

        xLista.append(dataSet[i][0][1])
        yLista.append(dataSet[i][0][2])

    # Remove valores duplicados para atribuir os rotulos
    xLista = remove_repetidos(xLista)
    yLista = remove_repetidos(yLista)

    rotulo = 1
    for i in range(len(xLista)):
        idade = xLista[i]
        xLista[i] = (idade, rotulo)
        rotulo = rotulo + 1

    rotulo = 1
    for i in range(len(yLista)):
        idade = yLista[i]
        yLista[i] = (idade, rotulo)
        rotulo = rotulo + 1

    for i in range(len(dataSet)):
        nome = dataSet[i][0][0]
        idade = dataSet[i][0][1]
        salario = dataSet[i][0][2]

        for i in range(len(xLista)):
            if type(idade) == int or type(idade) == float:
                x = idade
                break
            else: 
                xLista[i][0] == idade
                x = xLista[i][1]  
        for i in range(len(yLista)):
            if type(salario) == int or type(salario) == float:
                y = salario
                break
            else:
                yLista[i][0] == salario
                y = yLista[i][1]
        
        dataSetProc.append([nome, x, y, 0])

    return xLista, yLista, dataSetProc


def calcularCentroids(xLista, yLista, centroid1, centroid2, dataSetProc = []):

    if centroid1 == [0, 0] and centroid2 == [0, 0]:
        centroid1 = [random.randrange(1, len(xLista)), random.randrange(1, len(yLista))]
        while centroid2 == [0, 0] or centroid1 == centroid2:
            centroid2 = [random.randrange(1, len(xLista)), random.randrange(1, len(yLista))]
    else:
        qtd = 0
        total = 0
        #Média X no cluster 1
        for i in range(len(dataSetProc)):
            if dataSetProc[i][3] == 1:
                qtd = qtd + 1
                total = total + dataSetProc[i][1]
        if qtd == 0:
            centroid1[0] = centroid1[0]
        else:
            centroid1[0] = total/qtd

        qtd = 0
        total = 0
        #Média Y no cluster 1
        for i in range(len(dataSetProc)):
            if dataSetProc[i][3] == 1:
                qtd = qtd + 1
                total = total + dataSetProc[i][2]
        if qtd == 0:
            centroid1[1] = centroid1[1]
        else:
            centroid1[1] = total/qtd

        qtd = 0
        total = 0
        #Média X no cluster 2
        for i in range(len(dataSetProc)):
            if dataSetProc[i][3] == 2:
                qtd = qtd + 1
                total = total + dataSetProc[i][1]
        if qtd == 0:
            centroid2[0] = centroid2[0]
        else:
            centroid2[0] = total/qtd

        qtd = 0
        total = 0
        #Média X no cluster 1
        for i in range(len(dataSetProc)):
            if dataSetProc[i][3] == 2:
                qtd = qtd + 1
                total = total + dataSetProc[i][2]
        if qtd == 0:
            centroid2[1] = centroid2[1]
        else:
            centroid2[1] = total/qtd
   
    return centroid1, centroid2

def calcularDistancias(dataSetProc, centroid1, centroid2):
    verificador = False
    for i in range(len(dataSetProc)):
        
        distancia1 = math.sqrt(((centroid1[1] - dataSetProc[i][2]) ** 2) + ((centroid1[0] - dataSetProc[i][1]) ** 2))
        distancia2 = math.sqrt(((centroid2[1] - dataSetProc[i][2]) ** 2) + ((centroid2[0] - dataSetProc[i][1]) ** 2))

        if distancia1 < distancia2:
            #Verifica se mudou de cluster
            if dataSetProc[i][3] != 1:
                verificador = True
            #Atribui o cluster
            dataSetProc[i][3] = 1
        else:
            #Verifica se mudou de cluster
            if dataSetProc[i][3] != 2:
                verificador = True
            #Atribui o cluster
            dataSetProc[i][3] = 2
    #print('Verificador: ', verificador)
    #print(dataSetProc)
    #print('***************************************')
    return verificador, dataSetProc

criarDataSet()
xLista, yLista, dataSetProc = atribuirRotulos(dataSet, xLista, yLista)

centroid1, centroid2 = calcularCentroids(xLista, yLista, centroid1, centroid2, dataSetProc)
verificador = True

# Verifica se houve mudança de cluster
while verificador == True:
    
    # Calcula as distâncias para os centroids
    verificador, dataSetProc = calcularDistancias(dataSetProc, centroid1, centroid2)
    # Recalcula a média dos centroids
    centroid1, centroid2 = calcularCentroids(xLista, yLista, centroid1, centroid2, dataSetProc)
    
#print(dataSetProc)

for i in range(len(dataSetProc)):
    print(dataSetProc[i])






