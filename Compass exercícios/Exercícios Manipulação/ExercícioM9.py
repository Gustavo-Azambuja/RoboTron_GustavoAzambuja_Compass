import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
filme = tabela['Age']
print(filme)