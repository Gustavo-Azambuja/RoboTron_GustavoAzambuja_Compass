import json

with open('campeonato.json', encoding="utf-8") as p:
    campeonato = json.load(p)

ea = campeonato["edicao_atual"]
fa = campeonato["fase_atual"]
ra = campeonato["rodada_atual"]

lista = [ea, fa, ra]

for x in lista:
    for y in x:
        print(f"\"{y}\": \"{x[y]}\"")
        break