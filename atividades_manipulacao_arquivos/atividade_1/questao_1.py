

usuario = input('Digite seu nome: ')

carrinho = []
total = 0

while True:
    produto= input('Digite o nome do produto (digite fim para sair): ')
    if produto == 'fim':
        print ("encerrando programa")
        break
    valor = float(input('Digite o valor do produto: '))
    total += valor

    carrinho.append([produto, valor])

with open("carrinho.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write(f"Usuario: {usuario}\n")
    arquivo.write("-" * 30 + "\n")

    for item in carrinho:
        arquivo.write(f"{item[0]}: {item[1]:.2f}\n")
        
    arquivo.write("-" * 30 + "\n")
    arquivo.write(f"Total = R${total:.2f} \n")


print ("\n ---- PROCESSANDO PAGAMENTO ----\n")
print(f" produtos adicionado ao carrinho {carrinho}")
print(f"Total dos seus produtos foi {total}")




#erro, o codigo esta subscrevendo o que já esta escrito por ultimo. salva so 1 variavel.
#erro 2, não consegui adicionar o total ao recibo
