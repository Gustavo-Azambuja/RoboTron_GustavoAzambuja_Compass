import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
for linha in tabela.index:
    name = tabela.loc[linha, 'Name']
    age = tabela.loc[linha, 'Age']
    if tabela.loc[linha, 'Year'] > 1987 and tabela.loc[linha, 'Year'] < 1999:
        print(f'O ator {name} tinha {age} anos quando ganhou o óscar')