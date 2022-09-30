import json

def retornar_json():
    with open("campeonato.json", encoding="utf-8") as json_normal :
    
     json_jogo = json.load(json_normal)

    return json_jogo
campeonato = retornar_json()
print (campeonato)