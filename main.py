# -*- coding: utf-8 -*-

"""script_vista_teste.ipynb

Original file is located produced at Google Collab

IMPORTANTE: coloque o link do seu extrato csv da Noh antes de rodar os códigos em input_file

"""

from IPython.display import display
import pandas as pd

# Coloque o nome do arquivo do seu extrato csv da Noh
input_file = 'Noh_extrato_28082025_06092025.csv'
output_file = f'processed_{input_file.split('.')[0]}.xlsx'

df_noh = pd.read_csv(f"./input_files/{input_file}")

df_noh.info()

df_noh.head()

"""# Excluir movimentações internas"""

df_noh = df_noh[df_noh['Método'] != 'Noh']
display(df_noh.head())

df_noh = df_noh.dropna(subset=['Método'])
display(df_noh.info())

df_noh['Método'].unique()

"""# unir descrição e iniciante"""

df_noh['Descrição'] = df_noh['Descrição'].astype(str) + ' - ' + df_noh['Iniciador'].astype(str)
display(df_noh.head())

"""# Excluir colunas"""

del df_noh['Iniciador']
display(df_noh.head())

del df_noh['Tipo']
display(df_noh.head())

"""# Adicionar novas colunas"""

df_noh['Orçamento'] = ''
display(df_noh.head())

df_noh['Categoria'] = ''
display(df_noh.head())

del df_noh['Método']
display(df_noh.head())

df_noh['Meio de Pagamento'] = 'Noh'
display(df_noh.head())

"""# Troca dos valores

"""

df_noh['Valor'] = df_noh['Valor'].astype(str).str.replace('.', '', regex=False).str.replace('R$', '', regex=False).str.replace(' ', '', regex=False).str.replace('\xa0', '', regex=False).str.replace(',', '.', regex=False)
df_noh['Valor'] = df_noh['Valor'].astype(float)
display(df_noh.head())
display(df_noh.info())

"""# exportar"""

df_noh.to_excel(f"./output_files/{output_file}", index=False)
