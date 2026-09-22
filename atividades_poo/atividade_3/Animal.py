class Animal():
    def __init__(self, nome, idade, nivel_de_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_de_fome = nivel_de_fome


    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade >=0:
            self.__idade = idade

        else:
            return "Idade Inválida"


