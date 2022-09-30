import json
from time import time
from tkinter import Place

def retornar_json():
    with open("partida.json", encoding="utf-8") as json_normal :
    
     json_jogo = json.load(json_normal)

    return json_jogo
partida = retornar_json()

timevisitante = partida["copa-do-brasil"][0]["time_visitante"] 
print(timevisitante)