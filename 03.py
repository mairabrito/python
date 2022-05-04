#@title ###**Filtrar uma planilha por valor: a partir dos valores de uma coluna desejada.** { vertical-output: true }

def tratar_index (colecao):
  while True: #Trata o index errado
    print('\n# DIGITE O INDEX DO VALOR QUE DESEJA FILTRAR:', end='')
    option = int(input())
    if((option >=0) and (option < len(colecao))):
      break
    else:
      print('INDEX DIGITADO NÃO CONTÉM NA COLEÇÃO. TENTE NOVAMENTE...\n')
  return option

def filtro_por_valor (colecao, planilha,coluna):

  print('# ------------------ Coleção ------------------\n')
  for i in range(len(colecao)):
    print(f'[ {i:^3}] - { colecao[i]}') #listar a coleção
  
  option = tratar_index(colecao)
  
  planilha_aux = (planilha.loc[planilha[coluna]==colecao[option]])
  print('\n# ARQUIVO SALVO COM SUCESSO!  \n')
  
  return planilha_aux  

#Criar lista da coleção da coluna escolhida, ordenando e eliminando os valores repetidos
colecao = sorted(list(set(df['Submetido a'].tolist()))) 

df1 = filtro_por_valor(colecao, df, 'Submetido a')
df1
