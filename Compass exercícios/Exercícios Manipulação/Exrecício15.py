import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
for linha in tabela.index:
    if tabela.loc[linha,'Movie'] != 'The Revenant':
        filme = tabela.loc[linha,'Movie']
        print(filme)
