class Produto:
    def __init__(self, nome_produto, preco, quantidade, estoque):
        self.__nome_produto = nome_produto
        self.__preco = preco
        self.__quantidade = quantidade
        self.__estoque = estoque


    @property
    def get_nome_produto(self):
        produto_adicionado = str(input("digite o nome do produto: "))
    def adicionar_produto(self, __nome_produto):
        self.__nome_produto = __nome_produto
        print(f"{__nome_produto} adicionado")

    def preco_venda (self, __preco):
        return "o preço para venda é:", self.__preco

    def quantidade_total (self, __quantidade):
        return "quantidade em estoque:",self.__quantidade


    def adicionar_estoque(self, __estoque):
        if __estoque > 0:
            self.__estoque += 1
        else:
            print('Estoque negativo')

    def realizar_venda(self, __estoque):
        return self.realizar_venda -= 1

