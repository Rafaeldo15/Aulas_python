from Animal import Animal


class Mamifero(Animal):
    def __init__(self,nome, idade, nivel_de_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_de_fome)
        self.__velocidade_kmh = velocidade_kmh