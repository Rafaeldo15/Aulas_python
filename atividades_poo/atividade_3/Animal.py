#criando a classe
class Animal():
    #criando o construtor
    def __init__(self, nome, idade, nivel_de_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_de_fome = nivel_de_fome if nivel_de_fome >= 0.0 else 100

    #usando metodo get
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self, idade):
        return self.__idade
    #usando o set para idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            self.__idade = idade

        else:
            print ("Erro: Idade Inválida")

    @property
    def nivel_de_fome(self):
        return self.__nivel_de_fome

    @nivel_de_fome.setter
    def nivel_de_fome(self, nivel_de_fome):
        if nivel_de_fome > 50:
            print("O animal está com muita fome!")
        self.__nivel_de_fome = nivel_de_fome

    def alimentar (self, nivel_de_fome):
        if alimentar > nivel_de_fome:
            print("Quantidade de comida maior que a fome.")

    def exibir_resumo (self):
        print (f"Animal : {nome} tem {idade} anos e esta com {nivel_de_fome}")





