import requests

link = 'http://192.168.205.100:8080/usuarios'
resposta = requests.get(link)

print (f"Status busca dados: {resposta}")

meus_dados = {
    'nome':'Rafael',
    'email':'naopossuoemail@yahoo.com.br'
}

envio = requests.post(
    link,
    json=meus_dados)


print (f"status envio de dados: {envio}")
