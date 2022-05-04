#@title ###**Filtrar por palavra - selecionar a coluna e filtra buscando a palavra na coluna desejada** { vertical-output: true }

#Filtrar por palavra
def filtrar_por_palavra (Tabela, coluna):
  word = input()
  df_word = Tabela.loc[Tabela[coluna].str.contains(word)]
  print('\n# ...  \n')
  
  return df_word

#df_por_palavra = filtrar_por_palavra(df,'Submetido a') 
#df_por_palavra = filtrar_por_palavra(df,'Tarefas')
df_por_palavra = filtrar_por_palavra(df,'Submetido por')
df_por_palavra

#OBS.: caso retorne uma planilha vazia (apenas com o cabeçalho), 
#significa que a palavra buscada não tem na coluna desejada
