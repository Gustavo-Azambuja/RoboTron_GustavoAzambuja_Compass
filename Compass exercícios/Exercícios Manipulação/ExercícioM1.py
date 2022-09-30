import json

def retornar_json():
    with open("partida.json", encoding="utf-8") as json_normal :
    
     json_jogo = json.load(json_normal)

    return json_jogo
partida = retornar_json()
print (partida)


