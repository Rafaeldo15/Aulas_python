import json
import requests

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

try:
    resposta = requests.get(link_funcionarios)
    lista_funcionarios = resposta.json()
except Exception as abcd:
    print(f"Erro ao conectar com a API de funcionários: {abcd}")
    lista_funcionarios = []

print("--- PROCESSANDO LISTA DE FUNCIONÁRIOS ---\n")

for funcionario in lista_funcionarios:
    if funcionario.get('cep') is None:
        print(f"O funcionário(a) {funcionario['nome']} não tem CEP cadastrado.")

        while True:
            cep_digitado = input("Digite um CEP válido para ele(a): ").strip()
            link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"

            try:
                resposta_cep = requests.get(link_cep)

                if resposta_cep.status_code == 200:
                    dados_cep = resposta_cep.json()

                    if "erro" in dados_cep:
                        print(" CEP inexistente na base do ViaCEP. Tente novamente.")
                        continue

                    if funcionario.get('cidade') is None:
                        funcionario['cidade'] = dados_cep.get('localidade')

                    if funcionario.get('estado') is None:

                        funcionario['estado'] = dados_cep.get('estado') or dados_cep.get('uf')

                    if funcionario.get('bairro') is None:
                        funcionario['bairro'] = dados_cep.get('bairro')

                    if funcionario.get('logradouro') is None:
                        funcionario['logradouro'] = dados_cep.get('logradouro')

                    funcionario['cep'] = cep_digitado
                    print("\nDados de endereço preenchidos com sucesso!\n")
                    break

                else:
                    print(f"️\nErro na API ViaCEP (Status {resposta_cep.status_code}). Tente novamente.\n")

            except requests.exceptions.RequestException:
                print(f"\nErro. Verifique e tente novamente.\n")

print ("\t\t\t" + "-" * 50 + "\n")
print("\t\t\t\t\t\t""--BASE DE DADOS ATUALIZADA--")
print ("\n""\t\t\t" + "-" * 50 )

for funcionario in lista_funcionarios:
    print(funcionario)


nome_arquivo = "dados_funcionarios_atualizados.json"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(lista_funcionarios, arquivo, indent=4, ensure_ascii=False)
print ("\n\n")
print("\t\t\t" + "-" * 50 )
print(f"\t Arquivo '{nome_arquivo}' gerado e salvo com sucesso!")
print("\t\t\t" + "-" * 50)

