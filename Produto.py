class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for item in self.produtos:
            print(item.nome, item.preco)



produto1 = Produto(
    "Liquidificador",
    100
)
produto2 = Produto(
    "Cama",
    500
)
produto3 = Produto(
    "game",
    2000
)
pedido1 = Pedido()
pedido2 = Pedido()
pedido3 = Pedido()

pedido1.adicionar_produto(produto1)
pedido2.adicionar_produto(produto2)
pedido3.adicionar_produto(produto3)


print (Pedido().produtos)
