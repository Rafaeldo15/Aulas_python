

usuario = input('Digite seu nome: ')

carrinho = []
total = 0

while True:
    produto= input('Digite o nome do produto (digite fim para sair): ')
    if produto == 'fim':
        print ("encerrando programa")
        break
    valor = float(input('Digite o valor do produto: '))
    total = total + valor

    carrinho.append([produto, valor])

with open("carrinho.txt", 'w', encoding='utf-8') as arquivo:
    for carrinho in carrinho:
        nome_produto = carrinho[0]
        preco_produto = carrinho[1]

        arquivo.write(f"{nome_produto}: {preco_produto:.2f}\n")



print("\nProcessando pagamento\n")
print(carrinho)




#erro, o codigo esta subscrevendo o que já esta escrito por ultimo. salva so 1 variavel.
#erro 2, não consegui adicionar o total ao recibo
