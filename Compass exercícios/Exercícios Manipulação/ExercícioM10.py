import pandas as pd

tabela = pd.read_csv("Oscar.csv", encoding="utf-8", sep=",")
filme = tabela['Movie'][0]
print(filme)