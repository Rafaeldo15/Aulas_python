class Produto:
    def __init__(self, nome_produto, preco, quantidade_estoque):
        self.__nome_produto = nome_produto
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque


    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade

        else:
            print("Error: quantidade inválida")

    def realizar_venda(self):
        if self.__quantidade_estoque > 0:
            self.__quantidade_estoque -= 1


produto1= Produto(
    "Sabão",
    10,
    50
)
produto2= Produto(
    "Macarrão",
    20.50,
    100
)
produto3= Produto("Arroz",
                  20,
                  1000
                  )
adicionar_estoque = produto1.adicionar_estoque(10)
print(adicionar_estoque.__dict__)
