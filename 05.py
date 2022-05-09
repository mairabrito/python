#quantitativo
def quantitativo(Tabela, Filtro, n):
  colecaoTarefas =  sorted(list(set(Tabela['Tarefas'].tolist()))) 
  aux = 1

  for i in range(len(colecaoTarefas)):
    PlanilhaAUX =(Tabela.loc[Tabela['Tarefas']==colecaoTarefas[i]]) #Tabela aux - Tarefa
    if(Filtro != 'Sem filtro'):
      df_Q = PlanilhaAUX.loc[PlanilhaAUX['Submetido a'].str.contains(str(Filtro))] #Tabela do Filtro escolhido
    else:
      df_Q = PlanilhaAUX

    print(color.CBLUEBG2+color.CBOLD+f'\n {Filtro} - {colecaoTarefas[i]} \n'+color.CEND)
    print('Total de trabalhos: ', end='')
    print(color.CBOLD+color.CYELLOW2+str(len(df_Q.index))+color.CEND) #total

    colecaoFiltro= sorted(list(set(df_Q['Submetido a'].tolist()))) #Coleçao do Filtro
    PlanilhaQ = DataFrame(colecaoFiltro, columns=['Coleção']) #Construir Planilha 
    quantitativo = []
  

    for i in range(len(colecaoFiltro)):
      PlanilhaAUX2 = df_Q.loc[df_Q['Submetido a']==colecaoFiltro[i]] #Tabela de cada elemento do filtro
      quantitativo.append(len(PlanilhaAUX2.index)) #Quantitativo de cada elemento

    PlanilhaQ['Quantidade'] = quantitativo
    index = len(colecaoFiltro)
  
    total = PlanilhaQ['Quantidade'].sum() #Calcular o total na coluna
    PlanilhaQ.loc[index]= ['TOTAL', total] #Add o total na ultima linha

    if (n == 1):
      PlanilhaQ.to_excel('Quantitativo'+str(aux)+'.xlsx', index=False) #exportar
      aux +=1
  
    with pd.option_context("display.max_rows", 1000):
      display(HTML(PlanilhaQ.to_html(index=False)))
    print('\n\n')
    
quantitativo(df, 'TCC', 1)
