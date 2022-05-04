#@title Criar uma lista de planilhas a parte dos valores da coluna escolhida. { vertical-output: true }
def ListaDePlanilhas (Tabela,coluna, colecao):

  #popular a lista de planilhas
  for i in range(len(colecao)):
    Planilha_aux =(Tabela.loc[Tabela[coluna]==colecao[i]])
    Planilhas.append(Planilha_aux)

#lista no escoplo global
Planilhas = []

#Criar lista da coleção da coluna escolhida, ordenando e 
#eliminando os valores repetidos

colecao = sorted(list(set(df['Submetido a'].tolist()))) 
#chama função
ListaDePlanilhas(df, 'Submetido a', colecao)

#resultado (exemplo)
Planilhas[1]
