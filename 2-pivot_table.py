import pandas as pd

# 1 - Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")

# python é uma liguagem de tipagem dinâmica
# print(type(data)) 

#2 - Selecionando colunas
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3 - Criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# 4 - Exportando a tabela pivô em arquivo Excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")