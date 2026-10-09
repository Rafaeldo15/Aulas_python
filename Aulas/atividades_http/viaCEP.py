from operator import truediv

import requests
import json
historico_pesquisa = []

with open("viaCEP.json") as f:
    viaCEP = json.load(f)
    historico_pesquisa.append(viaCEP)

nova_pesquisa = []

while True:
    cep_digitado =  input("Digite seu cep ou sair para finalizar: ")
    link = f"http://viacep.com.br/ws/{cep_digitado}/json/"
    resposta = requests.get(link)

    if cep_digitado.lower() == 'sair':
        print("Encerrando o programa e salvando histórico final...")
        break

    if resposta.status_code == 200:
        print ("Requisição realizada com sucesso!")

    else:
        print ("Erro inesperado na requisição")
    nova_pesquisa.append(resposta.json())

    print("Adicionado ao JSON com sucesso!")
    print(resposta.json())

historico_pesquisa.extend(nova_pesquisa)

with open("viaCEP.json", "w", encoding='utf-8' ) as file:
    json.dump(historico_pesquisa, file, ensure_ascii=False, indent=4)


