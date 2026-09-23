


class Produto:
    def __init__(self, nome: str, preco: float, quantidade_estoque: int):
        self.__nome = nome
        self.__preco = preco if preco >= 0 else 0.0
        self.__quantidade_estoque = quantidade_estoque if quantidade_estoque >= 0 else 0

    def adicionar_estoque(self, quantidade: int):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade: int):
        if 0 < quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
        else:
            print("Venda negada: Estoque insuficiente")

    def aplicar_desconto(self, percentual: float):
        if 0 < percentual <= 80:
            self.__preco -= self.__preco * (percentual / 100)
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Estoque: {self.__quantidade_estoque}")

produto1 = Produto("Shampoo", 100, 10)

produto1.adicionar_estoque(100)
produto1.exibir_resumo()
produto1.realizar_venda(80)
produto1.exibir_resumo()
