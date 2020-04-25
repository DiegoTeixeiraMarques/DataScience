pesos = [1, 1, 1]
vies = 1
coeficiente = 0.3
DR = 0
matriz = [[0, 0, -1, "null"], [0, 1, -1, "null"], [1, 0, -1, "null"], [1, 1, 1, "null"]]
fim = False
#matriz = [[0, 0, -1, "null"], [0, 1, 1, "null"], [1, 0, 1, "null"], [1, 1, -1, "null"]]

def percepton(indice):
    # Faz a soma dos produtos dos X pelos Pesos
    soma = matriz[indice][0] * pesos[0] + matriz[indice][1] * pesos[1] + vies * pesos[2]
    # Excecuta a função de ativação
    classe = ativacao(soma) 
    # Verifica se os pesos atendem ao resultado esperado
    if classe != matriz[indice][2]:
        # Reinicia a matriz para cálculo de novos pesos
        reiniciarMatriz(indice)
        print("Indice: ", indice)
        # Calcula o erro
        DR = calcularDiferenca(matriz[indice][2], classe)
        print("DR: ", DR)
        # Recalcula os pesos
        recalculoPeso(indice, DR)
    else:
        # Atribui ok se os pesos condicionarem ao resultado esperado
        matriz[indice][3] = "ok"
        # Verifcia se a matriz está com todos os P atendidos pelos pesos
        return verificaConclusao()
    return False

def verificaConclusao():
    for i in range(len(matriz)):
        if matriz[i][3] != "ok":
            return False
            #print("Matriz: ", matriz)
    return True

def reiniciarMatriz(indice):
    # Atribui null a todos os P da matriz, pois o peso não satisfez o resultado esperado
    for i in range(len(matriz)):
        matriz[i][3] = "null"

def ativacao(soma):
    if soma >= 0:
        return 1
    else:
        return -1

def calcularDiferenca(desejado, obtido):
    print("Desejado: ", desejado)
    print("Obtido: ", obtido)
    return desejado - obtido


def recalculoPeso(indice, DR):
    #print(pesos[0], " + ", coeficiente, " * ", DR, " * ", matriz[indice][0])
    #print(pesos[1], " + ", coeficiente, " * ", DR, " * ", matriz[indice][1])
    #print(pesos[2], " + ", coeficiente, " * ", DR, " * ", vies)
    pesos[0] = round(pesos[0] + coeficiente * DR * matriz[indice][0], 2)
    pesos[1] = round(pesos[1] + coeficiente * DR * matriz[indice][1], 2)
    pesos[2] = round(pesos[2] + coeficiente * DR * vies, 2)
    print("Pesos: ", pesos)
    print("------------------------")

def pegarIndice():
    # Retorna o índice do primeiro P que encontrar null
    for indice in range(len(matriz)):
        if matriz[indice][3] == "null":
            return indice

if __name__ == '__main__':

    while fim == False:
        indice = pegarIndice()
        fim = percepton(indice)

        

  
   