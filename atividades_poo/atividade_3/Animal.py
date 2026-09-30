#criando a classe
class Animal():
    #criando o construtor
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome if nivel_fome >= 0.0 else 100

    #usando metodo get
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade #após o return não da pra digitar nada embaixo que o valor não será retornado
        #exemplo se adicionasse um print nessa linha

    #usando o set para idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            self.__idade = nova_idade

        else:
            print ("Erro: Idade Inválida")

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, novo_nivel_fome):
        if novo_nivel_fome < 0:
            novo_nivel_fome = 0


        elif novo_nivel_fome > 100:
            novo_nivel_fome = 100
            print("limite máximo atingido!")


        elif novo_nivel_fome > 50:
            print("O animal está com muita fome!")


        self.__nivel_fome = novo_nivel_fome

    def alimentar(self, quantidade_comida):
        print(f"Alimentando o animal com {quantidade_comida} de comida.")
        self.nivel_fome = self.nivel_fome - quantidade_comida

    def exibir_resumo (self):
        print (f"animal: {self.nome};\n"
               f"idade: {self.idade} anos; \n"
               f"nível de fome: {self.nivel_fome}.")

    def emitir_som(self):
        print (f"{self.nome} faz um som genérico")





