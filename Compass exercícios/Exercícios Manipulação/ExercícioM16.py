import pandas as pd

tabela = pd.read_csv("tabela_periodica.csv", encoding="utf-8", sep=",")
for linha in tabela.index:
        Tabela= tabela.loc[linha, 'Simbolo']
        print(Tabela)
