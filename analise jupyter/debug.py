# importando os módulos (bibliotecas)
import pandas as pd

# Import DS Jair
dfj = pd.read_json("jairbolsonaro.json")

#Carregando Data set das 'STOP WORDS'
sw = pd.read_csv("stopwords.txt", header = None, names=["Palavra"])

Palavras_N = sw['Palavra'].str.split()

Palavras_jair = dfj['full_text'].str.split()

#print(type(Palavras_N))
#print(type(Palavras_jair))

dictj = dict()

for Frases in Palavras_jair:
    for Palavras in Frases:
            if Palavras in dictj:
                dictj[Palavras] = dictj[Palavras] + 1
            else: 
                dictj[Palavras] = 1

#print('dictj: ', dictj)

dfj = pd.DataFrame(list(dictj.items()), columns=['Palavra', 'QTD'])
#sw = pd.DataFrame(sw, columns=['Palavra'])

print(len(dfj))

print("sw: ",sw)

ndfj = dfj[~dfj.Palavra.isin(sw.Palavra.values)] 
print(ndfj.sort_values(['QTD'],ascending=False).head(1000))

print(len(ndfj))