#essa foi uma versão que tinha feito, adicionando valor a uma variavel com letras
# pois não consegui criar uma variável com número
"""a = "Cachorro-quente R$ 10.00"
b = "Hambúrguer R$ 15.00"
c = "Batata frita R$ 8.00"
d = "Refrigerante R$ 5.00"

res=int(input("Digite o número do lanche: "))

match res:
    case 'a': print(f"{'a'}")
    case 'b': print(f"{'b'}")
    case 'c': print(f"{'c'}")
    case 'd': print(f"{'d'}")"""



valor_cachorro_quente = ("R$ 10,00")
valor_hamburguer = ("15,00")
valor_batata_frita = ("8,00")
valor_refrigerante = ("5,00")
codigo = int(input("Digite o código do item (1 a 4): "))

#criei uma varíavel com valores ajustáveis para os itens, e adicionei eles no print. em um
#caso hipotético de um estabelecimento usando, caso os valores alterasse
#era só alterar na variável invés de todo código.
if codigo == 1:
    print(f"Produto: Cachorro-quente | Preço: {valor_cachorro_quente}")
elif codigo == 2:
    print(f"Produto: Hambúrguer | Preço: {valor_hamburguer}")
elif codigo == 3:
    print(f"Produto: Batata Frita | Preço: {valor_batata_frita}")
elif codigo == 4:
    print(f"Produto: Refrigerante | Preço: {valor_refrigerante}")
else:
    print("Código inválido")



