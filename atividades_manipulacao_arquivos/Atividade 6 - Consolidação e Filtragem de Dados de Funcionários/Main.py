import json


with open ("base1.json", 'r', encoding="utf-8") as arquivo:
    dados1 = json.load(arquivo)

with open ("base2.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)

with open ("base3.json", "r", encoding="utf-8") as arquivo:
    dados3 = json.load(arquivo)

lista_aniversariantes = []



for aniversariante in dados1:
    dicionario_aniversariante = {
        "nome": aniversariante["nome"],
        "aniversario": aniversariante["aniversario"]
    }
    lista_aniversariantes.append(dicionario_aniversariante)
for aniversariante in dados2:
    dicionario_aniversariante = {
        "nome": aniversariante["nome"],
        "aniversario": aniversariante["aniversario"]
    }
    lista_aniversariantes.append(dicionario_aniversariante)
for aniversariante in dados3:
    dicionario_aniversariante = {
        "nome": aniversariante["nome"],
        "aniversario": aniversariante["aniversario"]
    }
    lista_aniversariantes.append(dicionario_aniversariante)

with open ("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

with open ("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

print(lista_aniversariantes)
