#@title ###**Importar e exibir planilha** { vertical-output: true }

import pandas as pd 
from google.colab import data_table # formatação
data_table.enable_dataframe_formatter()

#Ler palhinha
df = pd.read_excel('/COMINHO')
#df
data_table.DataTable(df, num_rows_per_page=5)
