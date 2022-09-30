from traceback import print_tb
import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
for linha in tabela.index:
    if tabela.loc[linha, 'Year'] == 1993:
        artista = tabela.loc[linha, 'Name']
        print(artista)