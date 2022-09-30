import json

with open('campeonato.json', encoding="utf-8") as p:
    campeonato = json.load(p)
for chave in campeonato:
    print(chave)