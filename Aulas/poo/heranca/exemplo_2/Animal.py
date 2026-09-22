class Animal:
    def __init__(self, tipo, idade):
        self.tipo = tipo
        self.idade = idade

    def comer (self):
        print(f' O animal {self.tipo} está comendo')

    def dormir (self):
        print(f"O animal {self.tipo} está dormindo")

    def MostrarIdade(self):
        print (f"o anial {self.tipo} tem a idade de {self.idade}")
