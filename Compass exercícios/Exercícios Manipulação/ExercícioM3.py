import json
from tkinter import Place

def retornar_json():
    with open("partida.json", encoding="utf-8") as json_normal :
    
     json_jogo = json.load(json_normal)

    return json_jogo
partida = retornar_json()

NEsdatio = partida["copa-do-brasil"][0]["estadio"]["nome_popular"] 
Placar = partida["copa-do-brasil"][0]["placar"]
Statusjogo = partida["copa-do-brasil"][0]["status"] 
print(NEsdatio)
print(Placar)
print(Statusjogo)