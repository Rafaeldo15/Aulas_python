import json


with open ("base1.json", "r", encoding="utf-8") as arquivo:
    dados1 = json.load(arquivo)

with open ("base2.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)

with open ("base3.json", "r", encoding="utf-8") as arquivo:
    dados3 = json.load(arquivo)

lista_aniversariantes = []

with open ("aniversariantes.json", "w", encoding="utf-8") as dados4:
    pass