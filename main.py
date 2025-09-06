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

df_noh = df_noh[df_noh["Método"] != "Noh"]
display(df_noh.head())

df_noh = df_noh.dropna(subset=["Método"])
display(df_noh.info())

df_noh["Método"].unique()

"""# unir descrição e iniciante"""

df_noh["Descrição"] = (
    df_noh["Descrição"].astype(str) + " - " + df_noh["Iniciador"].astype(str)
)
display(df_noh.head())

"""# Excluir colunas"""

del df_noh["Iniciador"]
display(df_noh.head())

del df_noh["Tipo"]
display(df_noh.head())

"""# Adicionar novas colunas"""

df_noh["Orçamento"] = ""
display(df_noh.head())

df_noh["Categoria"] = ""
display(df_noh.head())

del df_noh["Método"]
display(df_noh.head())

df_noh["Meio de Pagamento"] = "Noh"
display(df_noh.head())

"""# Troca dos valores

"""

df_noh["Valor"] = (
    df_noh["Valor"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace("R$", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.replace("\xa0", "", regex=False)
    .str.replace(",", ".", regex=False)
)
df_noh["Valor"] = df_noh["Valor"].astype(float)
display(df_noh.head())
display(df_noh.info())


def derive_category(df, conversion_values=CATEGORY_CONVERSION_VALUES):
    description = df["Descrição"]
    description = description.lower()
    for key in conversion_values.keys():
        if key in description:
            return conversion_values[key]
    else:
        return "Não Categorizado"


def insert_budget(df, budget_map=BUDGET_CATEGORY_MAPPING):
    value = df["Valor"]
    # valores default
    if value < 0:
        default = "Despesa não Categorizada"
    else:
        default = "Receita não Categorizada"

    category = df["Categoria"]
    category = category.lower()
    for budget, categories in budget_map.items():
        if category in categories:
            return budget
    return default


df_noh["Categoria"] = df_noh.apply(derive_category, axis=1)
df_noh["Orçamento"] = df_noh.apply(insert_budget, axis=1)
display(df_noh.head())

"""# exportar"""

df_noh.to_excel(f"./output_files/{output_file}", index=False)
