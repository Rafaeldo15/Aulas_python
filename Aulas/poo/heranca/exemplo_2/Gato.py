from Animal import Animal

class Gato(Animal):
    def __init__(self, tipo, nome, idade):
        super().__init__(tipo, idade)
        self.nome = nome
