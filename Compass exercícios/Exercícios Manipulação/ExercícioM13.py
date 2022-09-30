import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
movie_year = []
for linha in tabela.index:
    ano = tabela.loc[linha, 'Year']
    filme = tabela.loc[linha, 'Movie']
    movie_year.append(f'{ano},{filme}')
tabela = tabela.assign(MovieAndYear = movie_year)


print(tabela)